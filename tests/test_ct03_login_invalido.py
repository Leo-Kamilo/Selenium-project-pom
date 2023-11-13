import pytest
from pages.login_page import LoginPage



@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()


        #Faz login
        login_page.fazer_login("standard_user", "senha_incorreta")

         # Verifica se o login não foi realizado
        login_page.verificar_mensagem_erro_login()
       