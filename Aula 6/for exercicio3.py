produtos = ['arroz','feijão', 'macarrão']
precos = [5.50, 4.20, 3.80]

for i in range(len(precos)):
    print(f'O produto {produtos[i]} custa R$ {precos[i]:.2f}')

valor_compra = 0
for i in precos:
    valor_compra += i

print(f'O valor total da compra é R$ {valor_compra:.2f}')

