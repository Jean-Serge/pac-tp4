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
response = server.query('get/1/D')

id = response['id']
n = response['n']
f = []

n_donne = n
print("n : " + str(n))


# ----------------------------------------------------------------------------
# Calcul des facteurs
# -------------------------
p = 2

while n != 1:
    # Si n % p == 0 alors n est multiple de p
    if n % p == 0:
        f.append(p)
        n = floor(n / p)
        print("n : " + str(n))
        continue
    
    # Incrémenter le nombre p 
    if p == 2:
        p = 3
    else:
        p += 2

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
