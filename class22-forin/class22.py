"""
For in Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

text = 'Python'
count = 0

#while count < len(text):
#    print(text[count])
#    count += 1

#for n, letter in enumerate(text):
#    print(n, letter)

for letter in text:
    print(letter)

#for number in range(10):
#    print(number)

#for number in range(0, 10, 2):
#    print(number)

#for n in range(0, 10, 2):
#    print(n)

#for n in range(20, 10, -1):
#    print(n)

#for n in range(100):
#    if n % 8 == 0:
#        print(n)

"""
new_string = ''

for letter in text:
    if letter =='t':
        new_string = new_string + letter.upper()
    elif letter =='h':
        new_string = new_string + letter.upper()
    else:
        new_string += letter

print(new_string)
"""

#continue - pula para próximo laço
#break - para o laço

new_string = ''

for letter in text:
    if letter =='t':
        continue
        new_string = new_string + letter.upper()
    elif letter =='h':
        new_string = new_string + letter.upper()
        break
    else:
        new_string += letter

print(new_string)
