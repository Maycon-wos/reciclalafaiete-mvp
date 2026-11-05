from datetime import datetime
from pathlib import Path

from fastapi import Depends, FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.schemas.pesagem import PesagemCreate

# 1. Configuração do Banco de Dados SQLite
DATABASE_URL = "sqlite:///./reciclalafaiete.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 2. Modelos do Banco de Dados
class RotaModel(Base):
    __tablename__ = "rotas"
    id = Column(Integer, primary_key=True, index=True)
    bairro = Column(String, nullable=False)
    dia_semana = Column(String, nullable=False)
    turno = Column(String, nullable=False)
    associacao = Column(String, nullable=False)


class PesagemModel(Base):
    __tablename__ = "pesagens"
    id = Column(Integer, primary_key=True, index=True)
    rota = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    peso = Column(Float, nullable=False)
    data_registro = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


# Função para popular automaticamente a tabela de rotas com base na tabela oficial da ASMARCOL
def popular_rotas_iniciais():
    db = SessionLocal()
    if db.query(RotaModel).count() == 0:
        rotas_oficiais = [
            ("Angélica", "Quarta-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Arcádia", "Quarta-feira", "Manhã", "ASCOPRE"),
            ("Barreira", "Segunda-feira", "Manhã", "ASCOL"),
            ("Bellavinha", "Quarta-feira", "Tarde", "ASCOPRE"),
            ("BNH", "Quarta-feira", "Tarde", "ASCOL"),
            ("Cachoeira", "Segunda-feira", "Manhã", "ASCOL"),
            ("Campo Alegre", "Quarta-feira", "Tarde", "ASCOL"),
            ("Chapada", "Quarta-feira", "Tarde", "ASCOPRE"),
            ("Condomínio Turquesa", "Segunda-feira", "Tarde", "ASCOL"),
            ("Fonte Grande", "Quinta-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Gigante", "Terça-feira", "Tarde", "ASCOPRE"),
            ("Granja das Hortências", "Terça-feira", "Manhã", "ASCOL"),
            ("Jardim América", "Terça-feira", "Manhã", "ASCOL"),
            ("Jardim dos Inconfidentes", "Terça-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Lima Dias I", "Segunda-feira", "Tarde", "ASCOPRE"),
            ("Lourdes", "Quarta-feira", "Tarde", "ASCOL"),
            ("Manoel Correa", "Quinta-feira", "Manhã", "ASCOL"),
            ("Manoel de Paula", "Quinta-feira", "Manhã", "ASCOL"),
            ("Moinhos", "Quinta-feira", "Manhã", "ASCOL"),
            ("Morada do Sol", "Quarta-feira", "Manhã", "ASCOL"),
            ("Morro da Mina", "Quarta-feira", "Tarde", "ASCOPRE"),
            ("Museu", "Terça-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Ouro Verde", "Quarta-feira", "Manhã", "ASCOPRE"),
            ("Paulo VI", "Sexta-feira", "Manhã", "ASCOL"),
            ("Queluz", "Quarta-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Quinta das Flores", "Terça-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Recanto dos Colibris", "Quarta-feira", "Manhã", "ASCOL"),
            ("Rezende", "Terça-feira", "Manhã e Tarde", "ASCOPRE"),
            ("Rosário", "Quinta-feira", "Manhã e Tarde", "ASMARCOL"),
            (
                "Rua Brasil / Rua Santana (Centro)",
                "Terça-feira",
                "Manhã e Tarde",
                "ASCOL",
            ),
            ("Sagrado Coração de Jesus", "Quinta-feira", "Manhã e Tarde", "ASCOPRE"),
            ("Santa Cruz", "Segunda-feira", "Tarde", "ASCOL"),
            ("Santa Luzia", "Terça-feira", "Tarde", "ASCOL"),
            ("Santa Maria", "Sexta-feira", "Manhã", "ASCOL"),
            ("Santa Matilde", "Sexta-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Santa Terezinha", "Segunda-feira", "Tarde", "ASCOL"),
            ("Santo Agostinho", "Sexta-feira", "Manhã", "ASCOL"),
            ("Santo Antônio", "Terça-feira", "Manhã e Tarde", "ASMARCOL"),
            ("São Benedito", "Segunda-feira", "Tarde", "ASCOPRE"),
            ("São João", "Quinta-feira", "Manhã e Tarde", "ASMARCOL"),
            ("São Judas Tadeu", "Terça-feira", "Tarde", "ASCOPRE"),
            ("São Sebastião", "Segunda-feira", "Manhã e Tarde", "ASMARCOL"),
            ("Satélite", "Segunda-feira", "Tarde", "ASCOPRE"),
            ("Sion", "Sexta-feira", "Manhã", "ASCOL"),
        ]
        for bairro, dia, turno, assoc in rotas_oficiais:
            db.add(
                RotaModel(bairro=bairro, dia_semana=dia, turno=turno, associacao=assoc)
            )
        db.commit()
    db.close()


popular_rotas_iniciais()

# 3. Inicialização do App FastAPI e Templates
app = FastAPI(
    title="ReciclaLafaiete API",
    description="MVP de Gestão de Pesagem e Rotas de Coleta Seletiva para a ASMARCOL",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 4. Rota de Healthcheck
@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}


# 5. Rotas de Navegação e Transacionais
@app.get("/", response_class=HTMLResponse)
@app.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.post("/login")
async def login_action(usuario: str = Form(...), senha: str = Form(...)):
    return RedirectResponse(url="/pesagem", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/pesagem", response_class=HTMLResponse)
async def read_pesagem(request: Request, db: Session = Depends(get_db)):
    """Busca todas as rotas/bairros reais cadastrados no banco para exibir no select."""
    rotas = db.query(RotaModel).all()
    return templates.TemplateResponse(
        request=request, name="pesagem.html", context={"rotas": rotas}
    )


@app.post("/pesagem", response_class=HTMLResponse)
async def criar_pesagem_form(
    request: Request,
    rota: str = Form(...),
    categoria: str = Form(...),
    peso: float = Form(...),
    db: Session = Depends(get_db),
):
    nova_pesagem = PesagemModel(rota=rota, categoria=categoria, peso=peso)
    db.add(nova_pesagem)
    db.commit()

    rotas = db.query(RotaModel).all()
    mensagem_sucesso = f"Pesagem de {peso:.2f} kg ({categoria}) registada com sucesso!"
    return templates.TemplateResponse(
        request=request,
        name="pesagem.html",
        context={"sucesso": mensagem_sucesso, "rotas": rotas},
    )


@app.post("/api/pesagem", status_code=status.HTTP_201_CREATED)
async def criar_pesagem_api(dados: PesagemCreate, db: Session = Depends(get_db)):
    nova_pesagem = PesagemModel(
        rota=dados.rota, categoria=dados.categoria, peso=dados.peso
    )
    db.add(nova_pesagem)
    db.commit()
    return {
        "mensagem": "Pesagem registada com sucesso!",
        "dados_recebidos": dados.model_dump(),
    }


@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request, db: Session = Depends(get_db)):
    pesagens = db.query(PesagemModel).all()
    total_reciclado = sum(p.peso for p in pesagens)
    rotas_unicas = len(set(p.rota for p in pesagens))

    categorias = {"Plástico PET": 0.0, "Papelão": 0.0, "Alumínio": 0.0, "Vidro": 0.0}
    for p in pesagens:
        if p.categoria in categorias:
            categorias[p.categoria] += p.peso

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "total_reciclado": f"{total_reciclado:,.2f}",
            "rotas_atendidas": rotas_unicas,
            "estoque": categorias,
        },
    )
