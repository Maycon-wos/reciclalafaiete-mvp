from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root_e_login():
    response = client.get("/")
    assert response.status_code == 200


def test_read_pesagem():
    response = client.get("/pesagem")
    assert response.status_code == 200


def test_criar_pesagem_sucesso():
    payload = {
        "operador": "João Silva",
        "rota": "Rota Centro",
        "peso_kg": 45.5,
        "material": "PET",
    }
    response = client.post("/api/pesagem", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["mensagem"] == "Pesagem registada com sucesso!"


def test_criar_pesagem_dados_invalidos():
    payload = {
        "operador": "Jo",
        "rota": "Rota Centro",
        "peso_kg": -5.0,
        "material": "Papelão",
    }
    response = client.post("/api/pesagem", json=payload)
    assert response.status_code == 422
