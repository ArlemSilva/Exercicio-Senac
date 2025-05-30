valorTotal = float(input('Digite o valor total da compra: '))
pagamento = input('Digite o metodo de pagamento (diheiro, pix ou cartao: )').lower()
#forma de calculo mais facil, porem mais extensa.
if pagamento == 'dinheiro':
    valorTotal = valorTotal - (valorTotal * 0.027)
    print(valorTotal)
elif pagamento == 'pix':
    valorTotal = valorTotal - (valorTotal * 0.0195)
elif pagamento == 'cartao':
    valorTotal = valorTotal + (valorTotal * 0.0485)
else:
    print('Metodo de pagamento invalido')