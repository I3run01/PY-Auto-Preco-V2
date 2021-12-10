def preco(cProd, margem, quantunit, xml):

    #Parametro temporários
    #cProd = 'f000000000000059321'
    #margem = str(50)
    #quantunit = str(1)
    #xml = 'Pancoxml.xml'

    #importações
    import xml.etree.ElementTree as ET

    #converções
    cProd = cProd[1:]
    margem = float(margem)
    quantunit = float(quantunit)

    #árvore e raiz
    tree = ET.parse(xml)
    root = tree.getroot()


    #parâmetros importantes
    margem = margem
    quantunit = quantunit

    #abreviação de nome
    link = '{http://www.portalfiscal.inf.br/nfe}'

    #Busca das informações necessárias
    lvFCPST = []
    for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto"):
        vFCPST = ICMS.find(f'{link}ICMS/{link}ICMS10/{link}vFCPST')
        try:
            vFCPST = vFCPST.text
        except:
            vFCPST = str(0)
        lvFCPST.append(vFCPST)

    lIPI = []
    for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto"):
        IPI = ICMS.find(f'{link}IPI/{link}IPITrib/{link}vIPI')
        try:
            IPI = IPI.text
        except:
            IPI = str(0)
        lIPI.append(IPI)

    lvICMSST10 = []
    for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto"):
        vICMSST10 = ICMS.find(f'{link}ICMS/{link}ICMS10/{link}vICMSST')
        try:
            vICMSST10 = vICMSST10.text
        except:
            vICMSST10 = str(0)
        lvICMSST10.append(vICMSST10)

    lvICMST90 = []
    for ICMS in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}imposto"):
        vICMSST90 = ICMS.find(f'{link}ICMS/{link}ICMS90/{link}vICMSST')
        try:
            vICMSST90 = vICMSST90.text
        except:
            vICMSST90 = str(0)
        lvICMST90.append(vICMSST90)

    lcProdin = []
    for cProdin in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}cProd"):
        lcProdin.append(cProdin.text)

    lvProd = []
    for vProd in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}vProd"):
        lvProd.append(vProd.text)

    lqCom = []
    for qCom in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}qCom"):
        lqCom.append(qCom.text)

    lvDesc = []
    for vDesc in root.findall(f"./{link}NFe/{link}infNFe/{link}det"):
        vDesc = vDesc.find(f'{link}prod/{link}vDesc')
        try:
            vDesc = vDesc.text
        except:
            vDesc =str(0)
        lvDesc.append(vDesc)

    #calculo do preco
    termo = lcProdin.index(cProd)
    desconto = float(lvDesc[termo])
    imposto = float(lvICMST90[termo])+float(lvICMSST10[termo])+float(lvFCPST[termo])+float(lIPI[termo])

    preco = ((1+(margem/100))*((float(lvProd[termo])+imposto-desconto)/float(lqCom[termo])))/quantunit
    preco = str(preco)
    ponto = preco.find('.')
    precoint = preco[0:ponto]
    precofloat = (preco[ponto+1:])
    precofloat = int(precofloat[0:2])

    if precofloat <= 20:
        precofloat = str(20)

    elif precofloat >20 and precofloat <= 50:
        precofloat = str(50)

    else:
        precofloat = str(99)

    preco = precoint + '.' + precofloat




    return preco


def nome(cProd, xml):

    #cProd = 'f56298'
    #xml = 'CCxml.xml'

    import xml.etree.ElementTree as ET
    cProd = cProd[1:]
    tree = ET.parse(xml)
    root = tree.getroot()


    #abreviação de nome
    link = '{http://www.portalfiscal.inf.br/nfe}'

    lcProdin = []
    for cProdin in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}cProd"):
        lcProdin.append(cProdin.text)

    lxProd = []
    for xProd in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}xProd"):
        lxProd.append(xProd.text)
        
    termo = lcProdin.index(cProd)
    nome = lxProd[termo]

    return nome
