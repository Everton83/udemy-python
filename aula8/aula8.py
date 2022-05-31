"""
* Criar variaveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no a no atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Everton Pinheiro'
idade = 39
altura = 1.62
peso = 91.5
ano = 2022
ano_nasc = ano - idade
imc = peso / (altura ** 2)

print('Nome: {}, idade: {}, altura: {}m, peso: {}kg, nascido no ano de {}, esta com o IMC = {:.2f} no ano de {}'.format(nome,idade,altura,peso,ano_nasc,imc,ano))