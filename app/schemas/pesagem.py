from pydantic import BaseModel, Field


class PesagemCreate(BaseModel):
    operador: str
    rota: str
    peso_kg: float = Field(gt=0, description="O peso em kg deve ser maior que zero")
    material: str
