# Importation des modules nécessaires
import random
import string
import math
from passphrase_generator import generate_random_passphrase  # Importer le générateur de passphrase
from password_generator import generate_password  # Importer le générateur de mot de passe
from password_tester import test_password_strength  # Importer le testeur de force de mot de passe

def main():
    while True:
        # Affichage du menu principal
        print("1. Générateur de mot de passe")
        print("2. Testeur de mot de passe")
        print("3. Générateur de passphrase")
        print("4. Recommencer")
        print("5. Quitter")
        choice = input("Choisissez une option (1/2/3/4/5): ")

        if choice == '1':
            # Nous recueillons les critères pour la génération de mot de passe
            password_length = int(input("Longueur du mot de passe : "))
            lowercase_count = int(input("Nombre de minuscules : "))
            uppercase_count = int(input("Nombre de majuscules : "))
            digit_count = int(input("Nombre de chiffres : "))
            special_count = int(input("Nombre de caractères spéciaux : "))
            password = generate_password(password_length, lowercase_count, uppercase_count, digit_count, special_count)
            print(f"Mot de passe généré : {password}")

        elif choice == '2':
            # Nous demandons à l'utilisateur d'entrer un mot de passe à tester
            password = input("Entrez le mot de passe à tester : ")
            entropy, strength = test_password_strength(password)
            print(f"Entropie du mot de passe : {entropy}")
            print(f"Force du mot de passe : {strength}")

        elif choice == '3':
            # Nous demandons le nombre de mots pour la génération de passphrase
            num_words = int(input("Nombre de mots dans la passphrase : "))
            passphrase = generate_random_passphrase(num_words)
            print(f"Votre passphrase générée est : {passphrase}")

        elif choice == '4':
            # Option pour recommencer le programme
            continue

        elif choice == '5':
            # Option pour quitter le programme
            print("Au revoir !")
            break  # Met fin au programme

        else:
            # Gestion de l'option invalide
            print("Option invalide. Veuillez choisir une option valide (1/2/3/4/5).")

if __name__ == "__main__":
    main()
