import math

def calculate_entropy(password):
    # Nous calculons le nombre de caractères uniques dans le mot de passe
    character_count = len(set(password))
    
    # Nous calculons l'entropie du mot de passe
    entropy = len(password) * math.log2(character_count)
    return entropy

def test_password_strength(password):
    # Nous calculons l'entropie du mot de passe
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
