print('\nBEM VINDO AO SENAC\n')

while True:  
    try:
        nome = input('Ola, qual o seu nome?\n').upper()
        if not nome.isalpha():
            raise ValueError ('Digite um nome valido')
        break
    except ValueError as e:
        print(e)

curso = int(input('1- Analise de dados\n2- Power BI\n3- Desenvolvimento de Banco de Dados\n4- Outros\nQual curso voce deseja fazer conosco?: '))

match curso:
    case 1:
        print('Parabens por escolher o curso Análise de Dados')
    case 2:
        print('Parabens por escolher o curso Power BI')
    case 3:
        print('Parabens por escolher o curso Banco de Dados')
    case 4:
        print('Acesse o nosso site e veja outras opções')
    case _:
        print('Opção invalida')
    

while True:
    try:
        idade = int(input('Digite a sua idade'))
        if idade <= '17':
            print('voce precisa de um responsavel para adquirir um curso') 
        break
    except:
        print()

print(f'Parabens {nome}, voce acaba de adquirir o curso de {curso}, te aguardamos no primeiro dia de aula. ')
