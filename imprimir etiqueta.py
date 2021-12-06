lcod = []
import InLondrisoft

while True:
    cod = input(str('Código do produto:'))
    op = input(str('Deseja inserir outro codigo? [S/N]')).strip().upper()[0]

    lcod.append(cod)
  
    if op == 'N':
        break

InLondrisoft.ietiqueta(lcod)
