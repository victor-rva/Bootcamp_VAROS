from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

#Web Scraping = um "robô" para pegar dados em site
#Pegando dados de ETFs do mundo inteiro.
#Nesse caso o navegador utilizado será o Google Chrome
#Importar os módulos e bibliotecas.

#Requisições na internet.
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
#driver.get('https://www.google.com/')
driver.get('https://etf.com/etfanalytics/etf-screener')


#Achar todos os elementos necessários dentro do HTML do site.
time.sleep(30) #devido a demora para carregar o javascript do site é recomendado dar um delay para o python ler a linha de achar o botão.
botao_100 = driver.find_element("xpath", '/html/body/div[2]/div/div[1]/main/div/section/div[2]/div[2]/div[3]/div/article/div/div[3]/div/div[1]/div/div/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[5]/button/span')
botao_100.click()
#caso bugue e o .click() não funcione, usar a seguinte linha de código:
#driver.execute_script("arguments[0].click();", botao_100)
numero_paginas =  driver.find_element("xpath", '//*[@id="panel:r0:0"]/div/div[2]/div[2]/ul/li[8]/a')
numero_paginas.text
numero_paginas = int(numero_paginas)

#Ler a tabela de dados.
lista_tabela_por_pagina = []
elemento = driver.find_element("xpath", '//*[@id="screener-output-table"]')  

for pagina in range(1, numero_paginas + 1):
    html_tabela = elemento.get_attribute('outerHTML')
    tabela = pd.read_html(str(html_tabela))[0]
    lista_tabela_por_pagina.append(tabela)
    botao_avancar_pagina = driver.find_element("xpath", '//*[@id="panel:r0:0"]/div/div[2]/div[2]/ul/li[9]/a')
    botao_avancar_pagina.click()
tabela_cadastro_etfs = pd.concat(lista_tabela_por_pagina) #vai servir para cocatenar as tabelas

#Voltando para primeira página da tabela
voltar_para_primeira_pagina = driver.find_element("xpath", '//*[@id="panel:r0:0"]/div/div[2]/div[2]/ul/li[2]/a')
voltar_para_primeira_pagina.click()


#Ler tabela de performance dos etfs
botao_mudar_pra_perfomance = driver.find_element("xpath", '/html/body/div[2]/div/div[1]/main/div/section/div[2]/div[2]/div[3]/div/article/div/div[3]/div/div[1]/div/div/div/div[3]/div[2]/div/ul/li[2]')  
botao_mudar_pra_perfomance.click()

lista_tabela_por_pagina = []
elemento = driver.find_element("xpath", '//*[@id="screener-output-table"]')  

for pagina in range(1, numero_paginas + 1):
    html_tabela = elemento.get_attribute('outerHTML')
    tabela = pd.read_html(str(html_tabela))[0]
    lista_tabela_por_pagina.append(tabela)
    botao_avancar_pagina = driver.find_element("xpath", '//*[@id="panel:r0:0"]/div/div[2]/div[2]/ul/li[9]/a')
    driver.execute_script("arguments[0].click();", botao_avancar_pagina)
    # botao_avancar_pagina.click()
tabela_rentabilidade_etfs = pd.concat(lista_tabela_por_pagina) #vai servir para cocatenar as tabelas

driver.quit()

#Constuir a tabela final.
tabela_rentabilidade_etfs = tabela_rentabilidade_etfs.set_index("Ticker")
tabela_rentabilidade_etfs = tabela_rentabilidade_etfs[['1 Year', '3 Years', '5 Years']]
tabela_cadastro_etfs = tabela_cadastro_etfs.set_index("Ticker")
base_de_dados_final = tabela_cadastro_etfs.join(tabela_rentabilidade_etfs, how = 'inner')
print(base_de_dados_final)