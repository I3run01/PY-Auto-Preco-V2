def comparador(xml, nomecsv):
    #importações
    import xml.etree.ElementTree as ET
    import dadoscad
    import pandas as pd
    import time

    tree = ET.parse(xml)
    root = tree.getroot()

    #Parâmetros importantes
    df = pd.read_csv(nomecsv)
    df = df.drop(df.columns[[0]], axis = 1)
    tam = len(df)
    link = '{http://www.portalfiscal.inf.br/nfe}'

    #Listas
    lcode = []

    lindiceau = []
    lnomeau = []
    lpreconau = []
    lprecoaau = []
    lcodeina = []

    lindicead = []
    lnomed = []
    lprecond =[]
    lprecoad = []
    lcodeind = []

    lindicen = []
    lnomen = []
    lpreconn = []
    lprecoan = []
    lcodeinn = []

    for c in range(0, tam):
        lcode.append(df.iloc[c][0])
    


    for cProd in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}cProd"):
        cProd = f'f{cProd.text}'
        indice = lcode.index(cProd)
        margem = df.iloc[indice][3]
        quantunit = df.iloc[indice][4]
        codigo = df.loc[indice][1]
        nome = dadoscad.nome(cProd,xml)
        precon = dadoscad.preco(cProd,margem,quantunit,xml)
        precoa = df.iloc[indice][5]

        if float(precon) > float(precoa):
            lindiceau.append(indice)
            lpreconau.append(precon)
            lprecoaau.append(precoa)
            lnomeau.append(nome) 
            lcodeina.append(codigo)

        elif float(precon) < float(precoa):
            lindicead.append(indice)
            lprecond.append(precon)
            lprecoad.append(precoa)
            lnomed.append(nome)
            lcodeind.append(codigo)

        else:
            lindicen.append(indice)
            lpreconn.append(precon)
            lprecoan.append(precoa)
            lnomen.append(nome)
            lcodeinn.append(codigo)

    print('''
    0 - Finalizar o SoftWare
    1 - Ver produtos que aumentaram
    2 = Ver produtos que diminuiram
    3 - Ver produtos que não tiveram aumento
    ''')

    op = int(input('Opção: '))
    confirma = input(str('Confirma (S/N)')).strip().upper()[0]
    print(60*'-')


    if op == 1 and confirma == 'S':
        print(f'{"Nome             ":<5}', f'\t\t\t{"Pr. antigo":^5}', f'\t\t{"Pr. atual":>5}')
        for c in range(0, len(lindiceau)):
            print(f'{lnomeau[c][0:17]:<5}...',f'\t\tR${lprecoaau[c]:^5}', f'\t\tR${lpreconau[c]:>5}')




        



