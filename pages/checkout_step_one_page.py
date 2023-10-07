import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutStepOnePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.field_first_name = (By.ID, "first-name")
        self.field_last_name = (By.ID, "last-name")
        self.field_postal_code = (By.ID, "postal-code")
        self.button_continue_checkout = (By.ID, "continue")
        
    def checkout_step_one(self, first_name, last_name, postal_code):
        self.write(self.field_first_name, first_name)
        self.write(self.field_last_name, last_name)
        self.write(self.field_postal_code, postal_code)
        
    def click_button_continue_checkout(self):
        self.click(self.button_continue_checkout)