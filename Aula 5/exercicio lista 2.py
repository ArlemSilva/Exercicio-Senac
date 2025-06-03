itens = []
precos = []
contador = 1


try:
    while contador <= 3:
        item = input('Digite o produto : ')
        if item.isalpha():
            itens.append(item)
            
        else:
            print('Digite um produto disponivel')

        preco = float(input('Digite o preço do produto: '))
        precos.append(preco)
        contador += 1      
        
except:
    print()

#print(f'{itens , precos}')

#print(f'O produto {itens[0]} custa {precos[0]}, o produto {itens[1]} custa {precos[1]} e o produto {itens[2]} custa {precos[2]}.')

undcompra = 0
while undcompra < len(itens):
    print(f'O produto {itens[undcompra]} custa {precos[undcompra]}')
    undcompra += 1

soma = sum(precos)

print(f'O valor da compra é {soma}')

