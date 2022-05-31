"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = input('Digite um numero: ')
    numero = int(numero)
    resultado = numero % 2
    if resultado == 0:
        print('o numero é par')
    else:
        print('o numero é impar')
except:
    print(f'Este numero {numero} não é um numero inteiro')


"""
Faça um progama que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horario = input('Digite um horario (0-23): ')

    if horario.isdigit():
        horario = int(horario)

        if horario < 0 or horario > 23:
            print('Horário deve estar entre 0 e 23')
        else:
            if horario <= 11:
                print('Bom dia')
            elif horario <= 17:
                print('Boa tarde')
            else:
                print('Boa noite')
    else:
        print('Por favor digite um horario das (0-23)')
except:
    print('ERROR')

"""
Faça um progama que peça o primeiro nome do usuário. se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite o seu primeiro nome: ')
qtd_caracteres = len(nome)

if qtd_caracteres <= 4:
    print('Seu nome é curto')
elif qtd_caracteres == 5 or qtd_caracteres == 6:
    print('Seu nome é normal')
elif qtd_caracteres > 6:
    print('Seu nome é muito grande')
else:
    print('ERROR')