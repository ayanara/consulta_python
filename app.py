import openpyxl

# 1 - Entrar na planilha e extrair o cpf 
planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_cliente = planilha_clientes['Sheet1']

for linha in pagina_cliente.iter_rows(min_row=2, values_only=True):
    nome, valor, cpf , vencimento = linha

   