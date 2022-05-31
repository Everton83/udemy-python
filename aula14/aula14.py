"""
Documentação e funções built-in utéis
"""

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# isnumeric isdigit isdecimal
# checa numeros e positivos (1234567)
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pode converter os numeros para realizar as contas')

num3 = input('Digite um numero: ')
num4 = input('Digite outro numero: ')

try:
    num3 = float(num1)
    num4 = float(num2)
    print(num3 + num4)
except:
    print('ERROR')

    