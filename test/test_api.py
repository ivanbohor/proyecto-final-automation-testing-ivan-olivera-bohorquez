import pytest
import requests
from utils.log_service import LogService

# Inicializamos logger
log = LogService.get_logger()
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_api():
    log.info("--- INICIO API TEST: Obtener Usuarios (GET) ---")
    response = requests.get(f"{BASE_URL}/users")
    log.info(f"Request GET a {BASE_URL}/users - Status: {response.status_code}")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    log.info(f"Usuario encontrado: {data[0]['name']} - Email: {data[0]['email']}")

def test_create_user_api():
    log.info("--- INICIO API TEST: Crear Usuario (POST) ---")
    nuevo_usuario = {"name": "Ivan Olivera", "username": "ivanqa", "email": "ivan@test.com"}
    
    response = requests.post(f"{BASE_URL}/users", json=nuevo_usuario)
    log.info(f"Request POST - Status: {response.status_code}")
    
    assert response.status_code == 201
    data = response.json()
    log.info(f"Usuario creado con ID simulado: {data['id']}")

def test_update_user_api():
    log.info("--- INICIO API TEST: Actualizar Usuario (PUT) ---")
    user_id = 1
    datos = {"name": "Ivan Actualizado", "email": "nuevo@test.com"}
    
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=datos)
    log.info(f"Request PUT usuario {user_id} - Status: {response.status_code}")
    assert response.status_code == 200

def test_delete_user_api():
    log.info("--- INICIO API TEST: Borrar Usuario (DELETE) ---")
    user_id = 1
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    log.info(f"Request DELETE usuario {user_id} - Status: {response.status_code}")
    assert response.status_code == 200