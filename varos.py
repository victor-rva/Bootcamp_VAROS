import pandas as pd #principal pacote para análise de dados
import datetime #pacote que lida com datas 
import yfinance as yf #pacote para baixar as cotações de graça da yahoo finance
from matplotlib import pyplot as plt #pacote de gráficos do python
import mplcyberpunk #estilo de gráfico
import smtplib #biblioteca para gerenciar mensagens de e-mail
from email.message import EmailMessage #conseguir enviar o e-mail

ativos = ["^BVSP", "BRL=X"] #dados buscados no yahoo finance

hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days = 365)