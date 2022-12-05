#Código para calculo de fatorial - 1) utilizando o módulo Factorial da biblioteca math.
#2) Utilizando o modelo matemático tradicional com laço de repetição while
from math import factorial
n = int(input('Digite um numero para calcular o fatorial: '))
f=factorial(n)
#c = n
#f=1
#while c > 0:
#    print('{} '.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f=f*c
#    c = c - 1
print(f)