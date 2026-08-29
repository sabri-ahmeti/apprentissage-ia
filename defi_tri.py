fichiers = ["facture1.pdf", "photo_chantier.jpg", "devis.pdf", "note.txt", "photo2.jpg", "facture2.pdf"]

nb_pdf = 0
nb_images = 0
nb_texte = 0


for fichier in fichiers:
    if fichier.endswith(".pdf"):
        nb_pdf = nb_pdf + 1
    elif fichier.endswith(".jpg"):
        nb_images = nb_images + 1
    elif fichier.endswith(".txt"):
        nb_texte = nb_texte + 1


print("Rapport de tri :")
print("- PDF :", nb_pdf, "fichiers")
print("- Images (jpg) :", nb_images, "fichiers")
print("- Texte (txt) :", nb_texte, "fichiers")   