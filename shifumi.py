# -*- coding:utf-8 -*-

"""
TP4 PAC - shifumi
"""

from client import *
from random import randint
from rho import millerRabin

# ----------------------------------------------------------------------------
# Définition des variables
# -------------------------
URL = 'http://pac.bouillaguet.info/TP4/shifumi-deathmatch/'
NAME = 'monbailly'

# Coups possibles
PIERRE =  88275625857605
FEUILLE = 19779480974019653
CISEAUX = 18939445432636760

# Définition des variables nécessaires au chiffrement

p = 10
while(not millerRabin(p)):
    p = randint(10**100, 10**200)

g = 2
x = randint(0, p-1)
h = pow(g, x, p)


server = Server(URL)

# Initialisation de la partie
response = server.query('insert-coin/' + NAME)
# print(response)

def chiffrer_coup(coup, k):
    r = []
    c1 = pow(g, k, p)
    c2 = (coup * pow(h, k, p)) % p
    
    r.append(c1)
    r.append(c2)
    return r

    
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


pk = {'g':g, 'h':h, 'p':p}
commitment = {'ciphertext':cipher, 'PK':pk}
dic = {'foobar':foobar, 'commitment':commitment}

# while(True):
    # try:
print(dic)
response = server.query('move', dic)
print(response)
# break
    # except: 
    #     print('raté')
    #     continue
