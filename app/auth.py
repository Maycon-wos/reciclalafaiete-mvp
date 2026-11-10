from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(tags=["Autenticação"])


class LoginPayload(BaseModel):
    usuario: str
    senha: str


@router.post("/api/login")
async def fazer_login(dados: LoginPayload):
    if dados.usuario == "operador.asmarcol" and dados.senha == "asmarcol2026":
        return {
            "mensagem": "Login efetuado com sucesso!",
            "token": "token_valido_recicla_lafaiete",
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas"
    )
