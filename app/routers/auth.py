from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["Autenticação"])


class LoginPayload(BaseModel):
    usuario: str
    senha: str


@router.post("/login")
async def fazer_login(payload: LoginPayload):
    u = payload.usuario.strip()
    s = payload.senha.strip()

    if u == "operador.teste" and s == "senha123":
        return {"mensagem": "Login efetuado com sucesso!", "redirect": "/pesagem"}

    # Retorna exatamente o que o servidor comparou para vermos na tela de erro
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Recebido -> Usuário: [{u}] | Senha: [{s}]",
    )
