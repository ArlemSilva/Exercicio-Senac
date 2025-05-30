try:
    num1 = int(input('Digite o primeiro numero '))
    num2 = int(input('Digite o segundo numero '))
    divisao = num1 / num2
    resultado = round(divisao, 2)

    print(f'O resultado da divisao é {resultado} ')

except ZeroDivisionError:
    print('Divisao por zero nao é permitido ')

except ValueError:
    print('Digite um nº valido ')

except:
    print('Erro inesperado ')
