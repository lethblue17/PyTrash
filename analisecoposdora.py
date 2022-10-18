import pandas as pd
tabela = pd.read_excel('qdecoposdora.xlsx')

tabela.head()
total_de_copos = tabela['QDC'].sum()
peso_por_kg = tabela['QDC' * 'Pesodoscopos']