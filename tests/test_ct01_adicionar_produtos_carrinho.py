import time
import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        
        #Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        #Adiciona a mochila no carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")
       

        #Verifica se a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")


         #Volta pra tela de produtos
        carrinho_page.clicar_continuar_comprando()

         #Adiciona a mais um item ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Bolt T-Shirt")

         #Verifica se os 2 itens estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Bolt T-Shirt")