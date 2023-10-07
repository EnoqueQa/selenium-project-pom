import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def testct03_login_invalid(self):
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"
        
        login_page = LoginPage()
        
        login_page.login("standard_user","secret_sauc")
        login_page.verify_message_error_login_existing()
        login_page.verify_text_message_error_login(expected_error_message)
