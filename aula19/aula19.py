"""
while em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

#while True:
#    nome = input("Qual o seu nome? ")
#    print(f'Olá {nome}!')
#Print('Não executado.')

x=0
while x < 5:
    if x == 3:
        x = x + 1
        #continue # ira pular o 3 pois toda vez que tiver continue ele nao executa o codigo posterior a ele.
        break # ele encerra o laço
    print(x)
    x = x + 1
print('Acabou primeiro!')


x = 0 #coluna
while x < 10:
    y = 0 #linha
    while y <5:
        print(f'X vale {x} e Y vale {y}')
        y +=1
    print(x)
    x += 1 # # x = x + 1
print('Acabou segundo!')


# exemplo de calculudora

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]sim ou [n]não')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)

    if sair == 's':
        break