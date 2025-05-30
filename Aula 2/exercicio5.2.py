num1 = float(input('\nQual o valor total da compra?\n '))
compra = float(input('\nQual a forma de pagamento?\n1- Dinheiro\n2- Pix\n3- Cartão\n'))

match compra:
    case 1: 
        print(f'O valor total da compra é {num1-(num1*0.027)}')
    case 2:
        print(f'O valor total da compra é {num1-(num1*0.0195)}')
    case 3:
        print(f'O valor total da compra é {num1+(num1*0.0485)}')
    case _:
        print('Não entendi, refaça por favor')
