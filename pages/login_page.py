from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Selectores
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, '[data-test="error"]')

    # Acciones
    def ingresar_credenciales(self, usuario, password):
        self.escribir(self.USER_INPUT, usuario)
        self.escribir(self.PASS_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def obtener_mensaje_error(self):
        return self.obtener_texto(self.ERROR_MSG)