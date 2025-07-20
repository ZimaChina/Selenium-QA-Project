from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def agregar_producto_al_carrito(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_btn)
        ).click()

    def ir_al_carrito(self):
        self.driver.find_element(*self.cart_icon).click()
