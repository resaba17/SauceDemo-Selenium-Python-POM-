from pages.login_page import LoginPage 
from pages.logout_page import LogoutPage 
from utils.driver_setup import get_driver 

def test_logout():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver) 
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login() 

    logout = LogoutPage(driver) 
    logout.open_menu()
    logout.logout() 

    assert "saucedemo.com" in driver.current_url 
    driver.quit() 