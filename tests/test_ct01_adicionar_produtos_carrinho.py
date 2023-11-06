import time
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        #Faz Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        #Adiciona a mochila no carrinho
        driver.find_element(By.XPATH, '//*[@class="inventory_item_name " and text()="Sauce Labs Backpack"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        time.sleep(2)

        #Verifica se a mochila foi adicionada
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed

        #Volta pra tela de produtos
        driver.find_element(By.ID, "continue-shopping").click()

        #Adiciona a mais um item ao carrinho
        driver.find_element(By.XPATH, '//*[@class="inventory_item_name " and text()="Sauce Labs Bike Light"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        time.sleep(2)

        #Verifica se os 2 itens estão no carrinho
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed
        assert driver.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Bike Light"]').is_displayed