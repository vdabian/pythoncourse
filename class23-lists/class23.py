"""
Lists
slicing
append, insert, pop, del, clear, extend, +
min, max
range
"""

#        0    1    2    3    4   5
#list = ['A', 'B', 'C', 'D', 'E', 10.5]
#       -5   -4   -3   -2   -1

#list[5] = 'Other Thing'

print(list[0])
print(list[-6])
print(list)
print(list[5])

#     slicing

print()
print('Slicing:')
print(list[0:3])
print('Três primeiros: ', list[:3])
print('A partir do indice 2: ',list[2:])
print('Last item: ',list[-1])
print('First: ',list[0])
print('2 em 2: ',list[::2])
print('Trás para frente: ', list[::-1])

#     functions

print()
print('Functions:')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print('Lista 1: ', l1)
print('Lista 2: ', l2)

l3 = l1 + l2
print('Lista 3 (l1 + l2): ', l3)

#extend
l1.extend(l2)
print('l1 extend l2: ', l1)
l1.extend('a')
print('l1 extend a: ', l1)

#append
l2.append('b')
print('L2 append b:', l2)

#insert
l2.insert(0, 'X')
print('Inserindo X no início de l2: ', l2)

#pop
print('l2 antes da remoção: ', l2)
l2.pop()
print('l2 removendo o último elemento: ', l2)

#del
l4 = [1,2,3,4,5,6,7,8,9]
l4.insert(0, 'Banana')
print('Lista: ', l4)

#del(l2[3:5])
del(l4[0])
print('Excluindo valores: ', l4)

#max
print(max(l4))
#min
print(min(l4))

#range
l5 = list(range(0,100,8))
print(l5)

#     iteravel

l6 = [0,1,2,3,4,5,6,7,8,9]
soma = 0
for valor in l6:
    soma = soma + valor

print(soma)

l7 = ['String', True, 10, -20.5]

for elem in l7:
    print(f'O tipo do é {type(elem)} e seu valor é {elem}')

secreto = 'voyage'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break


    letra = input(' Digite uma letra: ')

    if len(letra) > 1:
        print('Não vale, difite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Very nice! A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Vish! A letra "{letra}" não existe na palavra')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'You win! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra certa está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances')
    print()