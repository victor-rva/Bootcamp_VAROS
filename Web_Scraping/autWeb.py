from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

#Web Scraping = um "robô" para pegar dados em site
#Pegando dados de ETFs do mundo inteiro.
# Nesse caso o navegador utilizado será o Google Chrome
#Importar os módulos e bibliotecas.

#Requisições na internet.
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
#driver.get('https://www.google.com/')
driver.get('https://etf.com/etfanalytics/etf-screener')

#Achar todos os elementos necessários dentro do HTML do site.
time.sleep(5) #devido a demora para carregar o javascript do site é recomendado dar um delay para o python ler a linha de achar o botão.

botao_100 = driver.find_element("xpath", '/html/body/div[2]/div/div[1]/main/div/section/div[2]/div[2]/div[3]/div/article/div/div[3]/div/div[1]/div/div/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[5]/button/span')
botao_100.click()

#caso bugue e o .click() não funcione, usar a seguinte linha de código:
#driver.execute_script("arguments[0].click();", botao_100)

#Ler a tabela de dados.

#Constuir a tabela final.