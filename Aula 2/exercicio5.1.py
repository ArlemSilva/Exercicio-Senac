num1 = float(input('\nQual o valor total da compra?'))
compra = float(input('\nQual a forma de pagamento?\n1- Dinheiro\n2- Pix\n3- Cartão\n '))

match compra:
    case 1: 
        print(f'O valor total da compra é {num1 * 0.973}')
    case 2:
        print(f'O valor total da compra é {num1 * 0.9805}')
    case 3:
        print(f'O valor total da compra é {num1 * 1.0485}')
    case _:
        print('Não entendi, refaça por favor')
