idade = int(input('Qual a sua idade? '))
ingresso = input('Voce comprou o ingresso? S/N ').upper()
nome = input('Qual e o seu nome? ').title()

if idade >= 18 and ingresso == 'S':
    print(f'{nome}, seu acesso esta liberado! ')
elif idade >= 18 and ingresso != 'S':
    print(f'{nome}, va ate a bilheteria e compre um ingresso. ') 
else:
    print('Acesso Negado')