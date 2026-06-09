from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestOficial:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 60)
        self.base = "http://localhost/sistema/public/"

    def teardown_method(self):
        self.driver.quit()

    # Test 1
    def test_precio_producto(self):
        self.driver.get(self.base + "catalogo.php")
        time.sleep(2)
        actual = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Pollo a la canasta']/following-sibling::div[@class='precio']")))
        actual = actual.text
        esperado = "Bs 23.00"
        print(f"++++ ACTUAL CAPTURADO: {actual}")
        assert actual == esperado, f"Error: se esperaba '{esperado}' pero se obtuvo '{actual}'"

    # Test 2
    def test_carrito_sin_login(self):
        self.driver.get(self.base + "catalogo.php")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Pollo a la canasta']/following-sibling::button[@class='btn']"))).click()
        actual = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alerta-login']")))
        actual = actual.text
        esperado = "Debes iniciar sesión para agregar productos."
        print(f"++++ ACTUAL CAPTURADO: {actual}")
        assert actual == esperado, f"Error: se esperaba '{esperado}' pero se obtuvo '{actual}'"

    # Test 3
    def test_agregar_al_carrito(self):
        self.driver.get(self.base + "login.php")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Ingresa tu correo']"))).send_keys("cliente@example.com")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Ingresa tu contraseña']"))).send_keys("12345678")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnLogin']"))).click()
        time.sleep(2)
        self.driver.get(self.base + "catalogo.php")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Milanesa']/following-sibling::button[@class='btn']"))).click()
        time.sleep(2)
        self.driver.get(self.base + "views/client/carritoCliente.html")
        time.sleep(2)
        actual = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Milanesa']")))
        actual = actual.text
        esperado = "Milanesa"
        print(f"++++ ACTUAL CAPTURADO: {actual}")
        assert actual == esperado, f"Error: se esperaba '{esperado}' pero se obtuvo '{actual}'"

    # Test 4
    def test_precio_catalogo_vs_carrito(self):
        self.driver.get(self.base + "login.php")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Ingresa tu correo']"))).send_keys("cliente@example.com")
        self.wait.until(EC.element_to_be_clickable( (By.XPATH, "//input[@placeholder='Ingresa tu contraseña']"))).send_keys("12345678")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnLogin']"))).click()
        time.sleep(2)
        self.driver.get(self.base + "catalogo.php")
        time.sleep(2)
        precio_catalogo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Milanesa']/following-sibling::div[@class='precio']")))
        precio_catalogo = precio_catalogo.text
        print(f"++++ ACTUAL CAPTURADO: {precio_catalogo}")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Milanesa']/following-sibling::button[@class='btn']"))).click()
        time.sleep(2)
        self.driver.get(self.base + "views/client/carritoCliente.html")
        time.sleep(2)
        precio_carrito = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Milanesa']/following-sibling::p[1]")))
        precio_carrito = precio_carrito.text
        print(f"++++ ACTUAL CAPTURADO: {precio_carrito}")
        esperado = precio_catalogo
        assert precio_catalogo in precio_carrito, f"Error: se esperaba '{esperado}' pero se obtuvo '{precio_carrito}'"

    # Test 5
    def test_producto_en_lista_admin(self):
        self.driver.get(self.base + "login.php")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Ingresa tu correo']"))).send_keys("admin@example.com")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Ingresa tu contraseña']"))).send_keys("12345678")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnLogin']"))).click()
        time.sleep(2)
        self.driver.get(self.base + "views/admin/productosAdmin.html")
        time.sleep(2)
        actual = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Pollo a la canasta']/following-sibling::td[1]")))
        actual = actual.text
        esperado = "Bs 23.00"
        print(f"++++ ACTUAL CAPTURADO: {actual}")
        assert actual == esperado, f"Error: se esperaba '{esperado}' pero se obtuvo '{actual}'"