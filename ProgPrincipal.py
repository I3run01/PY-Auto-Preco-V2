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





