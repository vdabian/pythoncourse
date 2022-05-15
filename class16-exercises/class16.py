"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que este não é um número inteiro.
"""

number = input('Please enter a integer number: ')

if number.isnumeric():
    number = int(number)
    if (number%2) == 0:
        print('Pair')
    else:
        print('Odd')
else:
    print('Please, try again and enter a integer number')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e boa noite 12-23
"""

hour = input('Please enter a integer hour: ')

if hour.isnumeric():
    hour = int(hour)
    if hour >= 0 and hour <= 11:
        print('Good morning!')
    elif hour >= 12 and hour <= 17:
        print('Good afternoon!')
    elif hour >= 18 and hour <= 23:
        print('Good night!')
    else:
        print('Please, try again and enter a valid hour 0 - 23')
else:
    print('Please, try again and enter a integer hour')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; Se for maior que 6 escreva "Seu nome é muito grande"
"""

name = input('Please enter your name: ')
name_characters = len(name)

if name_characters <= 4:
    print('Short name!')
elif name_characters >= 5 and name_characters <= 6:
    print('Normal name!')
else:
    print('Big name!')