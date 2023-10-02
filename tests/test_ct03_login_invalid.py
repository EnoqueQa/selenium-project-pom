import pytest
import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def testct03_login_invalid(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauc")
        driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//*[@data-test='error']").is_displayed()
