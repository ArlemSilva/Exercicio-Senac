lista = []

while True:
    try:
        nome = input('Digite um nome: ')

        if not nome.isalpha():
            raise ValueError('Digite um nome valido sem numeros.')
        
        lista.append(nome)

        sair = input('Deseja adicionar mais um nome? ').lower()

        if sair != 'sim':
            break

    except:
        print('Erro')

print(lista)
                        