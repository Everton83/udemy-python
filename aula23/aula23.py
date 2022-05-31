"""
Listas em Python
fatiamento
append, insert, pop, del ,clear, extend, + , min, max, range
"""

#l1 = ['A', 'B', "C", 'D', 'E']
#l2 = [1, 2, 3, 4, 5, 11]
#l3 = ['K', 'L', "M", 'N', 'O', 12.5]
#l1.extend(l2) # exetend lista
#l2.append('b') # insere um valor no final da lista
#l3.insert(0, 'banana') # insere um valor na lista no indice especifico 0 = numero do indice + palavra a inserir
#l3.pop() # remove o ultimo elemento da lista
#del(l3[3:5]) # remove mais de um valor fatiados da lista atraves do indice
#del(l3[0]) # remove valores da lista atraves do indice
#print( "maximo da lista: ", max(l2) )
#print( "maximo da lista: ", min(l1) )

#l5 = list(range(0,21))
#l5.clear()
#print(l5)


#l6 = ['String', True, 10, -20.5]
#for elem in l6:
#    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzzz: a letra "{letra}" NÃO EXISTE na palavra secreta. ')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Que legal voce acertou!!! a palavra era {secreto_temp}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')
    print() # para pular uma linha

