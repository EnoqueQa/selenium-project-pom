import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage 


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def testct02_login_valid(self):
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.login("standard_user","secret_sauce")
        home_page.verify_element_with_success()
