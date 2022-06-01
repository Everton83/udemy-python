"""
Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteraveis
"""

#usando split
string = "O Brasil é o pais do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

#usando o join
string2 = 'O Brasil é penta.'
lista = string2.split(' ')
string3 = ','.join(lista)

print(string2)
print(lista)
print(string3)

#usando enumerate ele retorna em tupla
for indice, valor in enumerate(lista):
    print()
    print(indice, valor, lista[indice])