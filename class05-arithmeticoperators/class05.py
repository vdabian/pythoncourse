"""
+, -, *, /, //, **, %, ()
+ Addition
- Subtraction
* Multiplication
/ Division
// Integer division
** Exponentiation
% Rest of Division
"""

print('Multiplication (*): ', 10 * 10)
print('Addition (+): ', 10 + 10)
print('Subtraction (-): ', 10 - 5)
print('Divison (/): ', 10 / 2)
# print('Multiplication (*): ', '10' * '10') Error
print('Multiplication like repetition (*): ', 10 * '10')
print('Addition  (+): ', '5' + '5')
# print('Addition  (+): ', 5 + '5') Error
print('Vinícius' + ' ' + 'Dabian')
# print('Vinícius' + ' ' + 'Dabian is' + 27 + 'years hold') Error
print('Vinícius' + ' ' + 'Dabian is ' + str(27) + ' years hold')
print(10.5 // 5)
print(10.5 // 2.1)
print(10.5 / 2.11)
print(2 ** 2)
print(10 % 5)
print(10*(10 + 5))
print(10 * 10 + 5)
print(20*'A')
print(20*2)
print('20'+'A')
print(20+2)

"""
Precedência dos Operadores Aritméticos
Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses (como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas (de maior para menor precedência).

( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm precedência, você pode ver a lista completa em https://docs.python.org/3/reference/expressions.html#operator-precedence (sempre utilize a documentação oficial como reforço caso necessário).

Caso tenha dúvidas, faça testes com números. Por exemplo, olhe para essa conta e tente decifrar como chegar no resultado: 2 + 5 * 3 ** 2 - (23.5 + 23.5) (o resultado é 0.0). Para isso você precisa realizar as contas com maior precedência primeiro.
"""