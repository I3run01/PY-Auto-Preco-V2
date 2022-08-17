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
        
    if num =='61186888014305':
        nome ='Coca-Cola'
        nomecsv = 'CC BD.csv'

    if num =='24782106000152':
        nome ='Tirol'
        nomecsv = 'Tirol BD.csv'

    if num == '77887412000543':
        nome = 'DEYCON'
        nomecsv = 'Deycon BD.csv'

    if num == '12133164000176':
        nome = 'RD'
        nomecsv = 'RD BD.csv'

    if num == '93209765047342':
        nome = 'WMS'
        nomecsv = 'WMS BD.csv'

    if num == '03303285000128':
        nome = 'Arrojito'
        nomecsv = 'Arrojito BD.csv'

    if num == '73778144000147':
        nome = 'Triunfante'
        nomecsv = 'Triunfante BD.csv'

    if num == '01333984000438':
        nome = 'Segalas'
        nomecsv = 'Segalas BD.csv'

    if num == '13495487000253':
        nome = 'Destro'
        nomecsv = 'Destro BD.csv'

    if num == '16624530000140':
        nome = 'BOCCHI'
        nomecsv = 'Bocchi BD.csv'

    if num == '07757548000120':
        nome = 'CBN'
        nomecsv = 'CBN BD.csv'

    if num == '11330623000149':
        nome = 'STAMPA'
        nomecsv = 'Stampa BD.csv'

    if num == '56228356005958':
        nome = 'Ambev'
        nomecsv = 'Ambev BD.csv'

    if num == '21381251000133':
        nome = 'Vigor'
        nomecsv = 'Vigor BD.csv'

    if num == '76492305000200':
        nome = 'Ouro fino'
        nomecsv = 'Ouro fino BD.csv'

    if num == '60409075019767':
        nome = 'Nestle'
        nomecsv = 'Nestle BD.csv'

    if num == '28842819000115':
        nome = 'BDL'
        nomecsv = 'BDL BD.csv'

    if num == '09241957000102':
        nome = 'Amabile'
        nomecsv = 'Amabile BD.csv'

    if num == '25769266002844':
        nome = 'Arcom'
        nomecsv = 'Arcom BD.csv'

    if num == '15814440000150':
        nome = 'IBD'
        nomecsv = 'IBD BD.csv'

    if num == '81611931000209':
        nome = 'OESA'
        nomecsv = 'OESA BD.csv'

    if num == '01838723012567':
        nome = 'BRF'
        nomecsv = 'BRF BD.csv'

    if num == '09095640000105':
        nome = 'Sueko'
        nomecsv = 'Sueko BD.csv'

    if num == '17790307000640':
        nome = 'E-UB'
        nomecsv = 'E-UB BD.csv'

    if num == '90724261000902':
        nome = 'Oniz'
        nomecsv = 'Oniz BD.csv'

    if num == '00249906000144':
        nome = 'Lemes e Oliveiras'
        nomecsv = 'Lemes e Oliveiras BD.csv'

    if num == '19195971000162':
        nome = 'DP4'
        nomecsv = 'DP4 BD.csv'

    if num == '01554188000182':
        nome = 'Grupo Lobo'
        nomecsv = 'Grupo Lobo BD.csv'

    if num == '10842044000384':
        nome = 'Copini'
        nomecsv = 'Copini BD.csv'

    if num == '24509214000156':
        nome = 'Oliveira'
        nomecsv = 'Oliveira BD.csv'

    if num == '77595395000490':
        nome = 'Frimesa'
        nomecsv = 'Frimesa BD.csv'
    
    if num == '29635803000102':
        nome = 'Hawaii Distribuição de materiais'
        nomecsv = 'Hawaii BD.csv'

    if num == '76430438010134':
        nome = 'Max Atacadista'
        nomecsv = 'Max BD.csv'

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



 