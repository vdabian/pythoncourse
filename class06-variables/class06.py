"""
Iniciar com letra, pode ter números, separar _, letras minúculas
"""

name = 'Vinícius Dabian'
age = 27 # int
height = 1.83 # float
is_legal = age > 18 # boll
weight = 80

print('Name:', name)
print('Age:', age)
print('Height:', height)
print('Is of legal age:', is_legal)
imc = weight / height ** 2

print(name, 'is', age, 'years old and his BMI is', imc)
