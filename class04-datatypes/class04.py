"""
Data types
str - string - 'This' "This"
int - integer - 123456 - 0 10 -1550 1000000 75
float - float - 0.0 -10,50 10.5 -50,93 40,47
bool - boolean - true or false
"""
print('Luis', type('Luis'))
print(1, type(1))
print(-10.50, type(-10.50))
print(10 == 10, type(10 == 10))
print('l' == 'L', type('l' == 'L'))
print(bool(''))
print(bool([]))
print(bool(0))

# Type casting
print('luis', type('luis'), bool('luis'))
print('10', type('10'), type(int('10')))
print('10', type('10'), type(10))
# print('luiz', int('luiz')) Error
# print('luiz', int('10.5')) Error
print('luiz', float('10.5'))
print('luiz', float('10'))
print(10+10)
print('10' + '10')

#Exercise

#String: name
print('Vinícius Dabian', type('Vinícius Dabian'))

#Integer: age
print(27, type(27))

#Float: height
print(1.83, type(1.83))

# > Of age
print(27 > 18, type(27 > 18))



