''' primeiro : se a pessoa quer adicionar mais um nome, segundo caso: se existir um numero, encerrar o codigo'''

while True:
    nome = input('Digite o nome: ')

    if nome == 'N' or int():
        print('Encerrando o comando')
        break
    else:
        print('Nome armazenado')
