lista = []

print('Peço que voce digite 5 nomes ')

contador = 1


try:
    while contador <= 5:
        nome = input('Digite o nome: ').upper()
        if nome.isalpha() and nome not in lista:
            lista.append (nome)
            contador += 1      
                     
        else:
            print('Digite um nome valido')
except:
    print()
  

print(lista)

while True:
    try: 
        remover = input('Qual o nome que voce retira da lista? ').upper()

        if remover in (lista):
            lista.remove(remover)
            break
        else:
            print('Digite um nome presente na lista')
    except:
        print()

print(f'A lista de nomes apos a remoção: \n {lista}')





