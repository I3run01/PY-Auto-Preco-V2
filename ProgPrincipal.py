def cnpj(xml):

    import xml.etree.ElementTree as ET

    tree = ET.parse(xml)
    root = tree.getroot()


    link = '{http://www.portalfiscal.inf.br/nfe}'
   

    for cnpj in root.findall(f"./{link}NFe/{link}infNFe/{link}emit/{link}CNPJ"):
       cnpjarq = cnpj.text
       
       return cnpjarq
       
def bibemp (cnpj):
    if cnpj == '62461140002834':
        nome = 'Panco'
        nomecsv ='Banco de dados/Panco BD.csv'
        
    elif cnpj =='61186888014305':
        nome ='Coca-Cola'
        nomecsv = 'Banco de dados/CC BD.csv'

    elif cnpj =='24782106000152':
        nome ='Tirol'
        nomecsv = 'Banco de dados/Tirol BD.csv'

    elif cnpj == '77887412000543':
        nome = 'DEYCON'
        nomecsv = 'Banco de dados/Deycon BD.csv'

    elif cnpj == '12133164000176':
        nome = 'RD'
        nomecsv = 'Banco de dados/RD BD.csv'

    elif cnpj == '93209765047342':
        nome = 'WMS'
        nomecsv = 'Banco de dados/WMS BD.csv'

    elif cnpj == '03303285000128':
        nome = 'Arrojito'
        nomecsv = 'Banco de dados/Arrojito BD.csv'

    elif cnpj == '73778144000147':
        nome = 'Triunfante'
        nomecsv = 'Banco de dados/Triunfante BD.csv'

    elif cnpj == '01333984000438':
        nome = 'Segalas'
        nomecsv = 'Banco de dados/Segalas BD.csv'

    elif cnpj == '13495487000253':
        nome = 'Destro'
        nomecsv = 'Banco de dados/Destro BD.csv'

    elif cnpj == '16624530000140':
        nome = 'BOCCHI'
        nomecsv = 'Banco de dados/Bocchi BD.csv'

    elif cnpj == '07757548000120':
        nome = 'CBN'
        nomecsv = 'Banco de dados/CBN BD.csv'

    elif cnpj == '11330623000149':
        nome = 'STAMPA'
        nomecsv = 'Banco de dados/Stampa BD.csv'

    elif cnpj == '56228356005958':
        nome = 'Ambev'
        nomecsv = 'Banco de dados/Ambev BD.csv'

    elif cnpj == '21381251000133':
        nome = 'Vigor'
        nomecsv = 'Banco de dados/Vigor BD.csv'

    elif cnpj == '76492305000200':
        nome = 'Ouro fino'
        nomecsv = 'Banco de dados/Ouro fino BD.csv'

    elif cnpj == '60409075019767':
        nome = 'Nestle'
        nomecsv = 'Banco de dados/Nestle BD.csv'

    elif cnpj == '28842819000115':
        nome = 'BDL'
        nomecsv = 'Banco de dados/BDL BD.csv'

    elif cnpj == '09241957000102':
        nome = 'Amabile'
        nomecsv = 'Banco de dados/Amabile BD.csv'

    elif cnpj == '25769266002844':
        nome = 'Arcom'
        nomecsv = 'Banco de dados/Arcom BD.csv'

    elif cnpj == '15814440000150':
        nome = 'IBD'
        nomecsv = 'Banco de dados/IBD BD.csv'

    elif cnpj == '81611931000209':
        nome = 'OESA'
        nomecsv = 'Banco de dados/OESA BD.csv'

    elif cnpj == '01838723012567':
        nome = 'BRF'
        nomecsv = 'Banco de dados/BRF BD.csv'

    elif cnpj == '09095640000105':
        nome = 'Sueko'
        nomecsv = 'Banco de dados/Sueko BD.csv'

    elif cnpj == '17790307000640':
        nome = 'E-UB'
        nomecsv = 'Banco de dados/E-UB BD.csv'

    elif cnpj == '90724261000902':
        nome = 'Oniz'
        nomecsv = 'Banco de dados/Oniz BD.csv'

    elif cnpj == '00249906000144':
        nome = 'Lemes e Oliveiras'
        nomecsv = 'Banco de dados/Lemes e Oliveiras BD.csv'

    elif cnpj == '19195971000162':
        nome = 'DP4'
        nomecsv = 'Banco de dados/DP4 BD.csv'

    elif cnpj == '01554188000182':
        nome = 'Grupo Lobo'
        nomecsv = 'Banco de dados/Grupo Lobo BD.csv'

    elif cnpj == '10842044000384':
        nome = 'Copini'
        nomecsv = 'Banco de dados/Copini BD.csv'

    elif cnpj == '24509214000156':
        nome = 'Oliveira'
        nomecsv = 'Banco de dados/Oliveira BD.csv'

    elif cnpj == '77595395000490':
        nome = 'Frimesa'
        nomecsv = 'Banco de dados/Frimesa BD.csv'
    
    elif cnpj == '29635803000102':
        nome = 'Hawaii Distribuição de materiais'
        nomecsv = 'Banco de dados/Hawaii BD.csv'

    elif cnpj == '76430438010134':
        nome = 'Max Atacadista'
        nomecsv = 'Banco de dados/Max BD.csv'

    elif cnpj == '36486464000105':
        nome = 'Chef Distribuidora'
        nomecsv = 'Banco de dados/Chef BD.csv'

    elif cnpj == '17467515002738':
        nome = 'Cafe Tres Coracoes S.A'
        nomecsv = 'Banco de dados/Três corações BD.csv'

    elif cnpj == '02914460045170':
        nome = 'Seara'
        nomecsv = 'Banco de dados/Seara BD.csv'

    elif cnpj == '45614719000150':
        nome = 'Life'
        nomecsv = 'Banco de dados/Life BD.csv'

    elif cnpj == '38714277000159':
        nome = 'Avante'
        nomecsv = 'Banco de dados/Avante BD.csv'

    elif cnpj == '44352956000128':
        nome = 'Suco&só'
        nomecsv = 'Banco de dados/Suco&só BD.csv'

    elif cnpj == '26312724000164':
        nome = 'Mega Brasil'
        nomecsv = 'Banco de dados/MegaBrasil BD.csv'

    else:
        print('Empresa não cadastrada')
        return

    print('')
    print(f'Essa nota é da empresa: {nome}')
    print(30*'-')

    return nomecsv


#import:
import Scripts.existprod as existprod
import Scripts.comparador as CP

#programa principal
xml = str(input('Nome do arquivo: '))+'.xml'
cnpj = cnpj(xml)
print(f'cnpj = {cnpj}')
nomecsv = bibemp(cnpj)

existprod.cadp(xml, nomecsv)

CP.comparador(xml, nomecsv)



 