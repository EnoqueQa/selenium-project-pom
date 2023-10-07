import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutCompletePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.checkout_complete = (By.XPATH, "//*[@class='complete-header']")
        
    def verify_checkout_with_success(self):
        self.verify_existing_element(self.checkout_complete)
        
    def verify_text_message_finish_order(self, text_expected):
        assert self.get_text_element(self.checkout_complete) == text_expected