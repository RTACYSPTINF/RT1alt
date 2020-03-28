# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

ce script doit fournie la possibilité de générer un mot de passe parmis un 
certain jeux de caractères
[a-z][A-Z] et[0-9] et [&#@{[(\])]}]
"""
import random
import string
from enum import Enum

ALPHA=list(string.ascii_letters)
DIGIT=list(string.digits)
CARACTERE=list("&#@{[(\])]}]'^")



def alea_cherche(liste,n):
    """
    Cette fonction doit chercher dans une liste un élément pris aléatoirement
    liste : est la liste des éléments dont on veut faire un tirage
    n :  est le nombre d'éléments tités améatoirement dans la liste : liste'
    
    """
    return random.choices(liste, k=n)

def test_caractere_different(liste):
    """
    
    """
    pass
    

def mdp_temp(N):
    """

    Parameters
    ----------
    N : TYPE interger
        DESCRIPTION. Nombre de caractères pour le mot de passe

    Returns un mot de passe avec le bonnombre de caractère sosu forme de string
    -------
    None.

    """
    l_tout_caracteres=ALPHA+DIGIT+CARACTERE
    l=random.choices(l_tout_caracteres,k=N)   
    # cetrte boucle va nous assurer que le mdp de commence
    # ni par un chiffre ni par un caractère spécial
    while True:
        if l[0] not in DIGIT and l[0] not in CARACTERE:
            break
        else:
            l=random.choices(l_tout_caracteres,k=N)     
    return l

def mdp_non_double(N):
    """
    génère un mot de passe de N caractère mais interdit que deux caractères
    de même nature se suivent :
    "aF" interdit 
    '56' interdit
    etc
    Parameters
    ----------
    N : TYPE in,teger
        DESCRIPTION.

    Returns chine de cractère mdp_str
    -------
    None.

    """
    l_tout_caracteres=ALPHA+DIGIT+CARACTERE
    l_mdp=[] # liste qui contient les caractères du mot de passe
    while len(l_mdp)!=N:
        l_mdp.append(random.choice(l_tout_caracteres))
        n_temp=len(l_mdp)
        while True and n_temp >= 2:
            if l_mdp[-1] in ALPHA and l_mdp[-2] in ALPHA:
                l_mdp[-1]=random.choice(l_tout_caracteres)
                l_mdp[-2]=random.choice(l_tout_caracteres)
                print(l_mdp)
            elif l_mdp[-1] in DIGIT and l_mdp[-2] in DIGIT:
                l_mdp[-1]=random.choice(l_tout_caracteres)
                l_mdp[-2]=random.choice(l_tout_caracteres)
            elif l_mdp[-1] in CARACTERE and l_mdp[-2] in CARACTERE: 
                l_mdp[-1]=random.choice(l_tout_caracteres)
                l_mdp[-2]=random.choice(l_tout_caracteres)
            else:
                break
    return "".join(l_mdp)
    
    
print(mdp_temp(10))
