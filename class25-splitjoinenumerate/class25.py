"""
Split, Join, Enumerate em Pyhton
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
print(lista_1)

lista_2 = string.split(',')
print(lista_2)

palavra = ''
contagem = 0

for valor in lista_1:
#    print(f' A palavra {valor} apareceu {lista_1.count(valor)} vezes na frase')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra =  valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x')

for valor in lista_2:
    print(valor.strip().capitalize())

#     Join

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string2)

#     Enumerate

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])


lista = [
    [0,2],
    [1,4],
    [2,6],
]

for v in lista:
    print(v[0], v[1])

lista = [
    [0,'Luiz'],
    [1,'João'],
    [2,'Maria'],
]

for indice, nome in lista:
    print(indice, nome)

lista = ['Luiz', 'João','Maria']
for indice, nome in enumerate(lista):
    print(indice, nome)

lista = ['Luiz', 'João','Maria']

n1, n2, n3 = lista
print(n2)