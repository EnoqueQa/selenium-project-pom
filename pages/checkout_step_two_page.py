import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutStepTwoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.button_finish_checkout = (By.ID, "finish")
        
    def click_finish_checkout(self):
        self.click(self.button_finish_checkout)