def cnpj(xml):

    import xml.etree.ElementTree as ET

    tree = ET.parse(xml)
    root = tree.getroot()


    link = '{http://www.portalfiscal.inf.br/nfe}'
   

    for cnpj in root.findall(f"./{link}NFe/{link}infNFe/{link}emit/{link}CNPJ"):
       cnpjarq = cnpj.text
       
       return cnpjarq
       
def bibemp(num):
    if num == '62461140002834':
        nome = 'Panco'
        nomecsv ='Panco BD.csv'
        
    elif num =='61186888014305':
        nome ='Coca-Cola'
        nomecsv = 'CC BD.csv'

    elif num =='24782106000152':
        nome ='Tirol'
        nomecsv = 'Tirol BD.csv'

    elif num == '77887412000543':
        nome = 'DEYCON'
        nomecsv = 'Deycon BD.csv'

    elif num == '12133164000176':
        nome = 'RD'
        nomecsv = 'RD BD.csv'

    elif num == '93209765047342':
        nome = 'WMS'
        nomecsv = 'WMS BD.csv'

    elif num == '03303285000128':
        nome = 'Arrojito'
        nomecsv = 'Arrojito BD.csv'

    elif num == '73778144000147':
        nome = 'Triunfante'
        nomecsv = 'Triunfante BD.csv'

    elif num == '01333984000438':
        nome = 'Segalas'
        nomecsv = 'Segalas BD.csv'

    elif num == '13495487000253':
        nome = 'Destro'
        nomecsv = 'Destro BD.csv'

    elif num == '16624530000140':
        nome = 'BOCCHI'
        nomecsv = 'Bocchi BD.csv'

    elif num == '07757548000120':
        nome = 'CBN'
        nomecsv = 'CBN BD.csv'

    elif num == '11330623000149':
        nome = 'STAMPA'
        nomecsv = 'Stampa BD.csv'

    elif num == '56228356005958':
        nome = 'Ambev'
        nomecsv = 'Ambev BD.csv'

    elif num == '21381251000133':
        nome = 'Vigor'
        nomecsv = 'Vigor BD.csv'

    elif num == '76492305000200':
        nome = 'Ouro fino'
        nomecsv = 'Ouro fino BD.csv'

    elif num == '60409075019767':
        nome = 'Nestle'
        nomecsv = 'Nestle BD.csv'

    elif num == '28842819000115':
        nome = 'BDL'
        nomecsv = 'BDL BD.csv'

    elif num == '09241957000102':
        nome = 'Amabile'
        nomecsv = 'Amabile BD.csv'

    elif num == '25769266002844':
        nome = 'Arcom'
        nomecsv = 'Arcom BD.csv'

    elif num == '15814440000150':
        nome = 'IBD'
        nomecsv = 'IBD BD.csv'

    elif num == '81611931000209':
        nome = 'OESA'
        nomecsv = 'OESA BD.csv'

    elif num == '01838723012567':
        nome = 'BRF'
        nomecsv = 'BRF BD.csv'

    elif num == '09095640000105':
        nome = 'Sueko'
        nomecsv = 'Sueko BD.csv'

    elif num == '17790307000640':
        nome = 'E-UB'
        nomecsv = 'E-UB BD.csv'

    elif num == '90724261000902':
        nome = 'Oniz'
        nomecsv = 'Oniz BD.csv'

    elif num == '00249906000144':
        nome = 'Lemes e Oliveiras'
        nomecsv = 'Lemes e Oliveiras BD.csv'

    elif num == '19195971000162':
        nome = 'DP4'
        nomecsv = 'DP4 BD.csv'

    elif num == '01554188000182':
        nome = 'Grupo Lobo'
        nomecsv = 'Grupo Lobo BD.csv'

    elif num == '10842044000384':
        nome = 'Copini'
        nomecsv = 'Copini BD.csv'

    elif num == '24509214000156':
        nome = 'Oliveira'
        nomecsv = 'Oliveira BD.csv'

    elif num == '77595395000490':
        nome = 'Frimesa'
        nomecsv = 'Frimesa BD.csv'
    
    elif num == '29635803000102':
        nome = 'Hawaii Distribuição de materiais'
        nomecsv = 'Hawaii BD.csv'

    elif num == '76430438010134':
        nome = 'Max Atacadista'
        nomecsv = 'Max BD.csv'

    elif num == '36486464000105':
        nome = 'Chef Distribuidora'
        nomecsv = 'Chef BD.csv'

    elif num == '17467515002738':
        nome = 'Cafe Tres Coracoes S.A'
        nomecsv = 'Três corações BD.csv'

    elif num == '02914460045170':
        nome = 'Seara'
        nomecsv = 'Seara BD.csv'
    
    else:
        print('Empresa não cadastrada')

    print('')
    print(f'Essa nota é da empresa: {nome}')
    print(30*'-')

    return nomecsv


#import:
import existprod
import comparador as CP

#programa principal
xml = str(input('Nome do arquivo: '))+'.xml'
cnpj = cnpj(xml)
print(f'cnpj = {cnpj}')
nomecsv = bibemp(cnpj)

existprod.cadp(xml, nomecsv)

CP.comparador(xml, nomecsv)



 