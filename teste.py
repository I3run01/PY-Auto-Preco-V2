import xml.etree.ElementTree as ET

xml = '41211201333984000438550010008691091114449877 (1).xml'

tree = ET.parse(xml)
root = tree.getroot()

link = '{http://www.portalfiscal.inf.br/nfe}'

lvICMST90 = []
for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto/{link}ICMS"):
    vICMSST90 = ICMS.find(f'{link}ICMS90/{link}vICMSST')
    try:
        vICMSST90 = vICMSST90.text
    except:
        vICMSST90 = str(0)
    lvICMST90.append(vICMSST90)

print(lvICMST90)
