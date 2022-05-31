"""
Iniciar com letra, pode conter numeros, separar _, letras minusculas
"""
nome = 'Everton Pinheiro'
idade = 37
altura = 1.62
e_maior = idade > 18
peso = 91
#imc = 'temp'
imc = (peso / (altura ** 2))

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome,idade,imc))
