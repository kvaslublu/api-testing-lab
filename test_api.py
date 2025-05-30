import requests
from jsonschema import validate
import pytest

# Базовые заголовки с API-ключом
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": "reqres-free-v1"
}

# Схема для проверки структуры ответа
schema = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "data": {"type": "array"}
    },
    "required": ["page", "data"]
}

def test_get_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data

def test_get_users_schema():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)

def test_create_user():
    payload = {"name": "Alice", "job": "Engineer"}
    response = requests.post("https://reqres.in/api/users", json=payload, headers=HEADERS)
    print("Status:", response.status_code, "| Response:", response.text)
    assert response.status_code == 201
    assert "id" in response.json()

@pytest.mark.parametrize("name, job", [("Bob", "QA"), ("Eve", "DevOps")])
def test_create_user_params(name, job):
    payload = {"name": name, "job": job}
    response = requests.post("https://reqres.in/api/users", json=payload, headers=HEADERS)
    print("Status:", response.status_code, "| Response:", response.text)
    assert response.status_code == 201
    assert "id" in response.json()

def test_invalid_login():
    payload = {"email": "test@test"}  # Без пароля — должна быть ошибка
    response = requests.post("https://reqres.in/api/login", json=payload, headers=HEADERS)
    print("Status:", response.status_code, "| Response:", response.text)
    assert response.status_code == 400
    assert "error" in response.json()


