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

print(f'{itens , precos}')

soma = sum(precos)

print(f'O valor da compra é {soma}')

