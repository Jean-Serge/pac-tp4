# -*- coding:utf-8 -*-

"""
TP4 PAC - shifumi
"""

from client import *
from random import randint

# ----------------------------------------------------------------------------
# Définition des variables
# -------------------------
URL = 'http://pac.bouillaguet.info/TP4/shifumi-deathmatch/'
NAME = 'monbailly'

# Coups possibles
PIERRE = 88275625857605
FEUILLE = 19779480974019653
CISEAUX = 18939445432636760

# Définition des variables nécessaires au chiffrement
p = 
g = randint(0, p-1)
x = randint(0, p-1)
h = pow(g, x, p)


server = Server(URL)

# Initialisation de la partie
response = server.query('insert-coin/' + NAME)
# print(response)

def chiffrer_coup(coup, k):
    c1 = pow(g, k, p)
    c2 = coup * pow(h, k, p)
    
    return c1, c2

    
# ----------------------------------------------------------------------------
# Round
# -------------------------
response = server.query('start/' + NAME)
print(response)
foobar = response['foobar']

k = randint(0, p-1)

cipher = chiffrer_coup(FEUILLE, k)
try:
    response['status']
    print('Je commence')    
    
except KeyError:
    print('Le serveur commence')



dic = {'foobar':foobar, 'commitment':{'ciphertext':cipher, 'PK':{'g':g, 'h':h, 'p':p}}}
response = server.query('move', dic)
print(response)
