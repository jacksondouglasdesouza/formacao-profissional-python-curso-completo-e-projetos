#Fundamentos de Python
# Principais Variáveis

# int() <<< Tipos de Variáveis
# float() <<< Tipos de Variáveis
# bool() <<< Tipos de Variáveis
# str() <<< Tipos de Variáveis

# Não pode usar variáveis com caracteres especiais;
# Números só pode ser usado depois da inicial, não sendo possível criar uma variável iniciando com um número;
# Usa-se pela comunidade python o estilo snake case: snake_case | casa_farinha ... etc;

#INT
numero_inteiro = 300
#FLOAT
numero_float = 300.55
#BOOLEANO
verdadeiro = True
falso = False
#TEXTOS - STRING - STR
strs = "Essa é uma vadeia de string"

print(f'Esse é um número inteiro = {numero_inteiro}')
print(f'Esse é um número float = {numero_float}')
print(f'Esse é um boleano verdadeiro = {verdadeiro}')
print(f'Esse é um boleano falso = {falso}')
print(f'Esse é uma cadeia de estring = {strs}')


#Tipos de Declaração de variáveis

# padrão camel case
saldoBancario = 100

# padrão pascal case
SaldoBancario = 200

# padrão snake case  <<<< Essa por padrão global recomenda-se usar!
saldo_bancario = 300

print(f'Saldo 01 - padrão camel case [ {saldoBancario} ]')
print((f'Saldo 02 - padrão pascal case [ {SaldoBancario} ]'))
print(f'Saldo 03 - padrão snake case [ {saldo_bancario} ]')

# ATIVIDADE 02

#1 - Crie uma variável de cada tipo e ponha alguma valor escolhido.
#Em seguida, printe todos esses valores.

variavel_tipo_inteiro = 1550
variavel_tipo_float = 2500.989
variavel_tipo_str = "Nessa casa de pão de queijos, o atendimento é muito ruim!"
variavel_tipo_boolean_verdadeiro = True
variavel_tipo_boolean_falsa = False

print(f'Essa variável é do tipo inteiro: [ {variavel_tipo_inteiro} ]')
print(f'Essa variável é do tipo Float: [ {variavel_tipo_float} ]')
print(f'Essa variável é do tipo str: [ {variavel_tipo_str} ]')
print(f'Essa variável é do tipo boolean VERDADEIRO: [ {variavel_tipo_boolean_verdadeiro} ]')
print(f'Essa variável é do tipo FALSO: [ {variavel_tipo_boolean_falsa} ]')

#--

#2 - Crie variáveis para guardar seu nome, CPF e uma que indique
# se você esta casado, em seguida printe esses valores separadamente,
# mas não esqueça de printar junto o que eles significam.

meu_nome_completo = "Jackson Douglas de Souza"
meu_cpf = 36925874132
sou_casado = False

print("\n")
print(f'Meu nome completo é {meu_nome_completo} [´* Essa é uma variável do tipo str() ]')
print(F'Meu CPF é : {meu_cpf} [ * Essa é uma variável do tipo int() ]')
print(f'É verdade que eu sou casado? [ {sou_casado} [ * Essa é uma variável do tipo bool() ]')

#--



