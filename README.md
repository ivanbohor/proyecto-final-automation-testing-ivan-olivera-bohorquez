Proyecto Final Talento Tech- Automatización de Testing (UI + API)
Este proyecto implementa un framework de pruebas automatizadas híbrido, abarcando tanto pruebas de interfaz (UI) para el sitio SauceDemo, como pruebas de backend (API) para JSONPlaceholder, utilizando Python y Selenium con el patrón Page Object Model.

🎯 Propósito del Proyecto
El objetivo es validar la calidad del software en dos frentes:

UI (Frontend): Automatizar flujos de negocio críticos como Login, Compra E2E y Carrito.

API (Backend): Validar los métodos HTTP (CRUD) y códigos de respuesta del servidor.

🛠️ Tecnologías Utilizadas
Python: Lenguaje de programación principal.

Pytest: Framework para estructurar, ejecutar y reportar pruebas.

Selenium WebDriver: Automatización de interfaz web.

Requests: Librería para automatización de pruebas de API.

Page Object Model (POM): Patrón de diseño para mantener el código organizado y escalable.

Faker: Generación de datos aleatorios para pruebas robustas.

WebDriver Manager: Gestión automática de drivers del navegador.

Git/GitHub: Control de versiones.

📁 Estructura del Proyecto

├── data/
│   └── usuarios.json         # Datos para Data Driven Testing (Login)
├── pages/                    # Page Object Model (Clases de páginas)
│   ├── base_page.py          # Métodos comunes y esperas
│   ├── login_page.py         # Lógica de Login
│   └── checkout_page.py      # Lógica de Compra
├── screenshots/              # Capturas de pantalla (se generan autom. al fallar)
├── test/
│   ├── conftest.py           # Configuración del Driver y Hooks de reporte
│   ├── test_api.py           # Pruebas de Backend (CRUD)
│   └── test_saucedemo.py     # Pruebas de Frontend (UI)
├── utils/
│   ├── helpers.py            # Funciones auxiliares (Carga de datos)
│   └── __init__.py
└── requirements.txt          # Lista de dependencias del proyecto


⚙️Instalación de Dependencias
 Tener Python instalado.

Crea un entorno virtual (opcional pero recomendado).

Instala todas las dependencias automáticamente:
pip install -r requirements.txt 
(Esto instalará selenium, pytest, requests, faker y webdriver-manager).

▶️ Ejecución de las Pruebas
Para ejecutar todas las pruebas (UI + API) y ver el resultado en consola:

python -m pytest -v

Para ejecutar solo las pruebas de API:

python -m pytest test/test_api.py -v -s


Para ejecutar solo las pruebas de UI (SauceDemo):

Bash

python -m pytest test/test_saucedemo.py -v
Para generar un reporte HTML visual:

Bash

python -m pytest -v --html=reporte.html --self-contained-html


✅ Funcionalidades Implementadas
🖥️ UI Testing (SauceDemo)
Patrón Page Object Model (POM): Lógica separada de los tests.

Login Data Driven: Pruebas con múltiples usuarios (estándar, bloqueado, etc.) cargados desde un JSON.

Flujo E2E de Compra:

Login.

Agregar al carrito.

Checkout con datos dinámicos (Faker).

Validación final de orden.

Manejo de Errores: Capturas de pantalla automáticas (screenshots/) cuando un test falla.

Navegación Segura: Ejecución en Modo Incógnito para evitar bloqueos y popups de contraseñas.

🔌 API Testing (JSONPlaceholder)
GET: Obtener listado de usuarios y validar status 200.

POST: Simular creación de usuario y validar ID generado (201).

PUT: Actualizar datos de un usuario y validar consistencia (200).

DELETE: Simular eliminación de registros (200).
