from database import Database
from personne import Personne

db = Database('moun.db')

while True:
    choix = input("Voulez-vous lire, écrire ou quitter le programme ? (l/e/q) ")

    if choix == 'e':
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prénom : ")
        age = int(input("Entrez votre âge : "))
        ville = input("Entrez votre ville : ")
        personne = Personne(nom, prenom, age, ville)
        db.ajouter_personne(personne)
        print("Les informations ont été sauvegardées avec succès dans la base de données 'personnes.db'.")

    elif choix == 'l':
        personnes = db.recuperer_personnes()
        for personne in personnes:
            print("Nom =", personne.nom)
            print("Prénom =", personne.prenom)
            print("Âge =", personne.age)
            print("Ville =", personne.ville)
            print("--------------------")
        print("Les informations ont été récupérées avec succès depuis la base de données 'personnes.db'.")

    elif choix == 'q':
        db.fermer_connexion()
        break

    else:
        print("Erreur : choix incorrect. Veuillez entrer 'l' pour lire, 'e' pour écrire ou 'q' pour quitter le programme.")

print("Fin du programme.")
