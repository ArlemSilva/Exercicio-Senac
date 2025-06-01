notas = []

contador = 1

try:
    while contador <= 5:
        nota = float(input(f'Digite a sua {contador}ª nota '))
        notas.append(nota)
        contador += 1
except:
    print()

print(notas)

qtd_notas = len(notas)
media = sum(notas) / qtd_notas
print(f'A Media das notas é {media}')

notas.sort()

print(f'A menor nota é {notas[0]} e a maior nota é {notas[4]} ')

print('As notas acima da media são: ')
print([n for n in notas if n > media])

