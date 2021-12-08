import xml.etree.ElementTree as ET

xml = '41211203303285000128550030002418641787202760 (1).xml'

tree = ET.parse(xml)
root = tree.getroot()

link = '{http://www.portalfiscal.inf.br/nfe}'

list = []
for prod in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod"):
    vDesc = prod.find(f'{link}vDesc')
    try:
        vDesc = vDesc.text
    except:
        vDesc = str(0)
    list.append(vDesc)

print(list)
