user = input('Type your user: ')
qtd = len(user)
print(user, qtd, type(qtd))

if qtd < 6:
    print('Please, enter at least six characters!')
else:
    print('Success!')

string1 = input('Please, enter: ')
string2 = input('Please, enter: ')
print(f'Quantity of characters is: {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__())

# error print(len(123456)) or print(len(1.2)) or print(len(True))