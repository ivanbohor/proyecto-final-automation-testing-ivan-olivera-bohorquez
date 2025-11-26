import pytest
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver(request):
    # --- Configuración del Driver (Igual que tenías antes) ---
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--incognito') # Modo incógnito clave
    options.add_argument("--disable-search-engine-choice-screen")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Inyectamos el driver en el test para que el hook de screenshot lo pueda usar
    request.cls.driver = driver
    yield driver
    driver.quit()

# --- HOOK PARA CAPTURA DE PANTALLA AUTOMÁTICA ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Si el test falló (report.failed)
    if report.when == "call" and report.failed:
        # Recuperamos el driver del test
        driver = getattr(item.instance, 'driver', None)
        if driver is None and "driver" in item.funcargs:
             driver = item.funcargs["driver"]
        
        if driver:
            # Creamos carpeta screenshots si no existe
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            # Nombre descriptivo: NombreTest_Fecha_Hora.png
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"screenshots/{item.name}_{now}.png"
            
            # Tomamos la foto
            driver.save_screenshot(file_name)
            print(f"\n📸 Screenshot guardado en: {file_name}")