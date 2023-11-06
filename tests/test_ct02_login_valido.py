import time
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
        time.sleep(2)