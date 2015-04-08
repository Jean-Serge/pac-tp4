# -*- coding:utf-8 -*-

"""
TP2 PAC - mersenne-twister
"""

from client import *
from fractions import gcd

import random

URL = 'http://pac.bouillaguet.info/TP4/ElGamal-forgery/'
server = Server(URL)

def xgcd(a,b):
    """
    Calcul de XGCD(a, b) récupéré sur internet
    """
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, r
    return a, prevx, prevy
                     

def inverse_mod(x, y):
    """
    Calcul de l'inverse modulaire de x par rapport à y.
    Revient à calculer le XGCD(x, y)
    """
    a,b,c = xgcd(x, y)
    return b

# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
response = server.query('PK/monbailly') # contient les champs p, g, h

p = response['p']
g = response['g']
h = response['h']
q = p - 1
k = random.randint(2, q)


# ----------------------------------------------------------------------------
# Calcul des valeurs
# -------------------------
e = random.randint(2, q)
while True:
    v = random.randint(2, q)
    if gcd(v, q) == 1:
        break


r = (pow(g, e, p) * pow(h, v, p)) % p
inv_v = inverse_mod(v, q)
s = ((-r) * inv_v) % q

m = (e * s) % q

# ----------------------------------------------------------------------------
# Envoi de la réponse
# -------------------------
dic = {'m':m, 'signature':(r, s)}
response = server.query('verify/monbailly', dic)
print(response) # Status:OK
