def lgeral(cod, nome, margem, preco):
    import pandas as pd

    df = pd.read_csv("Geral BD.csv")
    df = df.drop(df.columns[[0]], axis = 1)

    tamdf = len(df)


    for c in range(0, tamdf-1):
        exist = 'n'
        if cod == df.loc[c][0]:
            exist = 's'
        else:
            df.loc[tamdf] = [cod, nome, margem, preco ]

    print(df)

lgeral('f2610211', 'Docile',  '50', '4.99')

