print('\nOlá usuário\n')

nome = input('Qual o seu nome? ')
limite = float(input('\nQual o limite do seu cartão? '))
valorCompra = float(input('\nQual o valor da sua compra? '))
excedente = valorCompra - limite

if limite >= valorCompra:
    print(f'\n{nome}, a sua compra esta autorizada\n ')
else:
    print(f'\n{nome}, infelizmente a sua compra nao esta autorizada, a compra excedeu {excedente} reais do limite, entre contato com a Central de Relacionamento\n')