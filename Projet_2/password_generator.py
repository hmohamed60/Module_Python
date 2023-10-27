import random
import string

def generate_password(length, lowercase_count, uppercase_count, digit_count, special_count):
    # Vérifiez si la somme des compteurs n'excède pas la longueur du mot de passe
    total_count = lowercase_count + uppercase_count + digit_count + special_count
    if total_count > length:
        print("La somme des compteurs dépasse la longueur du mot de passe.")
        return None

    # Générez les caractères de chaque catégorie
    lowercase_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(lowercase_count))
    uppercase_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase_count))
    digit_chars = ''.join(random.choice(string.digits) for _ in range(digit_count))
    special_chars = ''.join(random.choice(string.punctuation) for _ in range(special_count))

    # Complétez la liste pour atteindre la longueur souhaitée
    remaining_chars = length - total_count
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    all_chars += ''.join(random.choice(all_chars) for _ in range(remaining_chars))

    # Mélangez les caractères pour obtenir un mot de passe aléatoire
    all_chars = list(all_chars)
    random.shuffle(all_chars)

    return ''.join(all_chars)
