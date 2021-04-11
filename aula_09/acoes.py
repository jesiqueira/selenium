from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait


def esperar_page(webdriver):

    elements = webdriver.find_element_by_id('conteudo-principal')

    print('Tentando encontrar  "conteudo-principal"')
    return bool(elements)


url = "http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/acoes/consultas/classificacao-setorial/"

driver = Chrome()

wdw = WebDriverWait(driver, 10)


driver.get(url)

wdw.until(esperar_page)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())
