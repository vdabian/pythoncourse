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
print(f'{name} is {age} years old and his BMI is {imc:.2f}')
print('{} is {} years old and his BMI is {:.2f}'.format(name, age, imc))
print('{0} is {1} years old and his BMI is {2:.2f}'.format(name, age, imc))
print('{n} is {a} years old and his BMI is {im:.2f}'.format(n=name, a=age, im=imc))