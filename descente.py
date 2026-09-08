# Script : descente de gradient à la main
# Le cœur de l'apprentissage des IA

# On veut trouver le point le plus bas de la fonction : f(x) = (x - 3)²
# La réponse évidente est x = 3 (là, la fonction vaut 0, son minimum).
# Mais on va laisser l'ordinateur le TROUVER tout seul, comme une IA.

# La fonction (la "colline")
def f(x):
    return (x - 3) ** 2

# La dérivée (la "pente" sous nos pieds)
def derivee(x):
    return 2 * (x - 3)

# --- LA DESCENTE DE GRADIENT ---

x = 0.0              # on démarre au hasard, à x = 0
pas = 0.1            # la taille de nos pas (le "learning rate")

print("Départ : x =", x, " | erreur =", f(x))

# On fait 20 pas vers le bas
for etape in range(20):
    pente = derivee(x)        # dans quel sens ça descend ?
    x = x - pas * pente       # on fait un pas dans ce sens
    print(f"Étape {etape+1} : x = {round(x, 3)} | erreur = {round(f(x), 3)}")

print("\nRésultat final : x =", round(x, 3), "(la vraie réponse est 3)")