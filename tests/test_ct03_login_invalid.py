import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def testct03_login_invalid(self):
        login_page = LoginPage()
        
        login_page.login("standard_user","secret_sauc")
        login_page.verify_message_error_login()
