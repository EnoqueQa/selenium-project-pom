import conftest
from selenium.webdriver.common.by import By


class LoginPage:
    
    def __init__(self):
        self.driver = conftest.driver
        
    def login(self, users, password):
        self.driver.find_element(By.ID, "user-name").send_keys(users)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
