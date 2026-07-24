from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.driver_setup import get_driver


def test_complete_checkout():
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
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    # Enter user details
    driver.find_element(By.ID, "first-name").send_keys("Resaba")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("600001")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    driver.find_element(By.ID, "finish").click()

    # Verify success message
    message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert message == "Thank you for your order!"

    driver.quit()