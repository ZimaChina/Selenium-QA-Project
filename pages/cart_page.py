from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_nombre = (By.CLASS_NAME, "inventory_item_name")

    def obtener_nombre_producto(self):
        return self.driver.find_element(*self.item_nombre).text
