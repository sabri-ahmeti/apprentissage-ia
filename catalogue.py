# Script : mon premier catalogue avec un dictionnaire

# Un dictionnaire : chaque info a une étiquette (une "clé")
tube_cuivre = {
    "nom": "Tube cuivre Ø18",
    "prix": 12.50,
    "fournisseur": "Tobler",
    "stock": 8
}

# J'accède à une info précise grâce à son étiquette :
print("Produit :", tube_cuivre["nom"])
print("Prix :", tube_cuivre["prix"], "CHF")
print("Fournisseur :", tube_cuivre["fournisseur"])
print("Stock actuel :", tube_cuivre["stock"])