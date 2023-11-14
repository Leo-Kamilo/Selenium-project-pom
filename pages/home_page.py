from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
       self.driver = conftest.driver
       self.titulo_pagina = (By.XPATH, "//span[@class='title']")
       self.item_iventario = (By.XPATH,'//*[@class="inventory_item_name " and text()="{}"]')
       self.adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")   

       
        

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_iventario[0], self.item_iventario[1].format(nome_item))  
        self.clicar(item)   
        self.clicar(self.adicionar_carrinho)