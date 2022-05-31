"""
Entrada de dados
"""

nome = input("Qual seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = 2022-int(idade)

print() #quebra uma linha
print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu em {ano_nascimento}.')


# convertendo inputs pois o input sempre  retorna uma string
numero_1 = int(input('Digite um numero: ')) # primeira maneira
numero_2 = input('Digite um numero: ')
numero_2 = int(numero_2)# segunda maneira

print()
print( numero_1 ** numero_2 )