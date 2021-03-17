import requests as Req

# Não transformar a entrada de dados em número #
cep = input("Digite o CeP para consulta: ")

# Consultando as informações do CEP #
url = f'http://viacep.com.br/ws/{cep}/json'

# Armazenando as informações #
endereco = Req.get(url).json()

# Coletando as informações do Json#
logra = endereco['logradouro']
bairro = endereco['bairro']
cidade = endereco['localidade']

print(f'Seu CEP: {cep} esta localizado na {logra}, no bairro: {bairro}, na cidade {cidade}')