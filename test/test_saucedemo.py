import pytest
import sys
import os
from faker import Faker
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

# Configuración para importar utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.helpers import get_data

fake = Faker()
lista_usuarios = get_data('usuarios.json')

# Marcamos que esta clase usa el fixture "driver"
@pytest.mark.usefixtures("driver")
class TestSauceDemo:
    
    @pytest.mark.parametrize("usuario", lista_usuarios)
    def test_login_varios_usuarios(self, driver, usuario):
        login_page = LoginPage(driver)
        
        # Lógica separada: El test solo dice "QUÉ" hacer
        driver.get("https://www.saucedemo.com/")
        
        user_name = usuario['user']
        password = usuario['pass']
        resultado = usuario.get('resultado_esperado', 'exitoso')

        login_page.ingresar_credenciales(user_name, password)
        login_page.click_login()

        if resultado == "exitoso":
            assert "/inventory.html" in driver.current_url
        elif resultado == "fallido":
            assert "locked out" in login_page.obtener_mensaje_error()

    def test_checkout_con_faker(self, driver):
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Login
        driver.get("https://www.saucedemo.com/")
        login_page.ingresar_credenciales("standard_user", "secret_sauce")
        login_page.click_login()

        # 2. Flujo de Compra
        checkout_page.agregar_al_carrito()
        checkout_page.ir_al_carrito()
        checkout_page.ir_al_checkout()

        # 3. Faker
        nombre = fake.first_name()
        apellido = fake.last_name()
        postal = fake.zipcode()

        checkout_page.llenar_formulario(nombre, apellido, postal)
        checkout_page.finalizar_compra()

        # 4. Validar
        # Usamos el método de la BasePage para esperar URL
        checkout_page.esperar_url("checkout-step-two.html")
        assert checkout_page.obtener_titulo() == "Checkout: Overview"