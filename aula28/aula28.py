"""
Operador ternário em Python
"""

logged_user = False

if logged_user:
    msg = 'Ola voec esta logado'
else:
    msg = 'usuário Precisa logar'
print(msg)

msg = 'Usuário Logado(ternario).' if (logged_user) else 'Usuário precisa logar(ternario)'
print(msg)

idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Voce tem que digiatar somente numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    print(msg)