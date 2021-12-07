def comparador(xml, nomecsv):
    #importações
    import xml.etree.ElementTree as ET
    import dadoscad
    import pandas as pd
    import time
    import InLondrisoft as IS

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
    lcodeinau = []

    lindiced = []
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
            lpreconau.append(str(precon).replace('.',','))
            lprecoaau.append(precoa)
            lnomeau.append(nome)
            lcodeinau.append(str(codigo))

        elif float(precon) < float(precoa):
            lindiced.append(indice)
            lprecond.append(str(precon).replace('.',','))
            lprecoad.append(precoa)
            lnomed.append(nome)
            lcodeind.append(str(codigo))

        else:
            lindicen.append(indice)
            lpreconn.append(str(precon).replace('.',','))
            lprecoan.append(precoa)
            lnomen.append(nome)
            lcodeinn.append(str(codigo))
    while True:
        print('''
        0 - Finalizar o SoftWare
        1 - Ver produtos que aumentaram
        2 = Ver produtos que diminuiram
        3 - Ver produtos que não tiveram aumento
        4 - Atualizar os preços que aumentaram na LS
        5 - Atualizar os preços que diminuiram na LS
        6 - Imprimir os preços que aumentaram
        7 - Imprimir os preços que diminuiram
        ''')

        op = int(input('Opção: '))
        confirma = input(str('Confirma (S/N)')).strip().upper()[0]
        print(60*'-')

        if op == 1 and confirma == 'S':
            print(f'{"Nome                             ":<5}', f'\t\t\t{"Pr. antigo":^5}', f'\t\t{"Pr. atual":>5}')
            for c in range(0, len(lindiceau)):
                print(f'{lindiceau[c]}-{lnomeau[c][0:10]:<5}........................',f'\t\tR${lprecoaau[c]:^5}', f'\t\tR${lpreconau[c]:>5}')

        elif op == 2 and confirma == 'S':
            print(f'{"Nome                             ":<5}', f'\t\t\t{"Pr. antigo":^5}', f'\t\t{"Pr. atual":>5}')
            for c in range(0, len(lindiced)):
                print(f'{lindiced[c]}-{lnomed[c][0:10]:<5}........................', f'\t\tR${lprecoad[c]:^5}', f'\t\tR${lprecond[c]:>5}')

        elif op == 3 and confirma == 'S':
            print(f'{"Nome                             ":<5}', f'\t\t\t{"Pr. antigo":^5}', f'\t\t{"Pr. atual":>5}')
            for c in range(0, len(lindicen)):
                print(f'{lindicen[c]}-{lnomen[c][0:10]:<5}........................', f'\t\tR${lprecoan[c]:^5}', f'\t\tR${lpreconn[c]:>5}')
        
        elif op == 4 and confirma == 'S':
            IS.apreco(lcodeinau, lpreconau)
            c = 0
            for indice in lindiceau:
                indice = int(indice)
                print(indice)
                preconau2 = lpreconau[c]
                preconau2 = preconau2.replace(',','.')
                print(preconau2)
                df.loc[indice] = [df.iloc[indice][0],df.iloc[indice][1],df.iloc[indice][2],df.iloc[indice][3],df.iloc[indice][4],preconau2]
                df.to_csv(nomecsv)
                c = c+1

        elif op == 5 and confirma == 'S':
            IS.apreco(lcodeind, lprecond)
            c = 0
            for indice in lindiceau:
                indice = int(indice)
                print(indice)
                preconau2 = lpreconau[c]
                preconau2 = preconau2.replace(',','.')
                print(preconau2)
                df.loc[indice] = [df.iloc[indice][0],df.iloc[indice][1],df.iloc[indice][2],df.iloc[indice][3],df.iloc[indice][4],preconau2]
                df.to_csv(nomecsv)
                c = c+1

        elif op == 6 and confirma == 'S':
            IS.ietiqueta(lcodeinau)


        elif op == 7 and confirma == 'S':
            IS.ietiqueta(lcodeind)

        else:
            break






