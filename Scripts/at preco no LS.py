lcod = []
lpreco = []
import Scripts.InLondrisoft as InLondrisoft

while True:
    cod = input(str('Código do produto:'))
    preco = input(str('preço do produto: '))
    op = input(str('Deseja continuar? [S/N]')).strip().upper()[0]
    preco = preco.replace('.',',')

    lcod.append(cod)
    lpreco.append(preco)

  
    if op == 'N':
        break

InLondrisoft.apreco(lcod,lpreco)
