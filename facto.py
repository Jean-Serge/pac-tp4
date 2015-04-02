# -*- coding:utf-8 -*-

"""
TP2 PAC - mersenne-twister
"""

from client import *
from fractions import gcd
from math import sqrt

import random

URL = 'http://pac.bouillaguet.info/TP4/factoring/'
server = Server(URL)

def premier_suivant(x):
    while True : 
        x = x + 1
        if est_premier(x):
            return x

def est_premier(x):
    m = sqrt(x)
    crible = crible(m)
    for i in crible:
        if x % crible == 0:
            return False
    return True

def crible(x):
    """
    Retourne une liste contenant les nombre premiers < x
    Cette fonction a été récupérée sur internet.
    """
    prime_list = [2]
 
    # build a list with odd numbers after 2
    for i in range(3, x, 2):
        prime_list.append(i)
 
    # remove non prime numbers
    for i in prime_list:
        for n in prime_list:
            if n % i == 0 and i != n:
                prime_list.remove(n)
 
    return prime_list        


# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
response = server.query('get/1/D')

id = response['id']
n = response['n']
f = []

crible = crible(10000000)

i = 0
# while True :
#     if i == len(crible):
#         break
#     if n % crible[i] == 0:
#         print(str(n) + " divisé par " + str(crible[i]) + " donne " + str(n / crible[i]))
#         n = n / crible[i]
#         f.append(crible[i])
#     else:
#         i = i + 1

while True:
    if n == 1:
        break
    while n % crible[i] == 0 :
        pass
    i = i + 1
print(n)
print(f)

x = 1
for i in f:
    x = x * i

print(x)

dic = {'id':id, 'factors':f}
response = server.query('submit/monbailly', dic)
