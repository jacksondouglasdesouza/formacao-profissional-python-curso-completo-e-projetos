#Fundamentos de Python
# Formatações Especiais para texto
#Técnicas de Formatação de Texto
# %s - texto | %d - inteiro | %f - real

nome = "Carolina"
texto_formatado = 'O nome dela é %s ' % nome
print(f'Aqui está o texto formatado = [ {texto_formatado} ]')

#--

nome_usuario = "Rodrigão"
idade_usuario = 23
altura_usuario = 1.73
texto_informacoes_usuario = "O nome do usuário é %s. O usuário tem %d anos. O usuário tem %f de altura." % (nome_usuario, idade_usuario, altura_usuario)

print(texto_informacoes_usuario)

#--

numero_gigante = 12.58976524589752

print("Número gigante formatado: %.2f " % numero_gigante)
print("Número gigante formatado: %.3f " % numero_gigante)
print("Número gigante formatado: %.4f " % numero_gigante)
print("Número gigante formatado: %.5f " % numero_gigante)
print("Número gigante real: %f " % numero_gigante)

#-- Formatando variáveis do tipo boolean

value_verdadeiro = True
value_false = False

print(f'Valores sem formação: {value_verdadeiro}')
print(f'Valores sem formação: {value_false}')

print("\n")

print("Valores com formação: %s" % value_verdadeiro)
print("Valores com formação: %d" % value_verdadeiro)
print("Valores com formação: %.1f" % value_verdadeiro)

#--
print("\n")
print("Valores com formação: %s" % value_false)
print("Valores com formação: %d" % value_false)
print("Valores com formação: %.1f" % value_false)

#--

# Formação de texto com caractperes especiais!

print("\n")
texto_fomatacao_caracteres_uma_quebra_linha = ('Assim o texto tera somente uma quebra de linha \n'
                                               'Logo ficara indentado a esquerda da tela\n'
                                               'Você consegue entender?\n')
resposta_usuario = True

print(texto_fomatacao_caracteres_uma_quebra_linha)
print(f'>>> Possivel que sim [ {resposta_usuario} ]')

print("\n")
texto_fomatacao_caracteres_uma_quebra_mais_tabulacao = ("Assim o texto tera uma quebra de linha na primeira \n\t"
                                                        "Logo na segunda terá uma tabulação mais uma quebra de linha \n\t\t"
                                                        "Logo na tereira linha haverá duas tabulações e outra quebra de linha!\n\t\t\t"
                                                        "Logo a quarta linha tera trÊs tabulações e uma quebra de linha!!!\n\t\t\t\t"
                                                        "Conseguio Entender?")

print(texto_fomatacao_caracteres_uma_quebra_mais_tabulacao)

resposta_usuario = False

print("\n")
print(f'Possivel que não [ {resposta_usuario} ]')


aspas_simples_dentro_de_aspas_simples = 'Logo que você chegar no mc Donald\'s me ligha! Combinado?'

print(aspas_simples_dentro_de_aspas_simples)


# ATIVIDADE 03


# 1 - Escreva e formate a data em que você nasceu no formato dia/mês/ano.
# Não esqueça de criar 3 variáveis para guardar o dia, mês e ano.

dia_nascimento = 13
mes_nascimento = 12
ano_nascimento = 1985

informacoes_formatadas = f'Data de nascimento com formatação especial:  {dia_nascimento}/{mes_nascimento}/{ano_nascimento}'
print(">>>>>>>>>>><<<<<<<<<")
print(informacoes_formatadas)
print(">>>>>>>>>>><<<<<<<<<")

# 2 - Escreva e formate a hora e minuto atual.
# Não esqueça de criar duas variáveis para guardar a hora e minuto.

hora_atual = "16"
minuto_atual = "32"

print(f'São exatamente [ {hora_atual}:{minuto_atual} ]')


# 3 - Escreva um programa que contêm o número PI, que deve ter o valor exato
# de 3.14159265359. Agora formate esse número para ter apenas cinco casas decimais.

PI = 3.14159265359

print('O número PI é um número iracional que vale: %f' % PI)
print('Também é possível escrever o número PI com poucas casas decimais como por exeplo:  \n\t'
      'Com 2 casas decimais = %.2f\n\t'
      'Com 3 casas decimais = %.3f\n\t'
      'Com 4 casas decimais = %.4f\n\t'
      'Com 5 casas decimais = %.5f\n\t' % (PI, PI, PI, PI))

