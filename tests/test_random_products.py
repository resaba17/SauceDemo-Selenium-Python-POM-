import random 
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage 
from utils.driver_setup import get_driver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
def test_random_products():
    driver = get_driver() 
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver) 
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    selected_products = random.sample(products, 4)

    for product in selected_products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text 
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f"{name} - {price}")
    driver.quit() 