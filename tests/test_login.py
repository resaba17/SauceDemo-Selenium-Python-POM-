from utils.driver_setup import get_driver 
from pages.login_page import LoginPage 

def test_valid_login():
    driver = get_driver()

    login = LoginPage(driver) 
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url.lower() 
    driver.quit() 