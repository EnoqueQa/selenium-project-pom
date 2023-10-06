import conftest


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
    