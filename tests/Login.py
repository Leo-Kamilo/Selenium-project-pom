import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5) 
driver.maximize_window()
driver.get('https://autovist.com.br/login/')

driver.find_element(By.ID, "id_email").send_keys("leonardo@autovist.com.br")
driver.find_element(By.ID, "id_senha").send_keys("@3835204Ls")
time.sleep(3)
driver.find_element(By.ID, "logar").click()
time.sleep(20)
