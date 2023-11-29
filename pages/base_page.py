import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator): 
        return self.driver.find_element(*locator)   
    
    def encontrar_elementos(self, locator): 
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def  pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text
    
    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(*locator))
    
    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f"elemento '{locator}' não existe, mas é esperado que exista."

    def verificar_elemento_não_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f"elemento '{locator}' existe, mas é esperado que não exista."

    def  cliclar_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    def  cliclar_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()  

    def  pressionar_tecla(self, locator, key):
        elem = self.encontrar_elemento(locator)
        if key == "ENTER":
            elem.send_keys(Keys.ENTER)  
        elif key == "ESPAÇO":
            elem.send_keys(Keys.SPACE)    
        elif key == "f1":
            elem.send_keys(Keys.F1)           

