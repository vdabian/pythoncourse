"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""

# positives
text1 = 'Python s2'

# negatives
url = 'www.google.com.br/'
text2 = text1[2:6]
text3 = text1[:6]
text4 = text1[7:]
text5 = text1[-1]  # negatives
text6 = text1[-9]  # negatives
text7 = text1[-9:-3]  # negatives
text8 = text1[:-2]  # negatives
text9 = text1[0::2]   # characters pula
text10 = text1[0:6:2]   # characters pula
text11 = text1[0::3]   # characters pula
text12 = text1[:]

print(text1[2])
print(text1[8])
# print(text1[9]) Return error
print(url[:-1])  # Sem /
print(text2)
print(text3)
print(text4)
print(text5)  # negatives
print(text6)  # negatives
print(text7)  # negatives
print(text8)  # negatives
print(text9)  # negatives pula
print(text10)  # negatives pula
print(text11)  # negatives pula
print(text12)
print(len(text1))

