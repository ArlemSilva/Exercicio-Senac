
produto = {'nome': 'mouse', 'preco' : 49.90, 'estoque': 25}

for chave, valor in produto.items():
    print (f'{chave} : {valor}')

while True:
    try:
        chave = input('Qual informação voce precisa? ').lower()
        if chave in produto:
            print(produto.get(chave))
            break
        else:
            print('chave nao existe')
    except:
        print()

produto['categoria'] = 'informatica'

produto['preco'] = 59.99

del produto['estoque']

for chave, valor in produto.items():
    print (f'{chave} : {valor}')






