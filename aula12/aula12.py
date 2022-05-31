"""
Operadores Lógicos
and, or, not
in e not in
"""
# (Verdadeiro e Vedadeiro) = True | (Verdadeiro e Falso) = False
# comparação and comapracao

# Verdadeiro OU Verdadeiro
# comparacao or comparacao

# not conheico com inerson

a = 2
b = 0
c = 3
d = 'srawrsrsrs'

if  c > a:
    print ('C é maior que A')
else:
    print('A é maior que C')

if not b:
    print ('preencha o valor de B')
if not d:
    print ('preencha o valor de D')

nome = 'Everton Pinheiro'

if 'v' in nome:
    print('Existe a letra v no seu nome')
else:
    print('Não existe')

if 'sewsese' in nome:
    print('Existe a letra v no seu nome')
else:
    print('Não existe')


if 'v' not in nome:
    print('não existe o texto')
else:
    print('Existe o texto')

if 'sewsese' not in nome:
    print('não existe o texto')
else:
    print('Existe o texto')


usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Everton'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha incorreto')

num_1 = 2
num_2 = 1

if num_1 != num_2:
    print('num_1 é igual a num_2')