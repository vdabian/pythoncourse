"""
while em python

Utilizando para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operates
"""

"""
while True:
    name = input(" What's your name ?")
    print(f'Hello {name}!')
"""

"""
x = 0

while x < 10:
    
    print(x)
    x = x + 1

print("It's over!")
"""

"""
x = 0

while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print("It's over!")
"""

"""
x = 0

while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print("It's over!")
"""

"""
x = 0  # column
y = 0  # line

while x < 10:

    y = 0

    while y < 5:

        print(f'X vale {x} e Y vale {y}')
        print(f'({x},{y})')
        y += 1

    x += 1

print("It's over!")
"""

while True:
    print()
    num_1 = input('Type a number: ')
    num_2 = input('Type another number: ')
    operator = input('Type a operator: ')
    logoff = input('Do you want to close the application ? Type [y]es or [n]o: ')

    if logoff == 'y':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Please, type a number!!!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '*':
        print(num_1 * num_2)
    else:
        print('Invalid operator!')