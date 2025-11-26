from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def encontrar(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def escribir(self, locator, texto):
        elemento = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elemento.clear()
        elemento.send_keys(texto)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def obtener_texto(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def esperar_url(self, texto_url):
         WebDriverWait(self.driver, 10).until(EC.url_contains(texto_url))