# Script : découvrir Pandas et les DataFrames

import pandas as pd

# Un DataFrame : un tableau avec des colonnes nommées (comme un mini-Excel)
catalogue = pd.DataFrame({
    "produit": ["Tube cuivre Ø18", "Coude 90°", "Vanne d'arrêt", "Joint fibre"],
    "prix": [12.50, 3.20, 18.90, 0.80],
    "stock": [8, 25, 4, 150]
})

# Afficher tout le tableau
print("=== MON CATALOGUE ===")
print(catalogue)


# --- ACCÉDER À UNE COLONNE ---
print("\nLes prix :")
print(catalogue["prix"])

# --- FILTRER : les produits sous le seuil de stock ---
print("\nProduits à commander (stock < 10) :")
print(catalogue[catalogue["stock"] < 10])

# --- CALCULER : valeur totale du stock ---
catalogue["valeur"] = catalogue["prix"] * catalogue["stock"]
print("\nAvec la valeur de chaque ligne :")
print(catalogue)

print("\nValeur totale du stock :", catalogue["valeur"].sum(), "CHF")


# --- GROUPBY : regrouper et calculer par catégorie ---

# Un tableau de dépenses par chantier
depenses = pd.DataFrame({
    "chantier": ["Dupont", "Dupont", "Martin", "Dupont", "Martin"],
    "article": ["Tubes", "Coudes", "Vanne", "Joints", "Chauffe-eau"],
    "montant": [250, 45, 90, 30, 800]
})

print("\n=== TOUTES LES DÉPENSES ===")
print(depenses)

# Regrouper par chantier et additionner les montants
total_par_chantier = depenses.groupby("chantier")["montant"].sum()

print("\n=== TOTAL PAR CHANTIER ===")
print(total_par_chantier)