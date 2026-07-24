from pages.login_page import LoginPage
from utils.driver_setup import get_driver 
from selenium.webdriver.common.by import By 

def test_cart_icon():
    driver = get_driver()

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login() 

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    assert cart.is_displayed() 
    driver.quit() 