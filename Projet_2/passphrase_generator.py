import random

class PassphraseGenerator:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def generate_passphrase(self, num_words):
        passphrase = []
        for _ in range(num_words):
            dice_rolls = [random.randint(1, 6) for _ in range(5)]
            dice_number = self.dice_to_number(dice_rolls)
            word = self.wordlist[dice_number]
            passphrase.append(word)
        return ' '.join(passphrase)

    @staticmethod
    def dice_to_number(dice_rolls):
        dice_string = ''.join(map(str, dice_rolls))
        return int(dice_string, 6) - 1

# Charger la liste de mots depuis le fichier EFF_Wordlist.txt
def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        wordlist = file.read().splitlines()
    return wordlist

if __name__ == "__main__":
    # Charger la liste de mots depuis le fichier EFF_Wordlist.txt
    passphrase_wordlist = load_wordlist('EFF_Wordlist.txt')

    # Créer une instance du générateur de passphrase
    generator = PassphraseGenerator(passphrase_wordlist)

    num_words = int(input("Nombre de mots dans la passphrase : "))
    passphrase = generator.generate_passphrase(num_words)
    print(f"Votre passphrase générée est : {passphrase}")

