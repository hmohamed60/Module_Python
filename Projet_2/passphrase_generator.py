import random

word_list = ["chien", "chat", "maison", "soleil", "ordinateur", "pizza", "fleur", "plage", "montagne", "arc-en-ciel"]

def generate_random_passphrase(num_words):
    # On genere une passphrase aléatoire en sélectionnant des mots au hasard dans notre liste
    passphrase = [random.choice(word_list) for _ in range(num_words)]
    return ' '.join(passphrase)
