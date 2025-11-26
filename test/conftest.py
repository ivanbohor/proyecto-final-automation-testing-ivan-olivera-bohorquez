import pytest
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Importamos extras para adjuntar contenido al HTML
from pytest_html import extras

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')
    options.add_argument("--disable-search-engine-choice-screen")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    request.cls.driver = driver
    yield driver
    driver.quit()

# --- HOOK: Captura de pantalla y Reporte HTML ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Intentamos recuperar el driver del test
        driver = getattr(item.instance, 'driver', None)
        if driver is None and "driver" in item.funcargs:
             driver = item.funcargs["driver"]
        
        if driver:
            # 1. Guardar archivo físico en carpeta screenshots
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"screenshots/{item.name}_{now}.png"
            driver.save_screenshot(file_name)
            
            # 2. Adjuntar la imagen al reporte HTML (Codificada en Base64)
            # Esto permite ver la foto directamente en el navegador sin abrir archivos aparte
            screenshot_base64 = driver.get_screenshot_as_base64()
            html = (
                f'<div><img src="data:image/png;base64,{screenshot_base64}" '
                f'style="width:400px;height:auto;border:2px solid red;display:block;" '
                f'onclick="window.open(this.src)" align="right"/></div>'
            )
            extra.append(extras.html(html))
            
    report.extra = extra