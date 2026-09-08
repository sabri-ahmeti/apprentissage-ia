# Défi : lire un lot d'emails et sortir un tableau structuré

import ollama
import json
import pandas as pd

emails = [
    "De: Mme Rossi. Bonjour, mon robinet de cuisine goutte, ce n'est pas pressé.",
    "De: M. Favre. URGENT ! Grosse fuite dans ma salle de bain, ça inonde !",
    "De: Jean Dubois. Je souhaite un devis pour rénover ma salle de bain le mois prochain.",
    "De: Sophie Blanc. Mon chauffe-eau ne produit plus d'eau chaude depuis hier soir, c'est gênant."
]

def analyser_email(email):
    try:
        reponse = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": f"""Voici un email : "{email}"
Extrais les informations et réponds UNIQUEMENT avec un JSON de cette forme, sans texte autour :
{{"expediteur": "...", "sujet": "...", "urgence": "haute ou normale"}}"""}
            ]
        )
        texte = reponse["message"]["content"]
        return json.loads(texte)
    except Exception as erreur:
        print("   ⚠️ Problème avec cet email :", erreur)
        return None
    
# On va accumuler les résultats dans cette liste
resultats = []

print("Analyse des emails en cours...\n")

# Pour chaque email, on l'analyse et on ajoute le résultat à la liste
for email in emails:
    infos = analyser_email(email)
    if infos is not None:
        resultats.append(infos)

# On crée un tableau Pandas à partir de tous les résultats
tableau = pd.DataFrame(resultats)

print("=== TABLEAU DES EMAILS ===")
print(tableau)