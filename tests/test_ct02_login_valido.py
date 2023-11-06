import time
import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_ct02_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
        time.sleep(1)
