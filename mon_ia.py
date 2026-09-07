# Script : faire répondre l'IA en JSON structuré

import ollama
import json

# Un email de client (exemple)
email = "Bonjour, je suis M. Dupont. Ma douche fuit depuis ce matin, c'est urgent. Pouvez-vous venir vite ?"

# On demande à l'IA d'extraire les infos EN JSON
reponse = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": f"""Voici un email de client : "{email}"
Extrais les informations et réponds UNIQUEMENT avec un JSON de cette forme, sans aucun texte autour :
{{"nom_client": "...", "probleme": "...", "urgence": "haute ou normale"}}"""}
    ]
)

# On récupère le texte de la réponse
texte = reponse["message"]["content"]
print("Réponse brute de l'IA :")
print(texte)

# On transforme le JSON en dictionnaire Python utilisable
infos = json.loads(texte)
print("\n--- Infos extraites (utilisables par le programme) ---")
print("Client :", infos["nom_client"])
print("Problème :", infos["probleme"])
print("Urgence :", infos["urgence"])