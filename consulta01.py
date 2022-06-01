from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

element_consulta_path = '#front > div.content > div.tab.vertical.tab-veiculos > ul > li:nth-child(1)'
date_element_path = '#selectTabelaReferenciacarro_chosen > a > span'
date_element_inp_path = '#selectTabelaReferenciacarro_chosen > div > div > input[type=text]'
marca_element_path = '#selectMarcacarro_chosen > a > span'
marca_element_inp_path = '#selectMarcacarro_chosen > div > div > input[type=text]'
modelo_element_path = '#selectAnoModelocarro_chosen > a > span'
modelo_element_inp_path = '#selectAnoModelocarro_chosen > div > div > input[type=text]'
ano_element_path = '#selectAnocarro_chosen > a > span'
ano_element_inp_path = '#selectAnocarro_chosen > div > div > input[type=text]'
pesquisar_element_path = '#buttonPesquisarcarro'


driver = webdriver.Chrome()
driver.get("https://veiculos.fipe.org.br/")

element_consulta = driver.find_element_by_css_selector(element_consulta_path).click()
sleep(2)

date_element = driver.find_element_by_css_selector(date_element_path).click()
sleep(2)
date_element_inp = driver.find_element_by_css_selector(date_element_inp_path)
date_element_inp.send_keys('fevereiro/2022', Keys.ENTER)
sleep(2)

marca_element = driver.find_element_by_css_selector(marca_element_path).click()
sleep(2)
marca_element_inp = driver.find_element_by_css_selector(marca_element_inp_path)
marca_element_inp.send_keys('Fiat', Keys.ENTER)
sleep(2)

modelo_element = driver.find_element_by_css_selector(modelo_element_path).click()
sleep(2)
modelo_element_inp = driver.find_element_by_css_selector(modelo_element_inp_path)
modelo_element_inp.send_keys('ARGO DRIVE 1.3 8V Flex', Keys.ENTER)
sleep(2)

ano_element = driver.find_element_by_css_selector(ano_element_path).click()
sleep(2)
ano_element_inp = driver.find_element_by_css_selector(ano_element_inp_path)
ano_element_inp.send_keys('2018 Gasolina', Keys.ENTER)
sleep(2)

pesquisar_element = driver.find_element_by_css_selector(pesquisar_element_path).click()
sleep(5)

page_content = driver.page_source
site = BeautifulSoup(page_content, 'html.parser')
print(site.prettify())