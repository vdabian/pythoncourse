
"""

# Solution 1

num1 = input('Enter a number: ')
num2 = input('Enter other number: ')

# isnumeric isdigit isdecimal

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print('Sum: ',num1 + num2)
    
else:
    print('Numbers cannot be converted to perform calculations')

# Solution 2

import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

num1 = input('Enter a number: ')
num2 = input('Enter other number: ')

if is_number(num1) and is_number(num2):
    num1= float(num1)
    num2= float(num2)
    print('Sum: ', num1 + num2)
else:
    print('Error')

"""

# Solution 3

num1 = input('Enter a number: ')
num2 = input('Enter other number: ')

try:
    num1= float(num1)
    num2= float(num2)
    print('Sum: ', num1 + num2)
except:
    print('Error')