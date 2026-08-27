# Script : écrire et lire un journal de dépenses

# --- PARTIE 1 : écrire dans un fichier ---
fichier = open("depenses.txt", "w")

fichier.write("Chantier Dupont - Tubes cuivre - 250 CHF\n")
fichier.write("Chantier Dupont - Coudes 90 - 45 CHF\n")
fichier.write("Chantier Martin - Vanne d'arret - 90 CHF\n")

fichier.close()

print("Le journal de dépenses a été enregistré !")

# --- PARTIE 2 : relire le fichier ---
print("\n=== CONTENU DU JOURNAL ===")

fichier = open("depenses.txt", "r")
contenu = fichier.read()
fichier.close()

print(contenu)
