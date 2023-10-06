import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_mensage_login = (By.XPATH, "//*[@data-test='error']")
        
    def login(self, users, password):
        self.write(self.username_field, users)
        self.write(self.password_field, password)
        self.click(self.login_button)
        
    def verify_message_error_login(self):
        self.find_element(self.error_mensage_login)
