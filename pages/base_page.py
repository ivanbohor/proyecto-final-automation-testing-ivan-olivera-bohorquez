from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.log_service import LogService

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = LogService.get_logger() # Inicializamos el logger

    def encontrar(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def escribir(self, locator, texto):
        elemento = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elemento.clear()
        elemento.send_keys(texto)
        self.log.info(f"⌨️ Escribiendo '{texto}' en el elemento {locator}")

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        self.log.info(f"🖱️ Haciendo Click en {locator}")

    def obtener_texto(self, locator):
        texto = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        self.log.info(f"👀 Texto obtenido: '{texto}' de {locator}")
        return texto

    def esperar_url(self, texto_url):
         WebDriverWait(self.driver, 10).until(EC.url_contains(texto_url))
         self.log.info(f"⏳ Esperando URL que contenga: '{texto_url}'")