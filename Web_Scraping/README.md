# ETF Web Scraping

## Descrição
Este script em Python utiliza a biblioteca Selenium para realizar web scraping e coletar dados de Exchange-Traded Funds (ETFs) de todo o mundo a partir do site [ETF.com](https://etf.com/etfanalytics/etf-screener). Os dados coletados incluem informações cadastrais e de performance dos ETFs.

## Requisitos
- Python 3.x
- Bibliotecas:
  - selenium
  - webdriver_manager
  - pandas

## Instalação
Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:
```bash
pip install selenium webdriver_manager pandas
```

## Uso
1. Certifique-se de ter todas as bibliotecas instaladas.
2. Execute o script `etf_web_scraping.py`.

## Funcionalidades
- Abre o navegador Google Chrome automaticamente.
- Acessa a página de análise de ETFs no site [ETF.com](https://etf.com/etfanalytics/etf-screener).
- Clica no botão "Mostrar 100 entradas" para exibir mais ETFs por página.
- Extrai o número total de páginas disponíveis.
- Realiza o scraping das tabelas de dados cadastrais e de performance de cada ETF em todas as páginas.
- Constrói uma tabela final unindo as informações cadastrais e de performance usando o ticker como índice.
- Exibe a tabela final no console.

## Observações
- O script possui alguns comentários importantes que fornecem explicações sobre certas linhas de código.
- Um delay de 30 segundos é adicionado para garantir que a página seja completamente carregada antes de interagir com os elementos.
- Em caso de problemas com o clique do botão, há uma alternativa comentada usando `driver.execute_script`.
- Após a conclusão da execução, o navegador é fechado automaticamente.

**Nota:** Este script realiza scraping de dados de um site específico. Certifique-se de estar em conformidade com os termos de serviço do site antes de utilizar ou modificar o script para atender às suas necessidades.
