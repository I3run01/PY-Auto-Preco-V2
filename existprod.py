def cadp(xml, nomecsv):

    #Módulos importantes
    import pandas as pd
    import xml.etree.ElementTree as ET
    import time
    import dadoscad as dc
    import InLondrisoft as IS

    tree = ET.parse(xml)
    root = tree.getroot()

    #Listas
    lnprod = []
    lnpreco = []

    #Abreviação do link elemento XML
    link = '{http://www.portalfiscal.inf.br/nfe}'

    #planilha que será aberta
    df = pd.read_csv(nomecsv)
    df = df.drop(df.columns[[0]], axis = 1)



    while True:
        listCad = []
        #Conferência se todos os códigos estão cadastrados
        for cProd in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}cProd"):
            nlin = len(df)
            cProd = f'f{cProd.text}'
            conf = 'NA'
            for cont in range(0, nlin):
                if cProd == df.iloc[cont,0]:
                    conf = 'NE'

            if conf == 'NA':
                
                listCad.append(cProd)

        #Notas sem cadastro:
        taml = len(listCad)
        if taml >= 1:
            for item in listCad:
                print(30*'-')
                print(f'O produto {dc.nome(item, xml)} não tem cadastro!')
                print(30*'-')
            while True:
                print(30*'-')

                print('1 - Para continuar sem cadastrar\n2 - Para cadastrar os itens\n3 - Para ver a lista de produtos')
                print(30*'-')
                time.sleep(1)
                op = input(str('Opção: '))
                print(f'Você escolheu a opção {op}')
                ops = input(str('Confirma: (S/N)')).strip().upper()[0]

                if ops == 'S' and op =='1':
                    break
                if ops == 'S' and op =='2':
                    for c in listCad:
                        print(30*'-')
                        tamp = len(df)
                        print(f'Você está cadastrando o produto {dc.nome(c , xml)}')
                        time.sleep(1)
                        codigo = str(input('Código da empresa local para esse produto:'))
                        codigo = str(f'f{codigo}')
                        margem = str(input('Margem do produto: '))
                        quantunit = str(input('Quantidade fracionada: '))
                        nome = dc.nome(c,xml)
                        preco = dc.preco(c,margem,quantunit,xml)
                        precobr = preco.replace('.',',')
                        df.loc[tamp] = [c,codigo, nome, margem, quantunit, preco]   
                        df.to_csv(nomecsv)
                        print(f'O produto custa R${preco}')
                        print(f'O produto {nome} foi cadastrado!')
                        lnprod.append(codigo)
                        lnpreco.append(precobr)
                        print(30*'-')
                    print(30*'-=')
                    break
                if ops == 'S' and op =='3':
                    print(df)


        else:
            print('Todos os itens estão cadastrados')
            while True:
                print(30*'-')
                print('1 - Para continuar\n2 - Ver a lista de cadastro\n3 - Cadastrar na Londrisoft\n4 - Imprimir os produtos cadastrados na LS')
                print(30*'-')
                time.sleep(1)
                op = str(input('Opção: '))
                opc = str(input('Confirma? S/N')).strip().upper()[0] 

                if op == '1' and opc == 'S':
                    break
                elif op == '2' and opc =='S':
                    print(df)
                elif op =='3' and opc =='S':
                    IS.apreco(lnprod,lnpreco)
                elif op =='4' and opc =='S':
                    IS.ietiqueta(lnprod)

            break
