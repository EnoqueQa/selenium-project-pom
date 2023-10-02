import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage 


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def testct02_login_valid(self):
        driver = conftest.driver
        login_page = LoginPage()
        
        login_page.login("standard_user","secret_sauce")

        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
