from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')


def find_by_text(browser, tag, text):
    """
    - browser = instacia do browser 
    - texto = conteudo que deve estar na tag
    - tag = tag onde o texto será procurado

    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


nome_das_caixas = ['um', 'dois', 'tres', 'quatro']
for nome in nome_das_caixas:
    find_by_text(browser, 'div', nome).click()

for nome in nome_das_caixas:
    sleep(0.3)
    browser.back()

for nome in nome_das_caixas:
    sleep(0.3)
    browser.forward()
# browser.quit()
