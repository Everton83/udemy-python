"""
Contando carcateres com len
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print(usuario, qtd_caracteres, type(qtd_caracteres))
    print('Voce foi cadastrado no sistema')
else:
    print('Voce precisa digitar pelo menos de 6 caracteres')

