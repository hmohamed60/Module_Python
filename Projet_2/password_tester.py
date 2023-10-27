import math

def calculate_entropy(password):
    character_count = len(set(password))
    entropy = len(password) * math.log2(character_count)
    return entropy

def test_password_strength(password):
    entropy = calculate_entropy(password)
    if entropy < 64:
        strength = "Très faible"
    elif entropy < 80:
        strength = "Faible"
    elif entropy < 100:
        strength = "Moyen"
    else:
        strength = "Fort"
    return entropy, strength
