print('\nBEM VINDO AO SENAC\n')

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
    
