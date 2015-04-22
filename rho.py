# -*- coding:utf-8 -*-

"""
TP4 PAC - factoring
"""

from fractions import gcd
from math import sqrt
from math import floor
from primalite import millerRabin

import random

    
def est_premier(p):
    # if(p % 2 == 0):
    #     return False

    # sqr = sqrt(p)
    # cpt = 3
    # while(cpt <= sqr):
    #     if(p % cpt == 0):
    #         return False
    #     cpt += 2

    # return True
    return millerRabin(p)

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
    f = []
    while n % p == 0 :
        # print(str(n) + " divisé par " + str(p))
        n = n // p
        f.append(p)
        # print("Résultat : " + str(n))
        
    return n, f


# def pollardrho(n, x1=1, f=lambda x: x**2+1):
#     x = x1
#     cpt = 0
#     y = f(x) % n
#     p = gcd(y-x, n)
#     while p == 1:
#         x = f(x) % n
#         y = f(f(y)) % n
#         p = gcd(y-x, n)

#     if p == n:
#         return None
#     return p

def pollardrho(N):
    if N%2==0:
        return 2
    x = random.randint(1, N-1)
    y = x
    c = random.randint(1, N-1)
    g = 1
    while g==1:
        x = ((x*x)%N+c)%N
        y = ((y*y)%N+c)%N
        y = ((y*y)%N+c)%N
        g = gcd(abs(x-y),N)

    return g

def brent(N):
    if N%2==0:
        return 2
    y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                y = ((y*y)%N+c)%N
                q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m

        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1:
                break
    return g    


# ----------------------------------------------------------------------------
# Calcul des facteurs
# -------------------------

def factorise(n):
    f = []
    if(n == 2):
        f.append(2)
        return f

    n, tmp = divide_by(n, 2)
    f += tmp
    p = 3

    while n != 1:
        if(p == n):
            f.append(p)
            break
        if(p > sqrt(n)) :
            n, tmp = divide_by(n, n)
            f += tmp
            continue
        n, tmp = divide_by(n, p)
        f += tmp
        p = premier_suivant(p)    

    return f

    
