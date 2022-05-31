"""
For / Else
"""

lista = ['AEverton Pinheiro', 'Maria', 'Suelen', 'Livia']

for valor in lista:
    if valor.lower().startswith('e'):
 #       print(f'Existe uma palavra com a letra {valor}')
#        break
        continue
    print(f'Existe uma palavra com a letra {valor}')
else:
    print('Não existe uma palavra que começa com E.')

#for valor in lista:
#    if valor.startswith('E'):
#        print('começa com E', valor)
#    else:
#        print('não comeca com E')

