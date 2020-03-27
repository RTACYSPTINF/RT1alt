# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

ce script doit fournie la possibilité de générer un mot de passe parmis un 
certain jeux de caractères
[a-z][A-Z] et[0-9] et [&#@{[(\])]}]
"""
import random
from enum import Enum

"""
class Strategie(Enum):
    import string
    ALPHA = list(string.ascii_letters)
    DIGIT = list(string.digits)
    SPECIAL = list("&#@{}[]()\$")
"""  


class CONSTANTE(Enum):
    a=1
    B=2
    
def ale_cherche(liste,n):
    """
    Cette fonction doit chercher dans une liste un élément pris aléatoirement
    liste : est la liste des éléments dont on veut faire un tirage
    n :  est le nombre d'éléments tités améatoirement dans la liste : liste'
    
    """
    return random.choices(liste, k=n)

