import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.button_add_cart = (By.XPATH, "//*[text()='Add to cart']")
        self.icon_cart = (By.XPATH, "//*[@class='shopping_cart_link']")
        
    def verify_element_with_success(self):
        self.verify_existing_element(self.titulo_pagina)
        
    def add_to_cart(self, name_item):
        item = (self.inventory_item[0], self.inventory_item[1].format(name_item))
        self.click(item)
        self.click(self.button_add_cart)
        
    def access_the_cart(self):
        self.click(self.icon_cart)
        