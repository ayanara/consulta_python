import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# 1 - Entrar na planilha e extrair o cpf 
planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_cliente = planilha_clientes['Sheet1']

for linha in pagina_cliente.iter_rows(min_row=2, values_only=True):
    nome, valor, cpf , vencimento = linha
    # 2 - Entrar no site e usar o cpf para pesquisar o status do cliente\
    driver = webdriver.Chrome()
    driver.get('https://consultcpf-devaprender.netlify.app/')
    sleep(5)
    campo_pesquisa = driver.find_element(By.XPATH, "//input[@id='cpfInput']")
    sleep(1)
    campo_pesquisa.send_keys(cpf)
    sleep(1)
    # 3 - Verificar se está em dia ou atrasado
    botao_pesquisa = driver.find_element(By.XPATH, "//button[@class='btn btn-custom']")
    sleep(1)
    botao_pesquisa.click()
    sleep(4)
