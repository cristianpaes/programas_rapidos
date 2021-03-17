import random

# Caracteres usados para formar senhas #
let_minus = 'abcdefghijklmnopqrstuvwxyz'
let_maius = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numer = '0123456789'
caract = '#@$%&*-=+!'

# Agrupa todos os caracteres #
grupo = let_minus + let_maius + numer + caract

# Definindo o tamanho da senha #
tam = int(input("Digite o tamanho de sua senha para ser gerada: "))

# Gera senha #
ger_senha = "".join(random.sample(grupo, tam))

print(f'Sua senha é: {ger_senha}')