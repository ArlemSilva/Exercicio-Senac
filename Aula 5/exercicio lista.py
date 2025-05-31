lista = []

print('Peço que voce digite 5 nomes ')

contador = 1

while True:
    try:
        while contador <= 5:
            nome = input('Digite o nome: ')
            if nome.isalpha():
                lista.append (nome)
                contador += 1
                    
            elif nome in lista['']:
                print('Digite um nome diferente')                
            else:
                print('Digite um nome valido')
    except:
        print()
  

    print(lista)

    while True:
        try: 
            remover = input('Qual o nome que voce retira da lista? ')

            if remover in (lista):
                lista.remove(remover)
                break
            else:
                print('Digite um nome presente na lista')
        except:
            print()

    print(f'A lista de nomes apos a remoção: \n {lista}')





