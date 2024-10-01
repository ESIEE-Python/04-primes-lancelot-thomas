"""Module affichant la liste des nombres premiers"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un nombre est premier.

    Parameters:
        p (int): Nombre à vérifier

    Returns:
        bool: Vérifie si p est premier
    """
    # votre code ici
    if p<2 :
        return False
    for i in range(2, int(sqrt(p)+1)):
        if p%i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Fonction principale affichant parmis les 100 premiers nombres
    les nombres premiers
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
