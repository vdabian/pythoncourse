"""
Operators = Returns boolean
== equal
> bigger
>= greater equal
< smaller
<= lesser equal
!= different

print(2 == 1)
print(2 == '2')
print(2 == 2)

num1 = 2  # int
num2 = 2  # int
expression = (num1 == num2)
print(expression)

expression = (num1 > num2)
print(expression)

num2 = 3  # int
expression = (num1 > num2)
print(expression)

num2 = 2  # int
expression = (num1 >= num2)
print(expression)
expression = (num1 <= num2)
print(expression)

expression = (num1 != num2)
print(expression)
num2 = 3  # int
expression = (num1 != num2)
print(expression)
"""

name = input("What's your name? ")
age = input('How old are you? ')
age = int(age)

#limit
age1 = 20
age2 = 30

if age >= age1 and age <= age2:
    print(f'{name} can have a loan.')
else:
    print(f'{name} cant have a loan.')