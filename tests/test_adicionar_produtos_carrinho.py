import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5) 
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@class="inventory_item_name " and text()="Sauce Labs Backpack"]').click
time.sleep(2)
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
time.sleep(2)

assert driver.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed