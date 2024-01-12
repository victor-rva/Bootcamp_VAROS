import pandas as pd #principal pacote para análise de dados
import datetime #pacote que lida com datas 
import yfinance as yf #pacote para baixar as cotações de graça da yahoo finance
from matplotlib import pyplot as plt #pacote de gráficos do python
import mplcyberpunk #estilo de gráfico
import smtplib #biblioteca para gerenciar mensagens de e-mail
from email.message import EmailMessage #conseguir enviar o e-mail
import os
from dotenv import load_dotenv


#PEGAR DADOS DO YAHOO FINANCE
ativos = ["^BVSP", "BRL=X"] #dados buscados no yahoo finance

hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days = 365)

dados_mercado = yf.download(ativos, um_ano_atras, hoje)
# print(dados_mercado)


#MANIPULANDO OS DADOS - SELEÇÃO E EXCLUSÃO
dados_fechamento = dados_mercado["Adj Close"]

dados_fechamento.columns = ["dolar", "ibovespa"]
# print(dados_fechamento)

dados_fechamento = dados_fechamento.dropna() #dropna() serve para retirar os dados que estão faltando na tabela

dados_fechamento.head(50)


#MANIPULANDO OS DADOS - CRIANDO TABELAS COM OUTROS TIMEFRAMES
dados_fechamento_mensal = dados_fechamento.resample("M").last() 
dados_fechamento_anual = dados_fechamento.resample("Y").last() 
# resample() serve para redimensionar de acordo com o argumento, se for M ser mensal, Y será anual, W semanal.
# Nesse caso last()serve para transformar os dados do mês em um único dado para o fechamento do mês.


#CALCULAR FECHAMENTO DO DIA, RETORNO NO ANO E RETORNO NO MÊS DOS ATIVOS
retorno_no_ano = dados_fechamento_anual.pct_change().dropna() #pct_change() serve para calcular a porcentagem
retorno_no_mes = dados_fechamento_mensal.pct_change().dropna() 
retorno_no_dia = dados_fechamento.pct_change().dropna() 


#LOCALIZAR O FECHAMENTO DO DIA ANTERIOR, RETORNO NO MÊS E RETORNO NO ANO
# loc -> referenciar elementos a partir do nome
# iloc -> selecionar elementos como uma matriz
# print(retorno_no_dia)

# # retorno_no_dia.loc["linha", "coluna"]

# print(retorno_no_dia.loc["2024-01-04", "dolar"])
# print(retorno_no_dia.loc["2024-01-04"])

retorno_no_dia.iloc[0, 0]
retorno_dia_dolar = retorno_no_dia.iloc[-1, 0]
retorno_dia_ibovespa = retorno_no_dia.iloc[-1, 1]

retorno_mes_dolar = retorno_no_mes.iloc[-1, 0]
retorno_mes_ibovespa = retorno_no_mes.iloc[-1, 1]

retorno_ano_dolar = retorno_no_ano.iloc[-1, 0]
retorno_ano_ibovespa = retorno_no_ano.iloc[-1, 1]
    
# para diminuir os números do resultado dos dados
def retorno(x):
    return round(x * 100, 2)

retorno_dia_dolar = retorno(retorno_dia_dolar)
retorno_dia_ibovespa = retorno(retorno_dia_ibovespa)

retorno_mes_dolar = retorno(retorno_mes_dolar)
retorno_mes_ibovespa = retorno(retorno_mes_ibovespa )

retorno_ano_dolar = retorno(retorno_ano_dolar)
retorno_ano_ibovespa = retorno(retorno_ano_ibovespa) 


#FAZER OS GRÁFICOS DA PERFOMACE DO ÚLTIMO DOS ATIVOS
plt.style.use("cyberpunk")

dados_fechamento.plot(y = "ibovespa", use_index= True, legend= False)
#y é o eixo
#use_index é indice x com as datas
#legend é a legenda
plt.title("Ibovespa")
plt.savefig("Ibovespa.png", dpi = 300)
# plt.show()

dados_fechamento.plot(y = "dolar", use_index= True, legend= False)
plt.title("Dolar")
plt.savefig("Dolar.png", dpi = 300)
# plt.show()

#ENVIAR E-MAIL
#acessar o https://myaccount.google.com/apppasswords para gerar uma senha criptografada do seu e-mail, colocar a senha=senha_criptograda no bloco de notas e salvar na mesma pasta com o nome de .env
load_dotenv()

senha = os.environ.get("senha") 
email = "seu_email@gmail.com"

msg = EmailMessage() #cria um objeto de e-mail 
msg["Subject"] = "Envindo e-mail com o python"
msg["From"] = "seu_email@gmail.com"
msg["To"] = "seu_email@gmail.com"

msg.set_content(f''' Prezado diretor, segue o relatório diário:
                
Bolsa:

No ano o Ibovespa está tendo uma rentabilidade de {retorno_ano_ibovespa}%,
enquanto no mês a rentabilidade é de {retorno_mes_ibovespa}%.


Dólar:

No ano o Dólar está tendo um rentabilidade de {retorno_ano_dolar}%,
enquanto no mês a rentabilidade é de {retorno_mes_dolar}%.

Abs,

O melhor estagiário do mundo.
''' 
)

with open("dolar.png", "rb") as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype="application", subtype="png", filename="dolar.png")

with open("ibovespa.png", "rb") as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype="application", subtype="png", filename="ibovespa.png")
    
with smtplib.SMTP_SSL("smtp.gmail.com", "465") as smtp:
    
    smtp.login(email, senha)
    smtp.send_message(msg)