usuario_filmes = {'joao': ['matrix, constantine'], 'maria' : ['titanic, avatar']}
listafilme = []
print('Boa noite usuário!\nEscolha uma opção')
while True:
    opcoes = int(input('\n1) Adicionar um filme\n2) Remover um filme\n3) Consultar a lista de filmes de um usuário\n4) Consultar todos os usuários cadastrados\n0) Sair\n--> '))
    if opcoes in [0,1,2,3,4]:        
        print()
        break
    else:
        print('Digite uma opção valida')

match opcoes:
    case 1: # DEU CERTO
        while True:
            usuario = input('Digite o seu usuário.\n').strip().lower()
            print(usuario_filmes.get(usuario, 'Usuario não cadastrado'))
            filme = input('Digite o nome do filme \n')                
           
            usuario_filmes[usuario]=(listafilme)
            usuario_filmes[usuario].append(filme)

            print(f'Nome:{usuario}\nFilme(s): {filme}\nFilme Adicionado com sucesso! ')
            a = input('Quer adicionar mais um filme? (s/n) \n').upper()

            if a == 'N':                
                print(f'Nome:{usuario}\nFilme(s):{listafilme} ')
                break    
            else:
                print()
            
    case 2:
            usuario = input('Digite o seu usuário.\n').strip().lower()
            filme = input(f'Qual filme deseja remover?\n{usuario_filmes[usuario]}\n').lower()
            usuario_filmes.pop(filme, 'o filme informado não existe.')
            print(f'Lista de filmes atualizada:\n{usuario_filmes[usuario]}')

    case 3: # DEU CERTO
        usuario = input('Digite o seu usuário.\n').lower() 
        print(f'Lista de filmes do usuario - {usuario} -\n{usuario_filmes[usuario]}\n')
    case 4: # DEU CERTO
        for usuario, filme in usuario_filmes.items(): 
            print(f"{usuario} - {filme}")
    case _: # DEU CERTO
        print('Aplicação encerrada.') 







'''for usuario, filme in usuario_filmes.items():
    print(f"{usuario} - {filme}")'''

