# -*- coding:utf-8 -*-

"""
TP4 PAC - shifumi
"""

from client import *
from random import randint
from rho import millerRabin


# ----------------------------------------------------------------------------
# Définition des fonctions utiles
# -------------------------
def chiffrer_coup(coup, k):
    """
    Retourne le coup spécifié, chiffré avec ElGamal.
    k doit être différent à chaque fois.
    p, h et g doivent être définis au préalable.
    """
    r = []
    c1 = pow(g, k, p)
    c2 = (coup * pow(h, k, p)) % p
    
    r.append(c1)
    r.append(c2)
    return r


# ----------------------------------------------------------------------------
# Définition des variables
# -------------------------
URL = 'http://pac.bouillaguet.info/TP4/shifumi-deathmatch/'
NAME = 'monbailly'


# Définition des variables nécessaires au chiffrement

# Coups possibles
PIERRE =  88275625857605
FEUILLE = 19779480974019653
CISEAUX = 18939445432636760


coups = [PIERRE, FEUILLE, CISEAUX]
coups_ASCII = ['PIERRE', 'FEUILLE', 'CISEAUX']

while(True):
    p = randint(2**1024, 2**1025)
    if(millerRabin(p)):
        break
g = 2
x = randint(0, p-1)
h = pow(g, x, p)

# Dictionnaire utilisé pour envoyer un coup
pk = {'g':g, 'h':h, 'p':p}
   

server = Server(URL)

# Initialisation de la partie
response = server.query('insert-coin/' + NAME)


def envoyer_coup(coup):
    """
    coup représente l'index dans le tableau coups.
    
    Envoi le coup sélectionné au serveur.

    Affiche ensuite le résultat.
    """
    cipher = chiffrer_coup(coups[coup], k)
    commitment = {'ciphertext':cipher, 'PK':pk}
    move = {'foobar':foobar, 'commitment':commitment}

    response = server.query('move', move)
    # print(response)

    dic = {'move':coups_ASCII[coup], 'k':k, 'barfoo':response['barfoo']}
    response = server.query('result', dic)
    print(response)


# ----------------------------------------------------------------------------
# Round
# -------------------------

while(True):
    response = server.query('start/' + NAME)
    # print(response)
    foobar = response['foobar']

    
    k = randint(0, p-1)
    
    choix = randint(0, 2)
    try:
        response['status']
        print('Je commence')    
        
    except KeyError:
        print('Le serveur commence')
        continue
    
        
    envoyer_coup(choix)
        
