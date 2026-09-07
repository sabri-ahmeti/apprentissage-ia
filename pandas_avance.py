# Script : Pandas avancé - croiser deux tableaux (merge)

import pandas as pd

# --- TABLEAU 1 : ton catalogue (les prix) ---
catalogue = pd.DataFrame({
    "produit": ["Tube cuivre Ø18", "Coude 90°", "Vanne d'arrêt", "Joint fibre"],
    "prix": [12.50, 3.20, 18.90, 0.80]
})

# --- TABLEAU 2 : une commande d'un chantier (les quantités) ---
commande = pd.DataFrame({
    "produit": ["Tube cuivre Ø18", "Vanne d'arrêt", "Coude 90°"],
    "quantite": [10, 2, 6]
})

print("=== CATALOGUE ===")
print(catalogue)
print("\n=== COMMANDE ===")
print(commande)

# --- LE MERGE : croiser la commande avec le catalogue ---
devis = pd.merge(commande, catalogue, on="produit")

print("\n=== DEVIS (commande + prix retrouvés) ===")
print(devis)

# --- CALCULER LE TOTAL DU DEVIS ---

# Une nouvelle colonne : prix × quantité pour chaque ligne
devis["total_ligne"] = devis["prix"] * devis["quantite"]

print("\n=== DEVIS AVEC TOTAUX PAR LIGNE ===")
print(devis)

# Le total général du devis
total_devis = devis["total_ligne"].sum()
print("\n💰 TOTAL DU DEVIS :", total_devis, "CHF")