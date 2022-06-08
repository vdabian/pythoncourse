"""
For / Else em Python
"""

var = ['Luiz Otávio', 'João', 'Dabian']

"""
for valor in var:
    if valor.startswith('D'):
        print(f'Começa com D: {valor}')
    else:
        print('Não começa com D')
#     break
#     continue


inicia_com_j = False
for valor in var:
    if valor.lower().startswith('j'):
        inicia_com_j = True

if inicia_com_j:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe!')
"""

inicia_com_j = False
for valor in var:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe!')