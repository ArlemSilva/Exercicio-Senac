''' com contador para caso chegue a zero, o sistema bloqueia o acesso '''

''' contador = 0

while contador <= 5 
    print(f'Nº {contador}')
    contador += 1 '''

while True:
    senha = input ('Digite a senha: ')

    if senha == 'senac@13455':
        print('Acesso permitido')
        break
    else:
        print('Senha invalida')

