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
CARACTERE=list("&#@{[(\])]}]")



def alea_cherche(liste,n):
    """
    Cette fonction doit chercher dans une liste un élément pris aléatoirement
    liste : est la liste des éléments dont on veut faire un tirage
    n :  est le nombre d'éléments tités améatoirement dans la liste : liste'
    
    """
    return random.choices(liste, k=n)

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
    # verifie qu'on ne peut pas avoir deux caractères de même type      
    # on parcours la liste de 0 à N-2
    cpt=0       
    return l
        
        
        

