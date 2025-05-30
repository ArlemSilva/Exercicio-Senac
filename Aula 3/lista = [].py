''' primeiro : se a pessoa quer adicionar mais um nome, segundo caso: se existir um numero, encerrar o codigo'''


lista = []

while True:
    resposta = ('Quer adicionar um nome? S/N ').upper()

    if resposta == 'N':
        print('Vou encerrar o comando')
        break
    else:
        nome = input('Digite o nome desejado')
        lista.append(nome)
        
'''try:
    resposta = input('Quer adicionar um nome? S/N ').upper
    print('o nome digitado é {resposta}')

   except:
    print('digite um nome valido)')'''
      

     