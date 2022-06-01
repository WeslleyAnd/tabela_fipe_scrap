from importlib.resources import path
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from csv import DictWriter
from periodo import lista_meses
from paths import *

driver = webdriver.Chrome()
driver.get("https://veiculos.fipe.org.br/")
driver.maximize_window()
sleep(1)

# ========== CONSULTANDO ================== #
a = 0
while True:
  meses = lista_meses
  for mes in meses:
    if a > 0:
      #element_consulta = driver.find_element_by_css_selector(element_consulta_path).click()
      click_test = driver.find_element(By.CSS_SELECTOR, value=element_consulta_path_other2).click()
      element_consulta = driver.find_element(By.CSS_SELECTOR, value=element_consulta_path_other).click()
    else:
      #element_consulta = driver.find_element_by_css_selector(element_consulta_path).click()
      element_consulta = driver.find_element(By.CSS_SELECTOR, value=element_consulta_path).click()
    sleep(1)
    print('CONSULTA - OK')

    if a > 0:
      #date_element = driver.find_element_by_css_selector(date_element_path).click()
      click_test = driver.find_element(By.CSS_SELECTOR, value=element_consulta_path_other2).click()
      date_element = driver.find_element(By.CSS_SELECTOR, value=date_element_path_other).click()
      sleep(1)
      #date_element_inp = driver.find_element_by_css_selector(date_element_inp_path)
      date_element_inp = driver.find_element(By.CSS_SELECTOR, value=date_element_inp_path_other)
      sleep(1)
      date_element_inp.send_keys(mes, Keys.ENTER)
      sleep(1)
    else:
      #date_element = driver.find_element_by_css_selector(date_element_path).click()
      date_element = driver.find_element(By.CSS_SELECTOR, value=date_element_path).click()
      sleep(1)
      #date_element_inp = driver.find_element_by_css_selector(date_element_inp_path)
      date_element_inp = driver.find_element(By.CSS_SELECTOR, value=date_element_inp_path)
      sleep(1)
      date_element_inp.send_keys(mes, Keys.ENTER)
      sleep(1)
    print('DATA - OK')
    
    if a > 0:
        #marca_element = driver.find_element_by_css_selector(marca_element_path).click()
      marca_element = driver.find_element(By.CSS_SELECTOR, value=marca_element_path_other).click()
      sleep(1)
      #marca_element_inp = driver.find_element_by_css_selector(marca_element_inp_path)
      marca_element_inp = driver.find_element(By.CSS_SELECTOR, value=marca_element_inp_path_other)
      marca_element_inp.send_keys('Fiat', Keys.ENTER)
      sleep(1)
    else:
      #marca_element = driver.find_element_by_css_selector(marca_element_path).click()
      marca_element = driver.find_element(By.CSS_SELECTOR, value=marca_element_path).click()
      sleep(1)
      #marca_element_inp = driver.find_element_by_css_selector(marca_element_inp_path)
      marca_element_inp = driver.find_element(By.CSS_SELECTOR, value=marca_element_inp_path)
      marca_element_inp.send_keys('Fiat', Keys.ENTER)
      sleep(1)
    print('MARCA - OK')

    if a > 0:
      #modelo_element = driver.find_element_by_css_selector(modelo_element_path).click()
      modelo_element = driver.find_element(By.CSS_SELECTOR, value=modelo_element_path_other).click()
      sleep(1)
      #modelo_element_inp = driver.find_element_by_css_selector(modelo_element_inp_path)
      modelo_element_inp = driver.find_element(By.CSS_SELECTOR, value=modelo_element_inp_path_other)
      modelo_element_inp.send_keys('ARGO DRIVE 1.3 8V Flex', Keys.ENTER)
      sleep(1)
    else:
      #modelo_element = driver.find_element_by_css_selector(modelo_element_path).click()
      modelo_element = driver.find_element(By.CSS_SELECTOR, value=modelo_element_path).click()
      sleep(1)
      #modelo_element_inp = driver.find_element_by_css_selector(modelo_element_inp_path)
      modelo_element_inp = driver.find_element(By.CSS_SELECTOR, value=modelo_element_inp_path)
      modelo_element_inp.send_keys('ARGO DRIVE 1.3 8V Flex', Keys.ENTER)
      sleep(1)
    print('MODELO - OK')

    #ano_element = driver.find_element_by_css_selector(ano_element_path).click()
    ano_element = driver.find_element(By.CSS_SELECTOR, value=ano_element_path).click()
    sleep(1)
    #ano_element_inp = driver.find_element_by_css_selector(ano_element_inp_path)
    ano_element_inp = driver.find_element(By.CSS_SELECTOR, value=ano_element_inp_path)
    ano_element_inp.send_keys('2018 Gasolina', Keys.ENTER)
    sleep(1)
    print('ANO - OK')

    #pesquisar_element = driver.find_element_by_css_selector(pesquisar_element_path).click()
    pesquisar_element = driver.find_element(By.CSS_SELECTOR, value=pesquisar_element_path).click()
    sleep(2)
    print('PESQUISAR - OK')

    #data = driver.find_element_by_css_selector("#resultadoConsultacarroFiltros > table > tbody").text
    data = driver.find_element(By.CSS_SELECTOR, value=data_path).text
    print(data)
    print('\n')
    data = data.split('\n')
    print('\n')
    print(data)
    print('\n')
    data = [[data[x], data[x+1]] for x in range(0, len(data), 2)]
    print(data)

    dict_veiculo = {"marca": data[2][1], "modelo": data[3][1], "ano_modelo": data[4][1], "preco": data[7][1], "mes_referencia": mes, "data_consulta": data[6][1] }
    columns = list(dict_veiculo.keys())
    entry = dict_veiculo
    with open('teste.csv', 'a') as f:
      w = DictWriter(f, fieldnames=columns)
      w.writerow(entry)
    a = a + 1

    print('ATUALIZA CSV - OK')
    print(' ')
    print(f"Mês de {mes} concluído!")
