from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.database import Base


class PesagemModel(Base):
    __tablename__ = "pesagens"

    id = Column(Integer, primary_key=True, index=True)
    operador = Column(String, nullable=False)
    rota = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    peso = Column(Float, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)


class RotaModel(Base):
    __tablename__ = "rotas"

    id = Column(Integer, primary_key=True, index=True)
    bairro = Column(String, nullable=False)
    dia_semana = Column(String, nullable=False)
    turno = Column(String, nullable=False)
    associacao = Column(String, nullable=False)


class ConfiguracaoModel(Base):
    __tablename__ = "configuracoes"

    id = Column(Integer, primary_key=True, index=True)
    chave = Column(String, unique=True, nullable=False)
    valor = Column(Float, nullable=False)
