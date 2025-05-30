num1 = int(input('Diga o primeiro numero: '))
num2 = int(input('Diga o segundo numero: '))
calculo = float(input('Qual calculo deseja realizar?\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Modulo\n' ))

match calculo:
    case 1:
        print(f'O valor da soma dos numeros é {num1 + num2}')
    case 2:
        print(f'O valor da divisao dos numeros é {num1 - num2}')
    case 3:
        print(f'O valor da multiplicação dos numeros é {num1 * num2}')
    case 4:
        print(f'O valor da divisão dos numeros é {num1 / num2}')
    case 5:
        print(f'O valor do modulo dos numeros é {num1 % num2}')
    case _:
        print('Não te compreendi, repita a operação')

    
