from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.driver_setup import get_driver

def test_reset_app():

    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # Add first product
    driver.find_element(By.XPATH, "(//button[contains(text(),'Add to cart')])[1]").click()

    # Open menu
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))).click() 
    WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))) 

    # Verify cart badge is removed
    badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badge) == 0

    driver.quit()