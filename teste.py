import xml.etree.ElementTree as ET

xml = '41211213495487000253550010021789921287996756 (1).xml'

tree = ET.parse(xml)
root = tree.getroot()

link = '{http://www.portalfiscal.inf.br/nfe}'

lvICMSST10 = []
for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto/{link}ICMS"):
    vICMSST10 = ICMS.find(f'{link}ICMS10/{link}vICMSST')
    try:
        vICMSST10 = vICMSST10.text
    except:
        vICMSST10 = str(0)
    lvICMSST10.append(vICMSST10)

print(lvICMSST10)
