from selenium.webdriver.common.by import By

class LogoutPage:
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver 
    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()
    def logout(self):
        self.driver.find_element(*self.logout_button).click()
        