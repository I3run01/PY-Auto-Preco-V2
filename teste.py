import pandas as pd
import InLondrisoft as il


df = pd.read_csv('Arcom BD.csv')

lcodigos = []
lprecos = []

for c in range(16,len(df)):
    lcodigos.append(df.iloc[c][2])
    preco = str(df.iloc[c][6])
    preco = preco.replace('.',',')
    lprecos.append(preco)


#il.apreco(lcodigos, lprecos)

il.ietiqueta(lcodigos)


