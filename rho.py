# -*- coding:utf-8 -*-

"""
TP4 PAC - factoring
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
response = server.query('get/3/C')

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
        # print("Résultat : " + str(n))
        
    return n


def pgcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

def pollardrho(n, x1=1, f=lambda x: x**2+1):
    x = x1
    cpt = 0
    y = f(x) % n
    p = pgcd(y-x, n)
    while p == 1:
        x = f(x) % n
        y = f(f(y)) % n
        p = pgcd(y-x, n)

    if p == n:
        return None
    return p


# ----------------------------------------------------------------------------
# Calcul des facteurs
# -------------------------

cpt = 0

def factorise(n):
    if(n == 2):
        f.append(2)
        return

    n = divide_by(n, 2)
    p = 3

    while n != 1:
        if(p == n):
            f.append(p)
            break
        if(p > floor(sqrt(n))) :
            n = divide_by(n, n)
            continue
        n = divide_by(n, p)
        p = premier_suivant(p)    
    

    
while(n != 1):
    p = pollardrho(n)
    if p == None:
        f.append(n)
        print('Fini !!')
        break
    n = n // p
    # f.append(p)
    print("n : " + str(n))
    factorise(p)

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
