"""
Desempacotamento de listas
"""
lista = ['Luiz', 'João', 'Maria']

n1, n2, *outra_lista = lista

n1, n2, *_ = lista
print(n2)