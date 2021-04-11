from selenium.webdriver import Chrome
from parsel import Selector
from pprint import pprint

from time import sleep

browser = Chrome()

url = 'https://rennerocha.github.io/xpath/'

browser.get(url)

html = browser.page_source
sleep(1)

response = Selector(text = html)
# print(response.get())
# print(response.xpath("/html").get())
#  pprint(response.xpath("/html/head").get())
# pprint(response.xpath("/html/head/title").get())
# pprint(response.xpath("//title").get())

# pprint(response.xpath("//h1").getall())


# pprint(response.xpath("//ul").getall())

# Buscar qual conteudo que está dentro da tag ul
# pprint(response.xpath("//ul/*").getall())

# Mostra todo conteúdo que está abaixo da tag ul
#  pprint(response.xpath("//ul//*").getall())

# pprint(response.xpath("//ol").getall())
# pprint(response.xpath("//ol/li").getall())

#Pegar o primeiro ol e o segundo li
# pprint(response.xpath("//ol[1]/li[2]").getall())

# pprint(response.xpath("(//ol/li)").getall())
#  pprint(response.xpath("(//ol/li)[2]").getall())

# pprint(response.xpath("//h1").getall())
# Pegar o texto que está abaixo de H1
# pprint(response.xpath("//h1/text()").getall())
# Pegar todos os texto dentro de H1
# pprint(response.xpath("//h1//text()").getall())

# pprint(response.xpath("//ul[2]/li[3]").getall())
# pprint(response.xpath("//ul[2]/li[3]").getall())
# pprint(response.xpath("//ul[2]/li[3]//text()").getall())
#  pprint(response.xpath("//ul[2]/li[3]/span//text()").getall())

# pprint(response.xpath("//h1/@data-section").getall())
#  pprint(response.xpath("//h1[@data-section]").getall())

#  pprint(response.xpath("//tr").getall())
# pprint(response.xpath("//tr[th]").getall())

# pprint(response.xpath("//li[contains(text(), 'forno')]").getall())

# pprint(response.xpath("//span[@data-qtde > 1]").getall())

#  pprint(response.xpath("//h1[@data-section = 'ingredients' ]").getall())
# pprint(response.xpath("//h1[@data-section = 'ingredients' ]/parent::div//li").getall())

# pprint(response.xpath("//h1[@data-section = 'ingredients' ]/following-sibling::ul").getall())
# pprint(response.xpath("//h1[@data-section = 'ingredients' ]/following-sibling::ul/li").getall())

# pprint(response.xpath("//h2[contains( text(), 'Pudim')]/following-sibling::ul").getall()
#  pprint(response.xpath("//h2[contains( text(), 'Pudim')]/following-sibling::ul/li").getall())

