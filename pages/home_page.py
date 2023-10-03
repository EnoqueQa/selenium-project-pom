import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        
    def verify_element_with_success(self):
        self.verify_existing_element(self.titulo_pagina)
        