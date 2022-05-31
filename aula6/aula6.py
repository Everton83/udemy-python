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