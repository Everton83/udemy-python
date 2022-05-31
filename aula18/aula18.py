"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em :
https://docs.pythin.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""

# positivos [012345678]
# negativos -[987654321]
texto = 'Python_s2'

nova_string = texto[2:6]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[0:6:2]
print(nova_string)

nova_string = texto[0::3]
print(nova_string)
