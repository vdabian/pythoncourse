#     Indices
#     01234567489........................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
#print(frase[5])
nova_string = ''

#while True:
#    print(contador)
#    contador += 1

input_do_user = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_user:
        nova_string += input_do_user.upper()
    else:
        nova_string += letra
    print(nova_string)
    contador += 1

print(nova_string)
