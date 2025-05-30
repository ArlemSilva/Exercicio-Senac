try: 
    num1 = int(input('digite um numero '))
    operacao = input('qual operação matematica iremos utilizar? ')
    num2 = int(input('digite o segundo numero'))
        
    if operacao == 'soma':
        resultado = num1 + num2
        print(f'o calculo dos numeros {num1} e {num2} é {resultado}')
        
    elif operacao == 'multiplicação':
        resultado = num1 * num2
        print(f'o calculo dos numeros {num1} e {num2} é {resultado}')
    
    elif operacao == 'divisao':
        resultado = num1 / num2
        print(f'o calculo dos numeros {num1} e {num2} é {resultado}')
    
    elif operacao == 'subtração':
        resultado = num1 - num2
        print(f'o calculo dos numeros {num1} e {num2} é {resultado}')
    
except ZeroDivisionError:
    print('divisao por zero nao é permitido')

except ValueError:
    print('digite apenas numeros')

except:
    print('deu erro, digite novamente')