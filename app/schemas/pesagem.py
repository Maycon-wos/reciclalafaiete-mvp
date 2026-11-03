from pydantic import BaseModel, Field


class PesagemCreate(BaseModel):
    operador: str = Field(
        ..., min_length=3, description="Nome do operador da cooperativa"
    )
    rota: str = Field(..., description="Identificação da rota de coleta seletiva")
    peso_kg: float = Field(
        ..., gt=0, description="Peso do material reciclado em quilogramas"
    )
    material: str = Field(
        ..., description="Tipo de material reciclado (ex: PET, Papelão, Alumínio)"
    )
