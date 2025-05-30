
try:
    while True:
        try:
            num1 = int(input('nº 1: '))
            break

        except ValueError:
            print('digite um numero valido')

    while True:
        try:
            op = int(input('Qual op? \n1) +\n2) -\n3) *\n4) /\n'))
            if 1 <= op <= 4:
                break

        except:
            print('Escolha uma opção disponivel')

    while True:
        try:
            num2 = int(input('nº 2: '))
            break

        except ValueError:
            print('digite um numero valido')   

    print('Com esses dados, a operação fica:\n')

    match op:
        case 1:
            print(f'soma =  {num1 + num2}')

        case 2:
            print(f'sub =  {num1 - num2}')

        case 3:
            print(f'mult =  {num1 * num2}')

        case 4:
            print(f'div =  {num1 / num2}')


except ZeroDivisionError:
    print('Não existe divisão por zero')


