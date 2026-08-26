# Script du jour : ma première fonction

def calculer_marge(prix_achat, prix_vente):
    marge = prix_vente - prix_achat
    return marge

# Maintenant j'utilise ma fonction plusieurs fois :
marge1 = calculer_marge(800, 1200)
marge2 = calculer_marge(1500, 2300)
marge3 = calculer_marge(200, 350)

print("Marge du devis 1 :", marge1, "CHF")
print("Marge du devis 2 :", marge2, "CHF")
print("Marge du devis 3 :", marge3, "CHF")
