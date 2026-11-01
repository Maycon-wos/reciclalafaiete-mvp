from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="ReciclaLafaiete API",
    description="MVP de Gestão de Pesagem e Rotas de Coleta Seletiva para a ASMARCOL",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
@app.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):
    """Serve a Tela 1: Autenticação de Usuário (Login)."""
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/pesagem", response_class=HTMLResponse)
async def read_pesagem(request: Request):
    """Serve a Tela 2: Registro de Pesagem e Vinculação de Rotas."""
    return templates.TemplateResponse(request=request, name="pesagem.html")


@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    """Serve a Tela 3: Dashboard e Indicadores de Estoque (KPIs)."""
    return templates.TemplateResponse(request=request, name="dashboard.html")
