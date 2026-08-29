# Script : les compréhensions de listes

prix_ht = [100, 250, 80, 500, 45]

# --- L'ANCIENNE FAÇON (avec une boucle) ---
prix_ttc_ancien = []
for prix in prix_ht:
    prix_ttc_ancien.append(prix * 1.081)

print("Ancienne façon :", prix_ttc_ancien)

# --- LA NOUVELLE FAÇON (compréhension de liste, en 1 ligne) ---
prix_ttc_nouveau = [prix * 1.081 for prix in prix_ht]

print("Nouvelle façon :", prix_ttc_nouveau)