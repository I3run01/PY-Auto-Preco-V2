import xml.etree.ElementTree as ET

xml = '41211261186888014305550050047372921091188006.xml'

tree = ET.parse(xml)
root = tree.getroot()

link = '{http://www.portalfiscal.inf.br/nfe}'

lvFCPST = []
for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto/{link}ICMS"):
    vFCPST = ICMS.find(f'{link}ICMS10/{link}vFCPST')
    try:
        vFCPST = vFCPST.text
    except:
        vFCPST = str(0)
    lvFCPST.append(vFCPST)

lIPI = []
for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto/{link}IPI"):
    IPI = ICMS.find(f'{link}IPITrib/{link}vIPI')
    try:
        IPI = IPI.text
    except:
        IPI = str(0)
    lIPI.append(IPI)
