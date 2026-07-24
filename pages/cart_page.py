from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME,"cart_item")

    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text