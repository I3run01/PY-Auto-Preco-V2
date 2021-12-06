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

    print('')
    print(f'Essa nota é da empresa: {nome}')
    print(30*'-')

    return nomecsv


#import:
import existprod

#programa principal
xml = str(input('Nome do arquivo: '))+'.xml'
cnpj = cnpj(xml)
print(f'cnpj = {cnpj}')
nomecsv = bibemp(cnpj)

existprod.cadp(xml, nomecsv)





