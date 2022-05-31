"""
Operadores Relacionais
== igualdade > maior que
>= Maior que ou igual a
> maior que
< menor que
<= Menor que ou igual a
|= é diferente
"""

num_1 = 2
num_2 = 2

expressao1 = (num_1 == num_2)
expressao2 = (num_1 >= num_2)
expressao3 = (num_1 > num_2)
expressao4 = (num_1 < num_2)
expressao5 = (num_1 <= num_2)
expressao6 = (num_1 != num_2)

print(expressao1, '== igualdade > maior que')
print(expressao2, '>= Maior que ou igual a')
print(expressao3, '> maior que')
print(expressao4, '< menor que')
print(expressao5, '<= Menor que ou igual a')
print(expressao6, '|= é diferente')

# variaveis
nome= input('Qual o seu nome? ')
idade= input('Qual a sua idade? ')
idade = int(idade)
# Limite para pegar empréstimos
idade_limite = 18
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')