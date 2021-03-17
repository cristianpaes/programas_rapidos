import requests
import json

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

ct = input("Digite o País que deseja saber os dados: ")
querystring = {"country":"ct"}

headers = {
    'x-rapidapi-key': "XXXXXXX",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

dados = json.loads(response.text)

print(dados['data'])