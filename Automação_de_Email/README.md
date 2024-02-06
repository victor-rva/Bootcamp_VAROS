# Relatório Diário de Análise de Mercado

## Visão Geral
Este script Python foi desenvolvido para analisar dados financeiros, mais especificamente cotações do Ibovespa e do Dólar, utilizando o pacote `yfinance` para baixar informações da Yahoo Finance. Além disso, o script gera gráficos de desempenho e envia um relatório diário por e-mail.

## Requisitos
Certifique-se de ter os seguintes pacotes instalados antes de executar o script:
- pandas
- yfinance
- matplotlib
- mplcyberpunk
- smtplib
- python-dotenv

Você pode instalar esses pacotes usando o seguinte comando:
```bash
pip install pandas yfinance matplotlib mplcyberpunk smtplib python-dotenv
```

## Configuração
1. Antes de executar o script, é necessário configurar um arquivo `.env` na mesma pasta do script com as seguintes informações:
    ```
    senha=senha_criptografada
    ```

    Você pode gerar uma senha criptografada [aqui](https://myaccount.google.com/apppasswords).

2. Substitua `"seu_email@gmail.com"` pelo seu endereço de e-mail tanto no script quanto no arquivo `.env`.

## Execução
Execute o script Python para obter os dados do Yahoo Finance, manipular as informações, gerar gráficos e enviar um relatório diário por e-mail.

```bash
python seu_script.py
```

## Gráficos
O script gera dois gráficos de desempenho para o Ibovespa e o Dólar, salvando-os como `ibovespa.png` e `dolar.png` respectivamente.

## Relatório por E-mail
O script também envia um e-mail com um relatório diário contendo informações sobre o desempenho do Ibovespa e do Dólar no último dia, no último mês e no último ano.

## Observações
- Certifique-se de ter uma conexão com a internet ao executar o script para baixar dados do Yahoo Finance.
- Este script é específico para dados financeiros do mercado brasileiro.

**Disclaimer:** Este script é apenas uma ferramenta de análise e não oferece garantias quanto à precisão ou adequação das informações fornecidas. O uso do script é de responsabilidade do usuário.
