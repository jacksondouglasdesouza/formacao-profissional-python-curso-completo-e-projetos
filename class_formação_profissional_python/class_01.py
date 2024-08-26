#Fundamentos de Python
# Comentários e Método Print

#Este é um comentário de uma única linha!

'''
Esse é um comentário em Blocos
Assim é possível comentar variás linhas
sem que o interpretador não execute
essas linhas no código!
'''


print("Olá Galera, vamos começar Python para IA - metendo bronca no código!")
print(10 + 10)
print(8 - 2)
print(10 * 2)
print(10 / 2)

print("Maça", "Pera", end=" Fim...", sep=" * ")
print("Este texto vai ter uma quebra de linha \n"
      "Agora estou na próxima linha! \n"
      "Aqui também!")

#Variáveis no print

fruta_a = "Maçã"
fruta_b = "Banana"
fruta_c = "Limão"

print(f'Essa é a frutra 1 [ {fruta_a} ], essa é a fruta 2 [ {fruta_b} ], essa é a fruta 3 [ {fruta_c} ] ')

# ATIVIDADE 01

#1 - Realize o print do seu nome completo, sua idade e sua
# altura utilizando um print para cada valor.

nome_completo = "Jackson Douglas de Souza"
idade = 37
altura = 1.90

print("\n")
print(f'Mue nome completo é: [ {nome_completo} ]')
print(f'Minha idade é: [ {idade} ]')
print(f'Minha Altura é: [ {altura} ]')

#--

#2 - Realize o print do seu nome completo, sua idade e sua altura
# utilizando apenas um print para todos valores.

print(f'Meu nome completo é {nome_completo}, eu tenho {idade} anos e minha altura é {altura}')

#3 - Realize o print de 3 números de sua escolha em um mesmo print,
# mas separados pelo caracter '-'.

print(123, 456, 789, end=" Fim ... \n", sep=" - ")
print(101112, 131415, 161718, end=" Fim ... \n", sep=" - ")
print(192021, 222324, 252627, end=" Fim ... \n", sep=" - ")


