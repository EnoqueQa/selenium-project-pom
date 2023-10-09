import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def write(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    def click(self, locator):
        self.find_element(locator).click()
        
    def verify_existing_element(self, locator):
        assert self.find_element(locator).is_displayed(), f"The element {'locator'} was not displayed"
        
    def get_text_element(self, locator):
        return self.find_element(locator).text
    
    def wait_element_appear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verify_element_exists(self, locator):
        assert self.find_element(locator)
        
    def verify_element_dont_exists(self, locator):
        assert len(self.find_elements(locator)) == 0
        
    def double_click(self, locator):
        element = self.wait_element_appear(locator)
        ActionChains(self.driver).double_click(element).perform()
        
    def right_click(self, locator):
        element = self.wait_element_appear(locator)
        ActionChains(self.driver).context_click(element).perform()
        
    def press_key(self, locator, key):
        element = self.find_element(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            element.send_keys(Keys.SPACE)
        elif key == "COMMAND":
            element.send_keys(Keys.COMMAND)
        
    