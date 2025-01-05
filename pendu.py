import random
import urllib.request
import os

def telecharger_dictionnaire():
    """Télécharge le dictionnaire français si nécessaire et retourne la liste des mots"""
    fichier_dict = "dictionnaire.txt"

    # Vérifie si le fichier existe déjà
    if not os.path.exists(fichier_dict):
        url = "https://raw.githubusercontent.com/atebits/Words/master/Words/fr.txt"
        urllib.request.urlretrieve(url, fichier_dict)
    
    # Charge les mots du dictionnaire
    with open(fichier_dict, 'r', encoding='utf-8') as f:
        mots = [mot.strip().upper() for mot in f.readlines()
                if mot.strip().isalpha() and len(mot.strip()) >= 4
                and len(mot.strip()) <= 12]
        return mots

def dessin_pendu(nb):
    tab=[
    """
    =============
    """,
    """
        +
        |
        |
        |
        |
        |
    ==============
    """,
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]

def jeu():
    try:
        # Chargement du dictionnaire
        print("Chargement du dictionnaire...")
        mots = telecharger_dictionnaire()
        print(f"Dictionnaire chargé avec {len(mots)} mots")
        
        nom = input("Entrez votre nom : ")
        mot = random.choice(mots)
        mot1 = mot
        mot = list(mot)
        tirets = ["_" for i in range(len(mot))]
        lettres_utilisees = set()
        erreur = 0
        
        print("\nLe mot à deviner contient", len(mot), "lettres")
        print(" ".join(tirets))
        
        while erreur < 8 and '_' in tirets:
            lettre = input("Entrez une lettre : ").upper()
            
            if len(lettre) > 1:
                print("Veuillez n'entrer qu'une seule lettre.")
                continue
                
            if not lettre.isalpha():
                print("Veuillez entrer une lettre valide.")
                continue
                
            if lettre in lettres_utilisees:
                print("Vous avez déjà essayé cette lettre.")
                continue
                
            lettres_utilisees.add(lettre)
            
            if lettre in mot:
                while lettre in mot:
                    n = mot.index(lettre)
                    mot.remove(lettre)
                    mot.insert(n, '_')
                    del(tirets[n])
                    tirets.insert(n, lettre)
                print(" ".join(tirets))
                print("Lettres déjà utilisées:", ", ".join(sorted(lettres_utilisees)))
            else:
                print("La lettre n'est pas dans le mot.")
                erreur += 1
                print(dessin_pendu(erreur))
                print(" ".join(tirets))
                print(f"Il vous reste {8-erreur} essais")
                print("Lettres déjà utilisées:", ", ".join(sorted(lettres_utilisees)))
        
        if '_' not in tirets:
            print(f"\nFélicitations {nom}, vous avez trouvé le mot {mot1} !!!")
        else:
            print(f"\nDommage, vous n'avez pas trouvé le mot. Le mot était {mot1}.")
            
    except Exception as e:
        print(f"Une erreur est survenue: {e}")
        print("Vérifiez votre connexion internet pour télécharger le dictionnaire.")

if __name__ == "__main__":
    jeu()