"""

    1 - Pegar todos os links da Aula
        {'nome da aula':'link da aula'}
    2 - Navegar até Exercicio 3
        Achar a url do exerçicio 3 e ir até lá 
"""

from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04.html')


def get_links(browser, elemento):
    """
        Pega todos os links dentro de um elemento

        - browser = a instância  do navegador
        - element = ['aside', main, body, ul, ol]
    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado

#  Parte 1


sleep(2)

# aside = browser.find_element_by_tag_name('aside')
# aside_ancora = aside.find_elements_by_tag_name('a')

# resultado_1 = {}

# for ancora in aside_ancora:
#     resultado_1[ancora.text] = ancora.get_attribute('href')

aulas = get_links(browser, "aside")
pprint(aulas)

"""
    browser.get(resultado_1['Aula 3'])
    browser.get(resultado_1['Aula 4'])
"""

# Parte 2

exercio3 = get_links(browser, "main")
pprint(exercio3)

browser.get(exercio3['Exercício 3'])
# main = browser.find_element_by_tag_name('main')

# browser.quit()
