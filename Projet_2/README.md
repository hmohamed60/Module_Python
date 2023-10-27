# Projet 2

# Générateur et testeur de mot de passe

Ce programme Python est un outil de sécurité qui offre plusieurs fonctionnalités liées aux mots de passe. Il comprend un générateur de mot de passe, un testeur de force de mot de passe et un générateur de passphrase. Les fonctionnalités sont décrites ci-dessous :

## Menu

Lorsque vous exécutez le programme, vous verrez un menu avec les options suivantes :

1. Générateur de mot de passe
2. Testeur de mot de passe
3. Générateur de passphrase
4. Recommencer
5. Quitter

Vous pouvez choisir une option en saisissant le numéro correspondant à votre choix.

## 1. Générateur de mot de passe

Cette option vous permet de générer un mot de passe aléatoire en fonction des critères que vous spécifiez. Vous pouvez définir la longueur du mot de passe ainsi que le nombre de minuscules, de majuscules, de chiffres et de caractères spéciaux dans le mot de passe.

## 2. Testeur de mot de passe

Le testeur de mot de passe vérifie la force d'un mot de passe en fonction de son entropie. Il vous indique si le mot de passe est "Très faible", "Faible", "Moyen" ou "Fort" en fonction de l'entropie calculée.

## 3. Générateur de passphrase

Cette option génère une passphrase basée sur une liste de mots prédéfinis. Vous pouvez spécifier le nombre de mots dans la passphrase.

## 4. Recommencer

Si vous choisissez cette option, le programme reviendra au menu principal, vous permettant de sélectionner une autre opération.

## 5. Quitter

Vous pouvez quitter le programme en sélectionnant cette option.

## Fonctionnalités supplémentaires

Le programme est conçu de manière modulaire avec des fichiers séparés pour chaque fonctionnalité :

- `password_generator.py` contient le générateur de mot de passe aléatoire.
- `password_tester.py` contient le testeur de force de mot de passe.
- `passphrase_generator.py` contient le générateur de passphrase.
- `main.py` est le fichier principal qui gère le menu et les interactions avec l'utilisateur.

## Comment utiliser le programme

1. Assurez-vous d'avoir Python installé sur votre système.

2. Exécutez le fichier `main.py`.

3. Suivez les instructions à l'écran pour sélectionner l'opération souhaitée.

4. Le programme vous guidera tout au long du processus en fonction de votre choix.


