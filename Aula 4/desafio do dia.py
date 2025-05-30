print('Olá! Hoje começaremos mais uma votação para o representante de turma!!!')
while True:
    try:
        nome = input('Qual é o seu nome? -> ').upper()
        if not nome.isalpha():
            raise ValueError('Por favor, insira um nome valido')
        break
    except ValueError as e:
        print(e)

while True:
    try:
        idade = int(input('Qual a sua idade? -> '))
        if idade >= 14:
            break
        else:
            print('infelizmente voce nao tem idade para votar')
    except ValueError:
        print('Digite uma idade valida!')


voto1 = 0
voto2 = 0
voto3 = 0

candidatos = print('Os candidatos desse ano são:\n1) Son Goku\n2) Uzumaki Naruto \n3) Monkey D. Luffy')
while True:
    while True:
        try:
            voto = int(input('Em qual candidato irá votar? -> '))
            if voto in [1,2,3]:
                print('Voto computado!')
                break
            else: 
                print(f'Candidato invalido, selecione um dos candidatos disponiveis\n1) Son Goku\n2) Uzumaki Naruto \n3) Monkey D. Luffy.')
        
        except:
            print()
        
    
    match voto:
        case 1:
            voto1 += 1

        case 2:
            voto2 += 1
             
        case 3:
            voto3 += 1

    votar = input('Deseja votar novamente? S/N ').upper()
    if votar != 'S':
        break
    else:
        print()

print(f'\nO resultado atual da votação é:\n1)Son Goku = {voto1}\n2) Uzumaki Naruto {voto2}\n3) Monkey D. Luffy {voto3}\n')

if voto1 > voto2 and voto1 > voto3:
    print('O vencedor da eleição de representante de turma é o Son Goku')
elif voto2 > voto1 and voto2 > voto3:
    print('O vencedor da eleição de representante de turma é o Uzumaki Naruto')
elif voto3 > voto1 and voto3 > voto2:
    print('O vencedor da eleição de representante de turma é o Monkey D. Luffy')
else: 
    print('Houve um empate na eleição, havera um segundo turno')

