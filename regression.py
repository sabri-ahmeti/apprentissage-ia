# Script : régression linéaire - prédire le temps d'un chantier

import numpy as np
from sklearn.linear_model import LinearRegression

# --- NOS DONNÉES (chantiers passés) ---
# Nombre d'appareils à poser
appareils = np.array([[2], [4], [6], [8], [10]])
# Temps que ça a pris (en heures)
temps = np.array([3, 5, 8, 10, 13])

# --- ON CRÉE ET ENTRAÎNE LE MODÈLE ---
modele = LinearRegression()
modele.fit(appareils, temps)

print("Le modèle a appris !")

# --- ON PRÉDIT pour un nouveau chantier ---
nouveau_chantier = np.array([[5]])   # 5 appareils
prediction = modele.predict(nouveau_chantier)

print("Pour 5 appareils, temps estimé :", round(prediction[0], 1), "heures")

# On teste plusieurs cas d'un coup
for nb in [3, 7, 12]:
    p = modele.predict(np.array([[nb]]))
    print(f"Pour {nb} appareils → environ {round(p[0], 1)} heures")

# --- REGARDER CE QUE LE MODÈLE A APPRIS ---

print("\n--- Sous le capot ---")
print("Pente (par appareil) :", round(modele.coef_[0], 2), "heures/appareil")
print("Point de départ :", round(modele.intercept_, 2), "heures")