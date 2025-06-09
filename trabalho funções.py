alunos_notas = {'joao': [6.0, 5.5, 7.0], 'ana': [8.0, 7.5, 9.0]}
lista_notas = []
atualizar_notas = []  
def add_notas(a):        
            alunos_notas[aluno] = notas # sintaxe para adicionar ou substituir o Value     
            atualizar_notas.append(notas) # sintaxe para adicionar ao final da lista
            
            novas_notas = print(f'Nome:{aluno}\nNotas: {atualizar_notas}\nNota(s) Adicionado com sucesso! ')
            return novas_notas
def media(b):#nota
    media_notas = sum(notas) / len(notas)
    return media_notas
def situacao(c):
    if media(notas) > 7:
       situacao = print(f'Situação: o aluno está Aprovado')
    else:
       situacao = print(f'Situação: o aluno está Reprovado')
       return situacao
print('Boa noite usuário!\nEscolha uma opção')
while True:
    opcoes = int(input('\n1) Cadastrar aluno\n2) Calcular Média\n3) Verificar a situação do Aluno\n4) Exibir o Boletim\n5) Exibir todos os boletins\n0) Sair\n--> '))
    if opcoes in [0,1,2,3,4,5]:        
        print()
        break
    else:
        print('Digite uma opção valida')
match opcoes:
    case 1:  
        aluno = input('Digite o seu nome.\n').strip().lower()      
        consulta = alunos_notas.get(aluno, 'Aluno não cadastrado') # variavel = sintaxe para consulta de chave 
        print(consulta)
        for notas in range(1,4):       
            notas = float(input('Digite as suas notas \n')) 
            add_notas(notas)

    case 2:
        aluno = input('Digita o nome de um aluno: ').strip().lower()
        if aluno in alunos_notas:
            notas = alunos_notas[aluno]
            resultado = media(notas)
            print(f'A media de {aluno} é {resultado:.2f}')
        else:
            print('Aluno não está cadastrado')
    case 3:
        aluno = input('Digita o nome de um aluno: ').strip().lower()
        if aluno in alunos_notas:
            notas = alunos_notas[aluno]     
            situacao(notas)
        else:
            print('Aluno não está cadastrado')
    case 4:
        aluno = input('Digita o nome de um aluno: ').strip().lower()
        if aluno in alunos_notas:
            notas = alunos_notas[aluno]  
            print(f'Nome do aluno(a): {aluno}\nNotas: {notas}\nMédia: {media(notas):.2f}\n')
            situacao(notas) # não pode ter print (da função) dentro de outro print (do boletim)
        else:
            print('Aluno não está cadastrado')
    case 5:
        for aluno in alunos_notas:
            notas = alunos_notas[aluno]
            if media(notas) > 7:
                print(f'Nome do aluno(a): {aluno}\nNotas: {notas}\nMédia: {media(notas):.2f}\nSituação: o aluno está Aprovado\n')
            else:
                print(f'Nome do aluno(a): {aluno}\nNotas: {notas}\nMédia: {media(notas):.2f}\nSituação: o aluno está Reprovado\n')  

