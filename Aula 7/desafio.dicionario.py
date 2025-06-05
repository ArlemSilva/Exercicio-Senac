usuario_filmes = {}
usuario = 0
filme = 0

print('Boa noite usuário!\n ')
opcoes = int(input('Escolha uma opção:\n1) Adicionar um filme\n2) Remover um filme\n3) Consultar a lista de filmes de um usuário\n4) Consultar todos os usuários cadastrados\n0) Sair\n--> '))
match opcoes:
    case 1: 
        usuario = input('Digite o seu usuário.\n').lower() #adicionar uma estrutura de indecisão para caso haja um usuario ja adicionado
        filme = input('Digite o nome do filme') #caso a pessoa queira adicionar mais algum filme, solicitar a decisão
        usuario_filmes[usuario] = filme
        input('Quer adicionar mais um filme?').lower
       








'''for usuario, filme in usuario_filmes.items():
    print(f"{usuario} - {filme}")'''
        

