import pandas as pd

tabela = pd.read_csv('exportacoes_franca.csv') # only exports from Brazil to France

def formatar_dolar(valor):
    return f'${valor:,.2f}'



tabela = tabela.loc[tabela['Economic Block'] == 'Europe']


exportacao_por_ano = tabela.groupby('Year').sum(numeric_only=True)
exportacao_por_ano = exportacao_por_ano[['US$ FOB']]
exportacao_por_ano['US$ FOB'] = exportacao_por_ano['US$ FOB'].map(formatar_dolar)
print(exportacao_por_ano) # how many dollars did Brazil make with these sales per year


exportacao_por_produtos = tabela.groupby('SH4 Description').sum(numeric_only=True)
exportacao_por_produtos = exportacao_por_produtos[['US$ FOB']].sort_values(by='US$ FOB', ascending=False)
exportacao_por_produtos['US$ FOB'] = exportacao_por_produtos['US$ FOB'].map(formatar_dolar)
print(exportacao_por_produtos) # which type of Brazilian product is most exported


cidade_20201 = tabela.loc[tabela['Year'] == 2020]
cidade_2020 = cidade_20201.groupby('City').sum(numeric_only=True)
cidade_2020 = cidade_2020[['US$ FOB']].sort_values('US$ FOB', ascending=False)
cidade_2020['US$ FOB'] = cidade_2020['US$ FOB'].map(formatar_dolar)
print(cidade_2020) # brazilian cities that most profit in 2020


cidade1_index = cidade_2020.index[0]
cidade1 = cidade_20201.loc[cidade_20201['City'] == cidade1_index]
cidade1 = cidade1.groupby('SH4 Description').sum(numeric_only=True)
cidade1 = cidade1[['US$ FOB']].sort_values('US$ FOB', ascending=False)
cidade1['US$ FOB'] = cidade1['US$ FOB'].map(formatar_dolar)
print(f'''{cidade1_index} exportou:
# {cidade1}''') # what the first city that most profit has exported


cidade2_index = cidade_2020.index[1]
cidade2 = cidade_20201.loc[cidade_20201['City'] == cidade2_index]
cidade2 = cidade2.groupby('SH4 Description').sum(numeric_only=True)
cidade2 = cidade2[['US$ FOB']].sort_values('US$ FOB', ascending=False)
cidade2['US$ FOB'] = cidade2['US$ FOB'].map(formatar_dolar)

print(f'''{cidade2_index}, exportou:
{cidade2}''') # what the second city that most profit has exported