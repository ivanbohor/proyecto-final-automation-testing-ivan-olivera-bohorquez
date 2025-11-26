from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Selectores
    BTN_ADD_CART = (By.CLASS_NAME, "btn_inventory")
    LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    BTN_CHECKOUT = (By.ID, "checkout")
    INPUT_NAME = (By.ID, "first-name")
    INPUT_LASTNAME = (By.ID, "last-name")
    INPUT_ZIP = (By.ID, "postal-code")
    BTN_CONTINUE = (By.ID, "continue")
    TITLE_PAGE = (By.CLASS_NAME, "title")

    # Acciones
    def agregar_al_carrito(self):
        self.click(self.BTN_ADD_CART)

    def ir_al_carrito(self):
        self.click(self.LINK_CARRITO)

    def ir_al_checkout(self):
        self.click(self.BTN_CHECKOUT)

    def llenar_formulario(self, nombre, apellido, postal):
        self.escribir(self.INPUT_NAME, nombre)
        self.escribir(self.INPUT_LASTNAME, apellido)
        self.escribir(self.INPUT_ZIP, postal)

    def finalizar_compra(self):
        self.click(self.BTN_CONTINUE)

    def obtener_titulo(self):
        return self.obtener_texto(self.TITLE_PAGE)