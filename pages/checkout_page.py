import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def proceder_a_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def ingresar_datos_cliente(self, nombre, apellido, codigo_postal):
        try:
            # Intentar detectar un banner de seguridad (Google Chrome)
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Aceptar') or contains(text(), 'Entendido')]"))
            ).click()
            print("Se cerró el banner de advertencia de contraseña.")
        except:
            print("No apareció el banner de advertencia o no fue detectado.")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys(nombre)
        self.driver.find_element(By.ID, "last-name").send_keys(apellido)
        self.driver.find_element(By.ID, "postal-code").send_keys(codigo_postal)
        self.driver.find_element(By.ID, "continue").click()

    def finalizar_compra(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

    def obtener_mensaje_exito(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
