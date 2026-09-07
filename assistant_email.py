# Script robuste : analyser un email et extraire les infos en JSON
# La première vraie brique de l'assistant RNSA

import ollama
import json


def analyser_email(email):
    """Prend un email, renvoie les infos structurées (ou None si erreur)."""
    try:
        # 1. On demande à l'IA d'extraire les infos en JSON
        reponse = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": f"""Voici un email de client : "{email}"
Extrais les informations et réponds UNIQUEMENT avec un JSON de cette forme, sans aucun texte autour :
{{"nom_client": "...", "probleme": "...", "urgence": "haute ou normale"}}"""}
            ]
        )
        texte = reponse["message"]["content"]

        # 2. On transforme le JSON en dictionnaire Python
        infos = json.loads(texte)
        return infos

    except json.JSONDecodeError:
        # Si l'IA n'a pas renvoyé un JSON valide
        print("   ⚠️ L'IA n'a pas renvoyé un JSON correct.")
        return None
    except Exception as erreur:
        # Si autre chose plante (connexion, etc.)
        print("   ⚠️ Un problème est survenu :", erreur)
        return None


# --- TEST sur un email ---
email_test = "Bonjour, je suis M. Martin. Mon chauffe-eau ne marche plus, j'ai besoin d'une intervention rapide."

print("Analyse de l'email...")
resultat = analyser_email(email_test)

if resultat is not None:
    print("✅ Client :", resultat["nom_client"])
    print("✅ Problème :", resultat["probleme"])
    print("✅ Urgence :", resultat["urgence"])
else:
    print("❌ Impossible d'analyser cet email.")

# --- TEST SUR PLUSIEURS EMAILS (comme une vraie boîte mail) ---

emails = [
    "Bonjour, Mme Rossi à l'appareil. Mon robinet de cuisine goutte, ce n'est pas urgent.",
    "URGENT !! M. Favre, fuite d'eau importante dans ma salle de bain, ça inonde !",
    "Salut, c'est Jean. Je voudrais un devis pour rénover ma salle de bain le mois prochain."
]

print("\n\n=== TRAITEMENT DE PLUSIEURS EMAILS ===")

for numero, email in enumerate(emails, start=1):
    print(f"\n--- Email {numero} ---")
    resultat = analyser_email(email)
    if resultat is not None:
        print("Client :", resultat["nom_client"])
        print("Problème :", resultat["probleme"])
        print("Urgence :", resultat["urgence"])
    else:
        print("Cet email n'a pas pu être analysé.")