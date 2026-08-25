# Script 4 : vérifier automatiquement plusieurs stocks

stocks = [3, 12, 7, 20, 5]
seuil = 10

print("Vérification automatique des stocks :")

for quantite in stocks:
    if quantite < seuil:
        print("Stock de", quantite, "-> ALERTE : commander !")
    else:
        print("Stock de", quantite, "-> OK")

print("Vérification terminée.")
