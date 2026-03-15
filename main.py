# Atuomação de preenchimento de formulário baseado em planilha com openpyxl e selenium
# Autor: Peixe_C1vil
# 15/06/2026

from selenium import webdriver
import openpyxl

# Carregando planilha
workbook = openpyxl.load_workbook('clientes_produtos_exemplo.xlsx')
vendas_sheet = workbook['Pedidos']

# Abrindo navegador e entrando no formulário
driver = webdriver.Chrome()
driver.get("https://yoursite.com/formulario")

for linhas in vendas_sheet.iter_rows(min_row=2):

    # Extrair os dados da planilha
    nome_cliente = linhas[0].value
    produto = linhas[1].value
    quantidade = linhas[2].value
    categoria = linhas[3].value

    # Preencher o formulário usando Selenium
    driver.find_element("id","cliente").send_keys(nome_cliente)
    driver.find_element("id","produto").send_keys(produto)
    driver.find_element("id","quantidade").send_keys(str(quantidade))
    driver.find_element("id","categoria").send_keys(categoria)
    driver.find_element("css selector", "button[data-slot='button']").click()