from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def add_first_product(self):
        self.driver.find_element(By.XPATH,"(//button[contains(text(),'Add to cart')])[1]" ).click()

    def add_first_four_products(self):
        buttons = self.driver.find_elements( By.XPATH, "//button[contains(text(),'Add to cart')]")

        for button in buttons[:4]:
            button.click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    def sort_low_to_high(self):
        Select(
            self.driver.find_element(By.CLASS_NAME,"product_sort_container")).select_by_visible_text("Price (low to high)") 