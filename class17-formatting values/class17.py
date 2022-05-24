"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^) (QUANTIDADE) (TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro

num1 = 10
num2 = 3
division = num1 / num2
print('{:.2f}'.format(division))
print(f'{division:.2f}')

name = 'Vinícius Dabian'
print(f'{name:s}')
"""

num1 = 1
print(num1)
print(f'{num1:0>10}')

num2 = 1150
print(f'{num2:0<10}')

num2 = 1150
print(f'{num2:.2f}')

num2 = 1150
print(f'{num2:0>10.2f}')

nome = 'Vinícius Dabian'
print( len(nome) )
print(f'{nome:#^50}')

nome = 'Vinícius Dabian'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome = 'Vinícius Dabian'
nome_formatado = '{n}'.format(n=nome)
print(nome_formatado)

nome = 'Vinícius'
sobrenome = 'Dabian'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

nome = 'Vinícius Dabian'
nome = nome.ljust(20, '#')
print(nome)
print(nome.lower())
print(nome.upper())
print(nome.title())