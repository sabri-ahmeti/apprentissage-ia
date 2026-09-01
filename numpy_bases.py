# Script : découvrir NumPy

import numpy as np

# Une liste Python normale (ce que tu connais)
prix_liste = [100, 250, 80, 500]

# Un array NumPy (la "super-liste")
prix_array = np.array([100, 250, 80, 500])

print("Liste normale :", prix_liste)
print("Array NumPy   :", prix_array)

# LA DIFFÉRENCE : avec NumPy, on calcule sur TOUS les nombres d'un coup
prix_ttc = prix_array * 1.081

print("Prix TTC (tout d'un coup) :", prix_ttc)

# --- INDEXATION : aller chercher un nombre précis ---

stocks = np.array([8, 25, 4, 150, 12])

# Chaque nombre a une POSITION, qui commence à 0
print("Premier stock (position 0) :", stocks[0])
print("Troisième stock (position 2) :", stocks[2])
print("Dernier stock :", stocks[-1])

# Prendre une TRANCHE (du 2e au 4e)
print("Stocks position 1 à 3 :", stocks[1:4])

# --- FILTRAGE : la puissance de NumPy ---
# Trouver tous les stocks sous 10, en une ligne !
print("Stocks sous le seuil :", stocks[stocks < 10])
print("Test filtrage :", stocks[stocks < 10])
print("Test tranche 1:3 :", stocks[1:3])

# --- BROADCASTING : une opération sur tout l'array ---

stocks = np.array([8, 25, 4, 150, 12])

# Ajouter 5 à chaque stock (réappro de 5 unités partout)
print("Après +5 partout :", stocks + 5)

# Doubler tous les stocks
print("Stocks doublés :", stocks * 2)

# Comparer : True/False pour chaque élément
print("Sous le seuil ? :", stocks < 10)