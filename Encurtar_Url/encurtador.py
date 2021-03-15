import pyshorteners

urldigitada = input(str("Digite a URL para ser encurtada: "))

# Carrega lib #
carrega = pyshorteners.Shortener()

Urlcurta = carrega.tinyurl.short(urldigitada)

print(f"URL Encurtada: {Urlcurta}")