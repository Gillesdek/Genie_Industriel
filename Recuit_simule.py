from math import *
import random
import numpy as np
import matplotlib.pyplot as plt

distances = [[0, 9, 4, 9, 9, 4, 15, 4, 11, 9,12],
    [7, 0, 6, 11, 14, 5, 9, 12, 7, 7,8],
    [4, 13, 0, 9, 9, 14, 15, 12, 5, 14,8],
    [7, 5, 8, 0, 4, 15, 12, 5, 5, 7,8],
    [11, 8, 7, 13, 0, 11, 10, 11, 6, 5,6],
    [13, 4, 6, 15, 10, 0, 4, 10, 9, 7,8],
    [9, 4, 10, 15, 5, 13, 0, 14, 7, 15,8],
    [11, 7, 7, 10, 13, 15, 10, 0, 12, 11,4],
    [9, 6, 10, 10, 11, 10, 7, 7, 0, 5,14],
    [10, 10, 11, 9, 7, 9, 5, 7, 8, 0,10],
    [10, 9, 9, 15, 8, 6, 7, 9, 10, 10,0]]

ventes = [4982, 2185, 2209, 2083, 4286, 4654, 3925]

ordre =  [ [2,   1,   4,   7,   6,   3,   5,   8],
           [4,   6,   8,   2,   3,   1,   7,   5],
           [8,   5,   6,   4,   7,   3,   1],
           [4,   7,   3,   5,   2,   1,   6,8],
           [3,   2,   6,   7,   4],
           [1,   3,   2,   5,   4,   7,   6],
           [5,   6,   7,   3,   4,   1]]

def cout(s): #Calcul du cout d'une solution. Une solution est représentée par une permutation de L = [1,2,...,9] (la machine 9 est la machine vide). La machine L[i] est à l'emplacement i+1.
    somme = 0
    for i in range(0,len(ventes)):
        trajet = distances[0][s.index(ordre[i][0])+1] + distances[s.index(ordre[i][-1])+1][-1]
        for j in range(0,len(ordre[i])-1):
            trajet += distances[s.index(ordre[i][j])+1][s.index(ordre[i][j+1])+1]
        somme += trajet*ventes[i]
    return somme

#La fonction Cout est en O(p*m^2) avec p le nombre de produit et m le nombre de machines

def echange(l): #Fonction qui échange au hasard la position de deux éléments d'une liste
    n = len(l)
    i = random.randint(0,n-1)
    j = i
    while j == i:
        j = random.randint(0,n-1)
    l[i],l[j] = l[j],l[i]
    return l

# La fonction echange se fait en temps constant

def recuit(s0,t0,n,alpha): #On initialise l'algo de recuit avec une solution, une température et un palier de température arbitraires
    cout_min = +inf
    j = 0
    i = 0
    moyenne = 0
    while j < n :
        j += 1
        i += 1
        s = s0.copy()
        s = echange(s)
        if cout(s) < cout(s0):
            s0 = s
            if cout(s0) < cout_min :
                sm = s0 ; cout_min = cout(s0) ; j = 0
        else :
            deltaf = cout(s) - cout(s0)
            u = random.random()
            if u <= exp(-deltaf/t0):
                s0 = s
        t0 = t0*alpha
    return [cout_min, sm]

# La fonction recuit est en O(n*p*m^2) avec p le nombre de produit et m le nombre de machines

def plot_recuit(s0,t0,n,alpha,m):
    L = []
    moyenne = 0
    for k in range(0,m):
        L.append(recuit(s0,t0,n,alpha)[0])
        moyenne += L[k]
    moyenne = moyenne/m
    fig, ax = plt.subplots()
    ax.plot(L)
    plt.axhline(y=moyenne,color='red')
    plt.show()

