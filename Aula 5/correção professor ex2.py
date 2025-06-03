notas = [1,2,5,5,9,4,5,6,1,3]

maior = max(notas) # maior valor da lista
menor = min(notas) # menor valor da lista
tamanho = len(notas) # tamanho da lista, quantidade de elementos na lista
media = sum(notas) / len(notas) # soma das variaveis da lista / tamanho da lista = media da lista

# o calculo para as notas acima da media
acima_da_media = [] # criação da lista para as notas acima da media
indice = 0 # uma nova variavel para fazer a contagem 
while indice <  len(notas): # enquanto
    if notas[indice] > media:
        acima_da_media.append(notas[indice])

