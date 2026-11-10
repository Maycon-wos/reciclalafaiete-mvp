from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.init_db import popular_rotas_iniciais
from app.models import ConfiguracaoModel, PesagemModel, RotaModel
from app.routers import pesagem

templates = Jinja2Templates(directory="templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    popular_rotas_iniciais()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(pesagem.router)


# --- SCHEMAS DE VALIDAÇÃO ---
class LoginPayload(BaseModel):
    usuario: str
    senha: str


class MetaUpdate(BaseModel):
    meta_kg: float


# --- ROTAS DE API ---
@app.post("/api/login")
async def fazer_login(payload: LoginPayload):
    usuario_limpo = payload.usuario.strip()
    senha_limpa = payload.senha.strip()

    if usuario_limpo == "operador.teste" and senha_limpa == "senha123":
        return {"mensagem": "Login efetuado com sucesso!", "redirect": "/pesagem"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuário ou senha incorretos.",
    )


@app.post("/api/meta")
async def atualizar_meta(dados: MetaUpdate, db: Session = Depends(get_db)):
    # Busca a meta atual no banco SQLite
    config_meta = (
        db.query(ConfiguracaoModel)
        .filter(ConfiguracaoModel.chave == "meta_ods_kg")
        .first()
    )

    # Se não existir, cria o registro no .db; se existir, atualiza o valor
    if not config_meta:
        config_meta = ConfiguracaoModel(chave="meta_ods_kg", valor=dados.meta_kg)
        db.add(config_meta)
    else:
        config_meta.valor = dados.meta_kg

    db.commit()
    return {"mensagem": "Meta atualizada com sucesso!", "nova_meta": config_meta.valor}


# --- ROTAS DE INTERFACE (HTML) ---
@app.get("/", response_class=RedirectResponse)
async def raiz():
    return RedirectResponse(url="/login")


@app.get("/login", response_class=HTMLResponse)
async def pagina_login(request: Request):
    return templates.TemplateResponse(request, "login.html", {})


@app.get("/pesagem", response_class=HTMLResponse)
async def pagina_pesagem(request: Request, db: Session = Depends(get_db)):
    rotas_db = db.query(RotaModel).order_by(RotaModel.bairro).all()
    # Passamos o operador logado para o template (ajustado para operador.teste)
    operador_atual = "operador.teste"
    return templates.TemplateResponse(
        request, "pesagem.html", {"rotas": rotas_db, "operador": operador_atual}
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def pagina_dashboard(request: Request, db: Session = Depends(get_db)):
    lista_pesagens = db.query(PesagemModel).all()
    peso_total = sum(p.peso for p in lista_pesagens)

    config_meta = (
        db.query(ConfiguracaoModel)
        .filter(ConfiguracaoModel.chave == "meta_ods_kg")
        .first()
    )
    meta_kg = config_meta.valor if config_meta else 10000.0

    porcentagem_meta = min(100.0, (peso_total / meta_kg * 100)) if meta_kg > 0 else 0.0

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "pesagens": lista_pesagens,
            "peso_total": peso_total,
            "meta_kg": meta_kg,
            "porcentagem_meta": round(porcentagem_meta, 1),
        },
    )
