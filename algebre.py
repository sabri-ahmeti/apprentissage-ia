# Script : algèbre linéaire de base avec NumPy

import numpy as np

# --- UN VECTEUR : juste une liste de nombres ---
v = np.array([3, 5, 2])
print("Mon vecteur :", v)

# On peut faire des opérations dessus (comme tu l'as vu avec NumPy)
print("Vecteur × 2 :", v * 2)
print("Somme des éléments :", v.sum())

# --- ADDITIONNER DEUX VECTEURS ---
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("\na + b :", a + b)

# --- LE PRODUIT SCALAIRE : mesurer la "ressemblance" ---

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])   # identique à a
c = np.array([9, 0, 1])   # très différent de a
print("a . a (identiques) :", np.dot(a, a))
print("a . b (identiques) :", np.dot(a, b))
print("a . c (différents) :", np.dot(a, c))

# --- UNE MATRICE : un tableau de nombres (lignes + colonnes) ---

matrice = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMa matrice :")
print(matrice)

print("\nSa forme (lignes, colonnes) :", matrice.shape)
print("Le nombre en ligne 0, colonne 2 :", matrice[0, 2])