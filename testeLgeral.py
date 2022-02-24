def lgeral(cod, nome, margem, preco):
    import pandas as pd

    df = pd.read_csv("Geral BD.csv")
    df = df.drop(df.columns[[0]], axis = 1)

    tamdf = len(df)

    exist = 'n'
    for c in range(0, tamdf):

        if cod == df.loc[c][0]:
            exist = 's'
        else:
            df.loc[tamdf] = [cod, nome, margem, preco ]

    if exist == 'n':
        df.to_csv('Geral BD.csv')
    return exist




funcao = lgeral('f2610211', 'Docile',  '50', '4.99')
print(funcao)

