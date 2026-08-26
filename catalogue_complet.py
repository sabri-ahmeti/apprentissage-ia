# Script : un vrai mini-catalogue RNSA

# Une liste de dictionnaires : plusieurs produits, chacun avec ses infos
catalogue = [
    {"nom": "Tube cuivre Ø18", "prix": 12.50, "stock": 8},
    {"nom": "Coude 90°", "prix": 3.20, "stock": 25},
    {"nom": "Vanne d'arrêt", "prix": 18.90, "stock": 4},
    {"nom": "Joint fibre", "prix": 0.80, "stock": 150}
]

seuil = 10

print("=== ÉTAT DU CATALOGUE ===")

for produit in catalogue:
    print(produit["nom"], "- Prix:", produit["prix"], "CHF - Stock:", produit["stock"])
    if produit["stock"] < seuil:
        print("   >>> ALERTE : à commander !")

print("=== FIN ===")