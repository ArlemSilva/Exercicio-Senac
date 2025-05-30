lista = ['joao', 16, 'japeri']

print(f'o aluno mora no bairro {lista[2]}')

lista.append('RJ')
print(f'o aluno mora no bairro {lista[2]} e na cidade {lista[3]}')

lista.insert(1, 'Masculino')
print(lista[1:4])

#opções de remoção
del lista[2]
lista.pop(2)
'''lista = ['joao', 'mateus', 'sofia', 'maria', 'sofia']

lista.remove('sofia')'''

num1 = 10 
y = 10,5
nome = 'gabe'
print(type(num1))
print(type(y))
print(type(nome))