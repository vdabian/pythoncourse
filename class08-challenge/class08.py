"""
* Create variables for name (Str), age (int)
* height (float) and weight (float)
* Create variable for current year (int)
* Birth year
* IMC to two decimal cases
* Text in screen
"""
name = 'Vinícius Dabian'
age = 27
height = 1.83
weight = 65.5
current_year = 2022
birth_year = current_year - age
imc = weight / height ** 2

print(name, 'is', age, 'years old. Your birth year is', birth_year, '. HIS IMC is', imc, '. He is', height, 'tall and weighs', weight)
print(f'{name} is {age} years old. Your birth year is {birth_year}. He is {height} tall and weights {weight}. His IMC is {imc:.2f}.')
print('{} is {} years old. Your birth year is {}. He is {} tall and weights {}. His IMC is {:.2f}.'.format(name, age, birth_year, height, weight, imc))