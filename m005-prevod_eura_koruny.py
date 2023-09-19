import requests
data = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json").json()
rate = data["eur"]["czk"]
euros = float(input("Zadaj počet eur: "))
print(f"{euros}€ je {round(euros * rate, 2)} korún")
koruna = float(input("Zadaj počet korún: "))
print(f"{koruna} korún je {round(koruna/rate, 2)}€")
