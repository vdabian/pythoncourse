"""
Enumarate - Enumerar elementos da lista #list
"""

#lista = ['Edu', 'João', 'Luiz']

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu']
]

#print(lista[0][0])

#enumerada = list(enumerate(lista))
#print(enumerada[1][1][0])

for v1 in enumerate(lista, 0):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)

#for v1, v2 in enumerate(lista, 0):
#   print(v1, v2)