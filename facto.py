# -*- coding:utf-8 -*-

"""
TP2 PAC - mersenne-twister
"""

from client import *
from fractions import gcd
from math import sqrt
from math import floor

import random

URL = 'http://pac.bouillaguet.info/TP4/factoring/'
server = Server(URL)


# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
response = server.query('get/2/D')

id = response['id']
n = response['n']
f = []

n_donne = n
print(type(n))

    
def est_premier(p):
    if(p % 2 == 0):
        return False

    sqr = sqrt(p)
    cpt = 3
    while(cpt <= sqr):
        if(p % cpt == 0):
            return False
        cpt += 2

    return True

def premier_suivant(p):
    while(True):
        p += 2
        if(est_premier(p)):
               return p

def divide_by(n, p):
    """
    Divise le nombre n par p autant que possible.
    Retourne le dernier résultat de n / p
    """
    while n % p == 0 :
        # print(str(n) + " divisé par " + str(p))
        n = n // p
        f.append(p)
        print("Résultat : " + str(n))
        
    return n


# ----------------------------------------------------------------------------
# Calcul des facteurs
# -------------------------

n = divide_by(n, 2)
p = 3

while n != 1:
    
    if(p > floor(sqrt(n))) :
        n = divide_by(n, n)
        continue
    n = divide_by(n, p)
    p = premier_suivant(p)    
    
    
print(f)
trouve = 1
for i in f:
    trouve *= i

print('\n\n')
print(n_donne)
print(trouve)

dic = {'id':id, 'factors':f}
response = server.query('submit/monbailly', dic)
print(response)
