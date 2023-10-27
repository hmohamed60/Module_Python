import password_generator
import password_tester
from passphrase_generator import PassphraseGenerator



def main():
    print("1. Générateur de mot de passe")
    print("2. Testeur de mot de passe")
    print("3. Générateur de passphrase")
    choice = input("Choisissez une option (1/2/3): ")

    if choice == '1':
        password_length = int(input("Longueur du mot de passe : "))
        lowercase_count = int(input("Nombre de minuscules : "))
        uppercase_count = int(input("Nombre de majuscules : "))
        digit_count = int(input("Nombre de chiffres : "))
        special_count = int(input("Nombre de caractères spéciaux : "))
        password = password_generator.generate_password(password_length, lowercase_count, uppercase_count, digit_count, special_count)
        print(f"Mot de passe généré : {password}")

    elif choice == '2':
        password = input("Entrez le mot de passe à tester : ")
        entropy, strength = password_tester.test_password_strength(password)
        print(f"Entropie du mot de passe : {entropy}")
        print(f"Force du mot de passe : {strength}")
    
    elif choice == '3':
        num_words = int(input("Nombre de mots dans la passphrase : "))
        generator = PassphraseGenerator(passphrase_generator.passphrase_wordlist)
        passphrase = generator.generate_passphrase(num_words)
        print(f"Votre passphrase générée est : {passphrase}")
        # Pas besoin de vérifier la taille de la liste ici

if __name__ == "__main__":
    main()
