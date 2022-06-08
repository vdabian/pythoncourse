#secreto_temporario = ''
#for letra_secreta in secreto:
#    if letra_secreta in digitadas:
#        secreto_temporario += letra_secreta
#    else:
#        secreto_temporario += '*'

secreto_temporario = ''
secreto = 'python'
digitadas = ['t', 'o', 'p', 'y', 'h', 'n']

for letra_secreto in secreto:
    print (f'Iteração para a letra {letra_secreto}')
    if letra_secreto in digitadas:
        print(f'Opa, letra desejada {letra_secreto}')
        secreto_temporario += letra_secreto
    else:
        print(f'Letra não esperada {letra_secreto}')
        secreto_temporario += '*'

    print('secreto_temporario=', secreto_temporario)

print()
print(secreto_temporario)

if secreto == secreto_temporario:
    print('Você ganhou!')