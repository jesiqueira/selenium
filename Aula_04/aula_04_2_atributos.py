from selenium.webdriver import Chrome

def find_by_text(browser, tag, text):
    """
    - browser = instacia do browser 
    - texto = conteudo que deve estar na tag
    - tag = tag onde o texto será procurado

    """
    elementos = browser.find_elements_by_tag_name(tag) #lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """
    - Encontrar o Elemento 'a' com o link `link`

    """
    elementos = browser.find_elements_by_tag_name('a') 

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento



browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

elemento_ddg = find_by_text(browser, 'li', 'Item 1')
print(elemento_ddg.text)

elemento_tag = find_by_href(browser, 'google')
print(elemento_tag.get_attribute('href'))
print(elemento_tag.text)

browser.quit()