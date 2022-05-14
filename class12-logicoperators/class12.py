"""
Logic Operators
and, or, not
in and not in

a = 2
b = 2
c = 3

var = a == b and b < c
print(var)
var = a == b or b < c
print(var)
var = not a == b and not b < c
print(var)

# AND => True and True = True ... True and False = False
comp1 and comp 2

# OR => True or True = True
comp1 or comp2

# NOT => True and True = False ... True and False = True
a = 2
b = 3
if not b > a:
    print("B > A.")
else:
    print("A > B.")
"""

name = "Vinícius Dabian"
if 'u' in name:
    print("Name have letter u")
else:
    print("Name don't have letter u")

name = "Vinícius Dabian"
if 'u' not in name:
    print("Name don't have letter u")
else:
    print("Name have letter u")

user = input('Name: ')
passoword = input('Password: ')

user_bd = 'vdabian'
password_bd = '123456'

if user_bd == user and password_bd == passoword:
    print('Login successfully!')
else:
    print('Username or password is invalid!')