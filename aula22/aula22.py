"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

#for n in range(10):
#    print(n)

#for n in range(5, 10):
#    print(n)

#for n in range(20, 10, -1):
#    print(n)

#for n in range(0, 10, 2):
#    print(n)

#for n in range(100):
#    if n % 8 == 0:
#        print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)