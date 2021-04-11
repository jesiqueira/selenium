from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import time

chrome = Chrome()

url = 'https://statusinvest.com.br/acoes/busca-avancada'

chrome.get(url)

buscar = chrome.find_element_by_class_name('find')

buscar.click()

time.sleep(2)

# chrome.find_element_by_css_selector('dropdown-content.select-dropdown li::nth-of-type(3)').click()
select = chrome.find_element_by_class_name('select-dropdown').


select.send_keys('TODOS')
