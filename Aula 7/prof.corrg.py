produto = {'nome': 'mouse', 'preco' : 49.90, 'estoque': 25}

for chave, valor in produto.items():
    print (f'{chave} : {valor}')


chave = input('Qual informação voce precisa? ').lower()
print(produto.get(chave, 'essa informação nao esta disponivel'))


produto['categoria'] = 'informatica'

produto['preco'] = 59.99

del produto['estoque']

for chave, valor in produto.items():
    print (f'{chave} : {valor}')