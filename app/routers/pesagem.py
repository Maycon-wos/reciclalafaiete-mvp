from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import PesagemModel
from app.schemas.pesagem import PesagemCreate

router = APIRouter(prefix="/api", tags=["Pesagens"])


@router.post("/pesagem", status_code=status.HTTP_201_CREATED)
async def criar_pesagem(dados: PesagemCreate, db: Session = Depends(get_db)):
    nova_pesagem = PesagemModel(
        operador=dados.operador,
        rota=dados.rota,
        categoria=dados.material,
        peso=dados.peso_kg,
    )
    db.add(nova_pesagem)
    db.commit()
    db.refresh(nova_pesagem)
    return {
        "mensagem": "Pesagem registada com sucesso!",
        "id": nova_pesagem.id,
    }


@router.get("/pesagens")
async def listar_pesagens(db: Session = Depends(get_db)):
    pesagens = db.query(PesagemModel).all()
    return pesagens
