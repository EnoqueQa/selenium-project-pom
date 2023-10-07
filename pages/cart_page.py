import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.button_continue_shopping = (By.ID, "continue-shopping")
        self.button_checkout = (By.ID, "checkout")
        
    def verify_product_cart_existing(self, name_item):
        item = (self.inventory_item[0], self.inventory_item[1].format(name_item))
        self.verify_existing_element(item)
    
    def click_continue_shopping(self):
        self.click(self.button_continue_shopping)
        
    def click_button_checkout(self):
        self.click(self.button_checkout)