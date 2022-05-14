"""
Data input - Class 09
"""

name = input("What's your name? ")
print(f'User type {name} and variable type is ' f'{type(name)}')
print()

name = input("What's your name? ")
age = input("How old are you? ")
birth_year = 2022 - int(age)
print(f'{name} is {age} years old and he born in {birth_year}')
print()

#Calculator
number_1 = int(input("Type a number: "))
number_2 = input("Type other number: ")
number_2 = int(number_2)
print(number_1+number_2)
