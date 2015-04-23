# -*- coding:utf-8 -*-

"""
TP4 PAC - factoring
"""

from client import *
from fractions import gcd
from math import sqrt
from math import floor
from rho import *
import random



# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
URL = 'http://pac.bouillaguet.info/TP4/factoring/'
server = Server(URL)
response = server.query('get/3/C')


id = response['id']
n = response['n']
n_donne = n
f = []

print(type(n))


while(n != 1):
    if(millerRabin(n)):
       f.append(n)
       print('Fini - premier !!')
       break

    p = pollardrho(n)
    if p == n:
        f.append(n)
        print('Fini - p = n!!')
        break

    n = n // p
    f.append(p)
    print("n : " + str(n))
    
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

