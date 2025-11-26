import pytest
import requests

# CAMBIO DE API: Usamos JSONPlaceholder porque ReqRes está rechazando la conexión
BASE_URL = "https://jsonplaceholder.typicode.com"

# --------------------------------------------------------------------------
# CASO 1: GET - Obtener lista de usuarios
# --------------------------------------------------------------------------
def test_get_users_api():
    print("\n--- API TEST: Obtener Usuarios (GET) ---")
    
    # 1. Request
    response = requests.get(f"{BASE_URL}/users")
    
    # 2. Validaciones
    assert response.status_code == 200, f"Fallo: Status esperado 200, obtenido {response.status_code}"
    
    data = response.json()
    assert len(data) > 0, "La lista de usuarios vino vacía"
    
    # JSONPlaceholder devuelve usuarios reales con email, validamos uno
    print(f"Usuario encontrado: {data[0]['name']} - Email: {data[0]['email']}")

# --------------------------------------------------------------------------
# CASO 2: POST - Crear un usuario
# --------------------------------------------------------------------------
def test_create_user_api():
    print("\n--- API TEST: Crear Usuario (POST) ---")
    
    nuevo_usuario = {
        "name": "Ivan Olivera",
        "username": "ivanqa",
        "email": "ivan@test.com"
    }
    
    # 1. Request
    response = requests.post(f"{BASE_URL}/users", json=nuevo_usuario)
    
    # 2. Validaciones
    # JSONPlaceholder devuelve 201 cuando se crea algo
    assert response.status_code == 201, f"Fallo: Status esperado 201, obtenido {response.status_code}"
    
    data = response.json()
    # Validamos que nos devolvió el ID (significa que se creó)
    assert "id" in data
    assert data['name'] == "Ivan Olivera"
    
    print(f"Usuario creado simulado con ID: {data['id']}")

# --------------------------------------------------------------------------
# CASO 3: PUT - Actualizar un usuario
# --------------------------------------------------------------------------
def test_update_user_api():
    print("\n--- API TEST: Actualizar Usuario (PUT) ---")
    
    user_id = 1
    datos_actualizados = {
        "name": "Ivan Actualizado",
        "email": "nuevo_email@test.com"
    }
    
    # 1. Request
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=datos_actualizados)
    
    # 2. Validaciones
    assert response.status_code == 200
    
    data = response.json()
    assert data['name'] == "Ivan Actualizado"
    
    print("Usuario actualizado correctamente (simulado).")

# --------------------------------------------------------------------------
# CASO 4: DELETE - Borrar un usuario
# --------------------------------------------------------------------------
def test_delete_user_api():
    print("\n--- API TEST: Borrar Usuario (DELETE) ---")
    
    user_id = 1
    
    # 1. Request
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    
    # 2. Validaciones
    # OJO: JSONPlaceholder devuelve 200 en el delete (ReqRes devolvía 204)
    # Ambos son válidos según el estándar HTTP.
    assert response.status_code == 200, f"Fallo: Status esperado 200, obtenido {response.status_code}"
    
    print("Usuario eliminado correctamente (simulado).")