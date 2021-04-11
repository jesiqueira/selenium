from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request
import json
from selenium.webdriver import Chrome
chrome = Chrome()
url = 'https://statusinvest.com.br/'
chrome.get(url)

entrar = chrome.find_element_by_class_name('container').find_element_by_class_name('links').find_element_by_class_name('mr-0').find_element_by_class_name('login-view').find_element_by_class_name('d-md-block')
print(entrar)
sleep(2)
entrar.click()
sleep(1)
email = chrome.find_element_by_name('Email')
email.send_keys('edmar.investing@gmail.com')
sleep(1)
password = chrome.find_element_by_name('Password')
password.send_keys('#planet15#')
logar = chrome.find_element_by_id('btn-login')
logar.click()



