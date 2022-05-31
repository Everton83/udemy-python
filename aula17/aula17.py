"""
Formatando valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - Numeros de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print( '{:.2f}'.format(divisao) )
print( f'{divisao:.2f}' )

nome = 'Everton Pinheiro'
print(f'{nome:s}')

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print (f'{num_4:0>10}')

num_5 = 1150
print (f'{num_5:0<10}')

num_6 = 1150
print (f'{num_6:0^10}')

num_7 = 1150
print (f'{num_7:.2f}')