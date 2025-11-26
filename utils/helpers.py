import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# URL Base
URL = "https://www.saucedemo.com/"

def get_driver():
    options = Options()
    options.add_argument('--start-maximized')
    
    #  MODO INCÓGNITO ---
    options.add_argument('--incognito')

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    # Otros bloqueos de seguridad
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-infobars")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        data = json.load(f)
    return data

def login_saucedemo(driver, user, password):
    driver.get(URL)
    
    # Campo Usuario
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'user-name'))
    ).send_keys(user)

    # Campo Contraseña
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'password'))
    ).send_keys(password)

    # Botón Login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'login-button'))
    ).click()