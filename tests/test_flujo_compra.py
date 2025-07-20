import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

def test_flujo_completo(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    productos = ProductsPage(driver)
    productos.agregar_producto_al_carrito()
    productos.ir_al_carrito()

    checkout = CheckoutPage(driver)
    checkout.proceder_a_checkout()
    checkout.ingresar_datos_cliente("Fernando", "QA", "1234")
    checkout.finalizar_compra()

    mensaje = checkout.obtener_mensaje_exito()
    assert mensaje == "Thank you for your order!", "La compra no fue completada correctamente"
