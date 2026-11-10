from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import RotaModel


def popular_rotas_iniciais():
    db: Session = SessionLocal()
    try:
        # Verifica se já existem rotas cadastradas no banco .db
        if db.query(RotaModel).count() == 0:
            rotas_iniciais = [
                RotaModel(
                    bairro="Angélica",
                    dia_semana="Quarta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Arcádia",
                    dia_semana="Quarta-feira",
                    turno="Manhã",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Barreira",
                    dia_semana="Segunda-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Bellavinha",
                    dia_semana="Quarta-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="BNH",
                    dia_semana="Quarta-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Cachoeira",
                    dia_semana="Segunda-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Campo Alegre",
                    dia_semana="Quarta-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Chapada",
                    dia_semana="Quarta-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Condomínio Turquesa",
                    dia_semana="Segunda-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Fonte Grande",
                    dia_semana="Quinta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Gigante",
                    dia_semana="Terça-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Granja das Hortênsias",
                    dia_semana="Terça-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Jardim América",
                    dia_semana="Terça-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Jardim dos Inconfidentes",
                    dia_semana="Terça-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Lima Dias I",
                    dia_semana="Segunda-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Lourdes",
                    dia_semana="Quarta-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Manoel Corrêa",
                    dia_semana="Quinta-feira",
                    turno="Manhã",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Manoel de Paula",
                    dia_semana="Quinta-feira",
                    turno="Manhã",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Moinhos",
                    dia_semana="Quinta-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Morada do Sol",
                    dia_semana="Quarta-feira",
                    turno="Manhã",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Morro da Mina",
                    dia_semana="Quarta-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Museu",
                    dia_semana="Terça-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Ouro Verde",
                    dia_semana="Quarta-feira",
                    turno="Manhã",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Paulo VI",
                    dia_semana="Sexta-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Queluz",
                    dia_semana="Quarta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Quinta das Flores",
                    dia_semana="Terça-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Recanto dos Colibris",
                    dia_semana="Quarta-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Rezende",
                    dia_semana="Terça-feira",
                    turno="Manhã e Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Rosário",
                    dia_semana="Quinta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Rua Brasil / Rua Santana (Centro)",
                    dia_semana="Terça-feira",
                    turno="Manhã e Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Sagrado Coração de Jesus",
                    dia_semana="Quinta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Santa Cruz",
                    dia_semana="Segunda-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Santa Luzia",
                    dia_semana="Terça-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Santa Maria",
                    dia_semana="Sexta-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Santa Matilde",
                    dia_semana="Sexta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Santa Terezinha",
                    dia_semana="Segunda-feira",
                    turno="Tarde",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Santo Agostinho",
                    dia_semana="Sexta-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
                RotaModel(
                    bairro="Santo Antônio",
                    dia_semana="Terça-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="São Benedito",
                    dia_semana="Segunda-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="São João",
                    dia_semana="Quinta-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="São Judas Tadeu",
                    dia_semana="Terça-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="São Sebastião",
                    dia_semana="Segunda-feira",
                    turno="Manhã e Tarde",
                    associacao="ASMARCOL",
                ),
                RotaModel(
                    bairro="Satélite",
                    dia_semana="Segunda-feira",
                    turno="Tarde",
                    associacao="ASCOPRE",
                ),
                RotaModel(
                    bairro="Sion",
                    dia_semana="Sexta-feira",
                    turno="Manhã",
                    associacao="ASCOL",
                ),
            ]
            db.add_all(rotas_iniciais)
            db.commit()
    finally:
        db.close()
