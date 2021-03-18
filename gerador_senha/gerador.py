import random
import string

# Agrupa todos os caracteres #
grupo = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

# Definindo o tamanho da senha #
tam = int(input("Digite o tamanho de sua senha para ser gerada: "))

# Gera senha #
ger_senha = "".join(random.sample(grupo, tam))

print(f'Sua senha é: {ger_senha}')