from random import *


def cout(L):
    """ renvoi le cout de la solution L en dictionnaire """
    # Distances entre chaque emplacement
    D = [[0, 9, 4, 9, 9, 4, 15, 4, 11, 9], 
         [7, 0, 6, 11, 14, 5, 9, 12, 7, 7], 
         [4, 13, 0, 9, 9, 14, 15, 12, 5, 14], 
         [7, 5, 8, 0, 4, 15, 12, 5, 5, 7], 
         [11, 8, 7, 13, 0, 11, 10, 11, 6, 5], 
         [13, 4, 6, 15, 10, 0, 4, 10, 9, 7], 
         [9, 4, 10, 15, 5, 13, 0, 14, 7, 15], 
         [11, 7, 7, 10, 13, 15, 10, 0, 12, 11], 
         [9, 6, 10, 10, 11, 10, 7, 7, 0, 5], 
         [10, 10, 11, 9, 7, 9, 5, 7, 8, 0], 
         [10, 9, 9, 15, 8, 6, 7, 9, 10, 10]]
    
    V = [4982, 2185, 2209, 2083, 4286, 4654, 3925]
    
    OF = [ [2,   1,   4,   7,   6,   3,   5,   8],
           [3,   6,   8,   2,   3,   1,   7,   5],
           [8,   5,   6,   4,   7,   3,   1],
           [4,   7,   3,   5,   2,   1,   6],
           [3,   2,   6,   7,   4],
           [1,   3,   2,   5,   4,   7,   6],
           [5,   6,   7,   3,   4,   7]]
    S = 0
    
    for produit in range(len(V)):
        distance_produit = 0
        for machine in range(len(OF[produit])-1):
            # récuperer la distance entre les machines 
            m1 = OF[produit][machine] # machine
            m2 = OF[produit][machine+1] # machine suivante
            
            
            e1 = L[m1]
            e2 = L[m2]
            
            
            distance_produit += D[e1-1][e2-1]
            
        distance_produit += D[0][OF[produit][0]] + D[-1][OF[produit][-1]]
            
        
        S += distance_produit * V[produit]

        
    return S


def Générer(MaxPopul,ind):
    """générer aléatoirement MaxPopul individus :
    Générer un ensemble de permutations aléatoires à partir d'une solution de base"""
    L=[]
    for i in range(MaxPopul):
        m1 = randint(0,len(ind)-1)
        m2 = randint(0,len(ind)-1)
        
        Ds = ind.copy()
        Ds[m1], Ds[m2] = ind[m2], ind[m1]
        L.append(Ds)
    return L    

    


def Evaluer(Popul):
    """Calculer f(Popul(i)) pour i allant de 1 à MaxPolul"""
    T = []
    for i in range(len(Popul)):
        
        T.append(cout(Popul[i]))
        
    
    
    
    return T





def Sélection(NbSelect,popul):
    """/sélectionner NbSelect (nombre paire) d'individus et retourner  /les indices dans TabSelect
    Methode de tournoi binaire"""
    TabSelect = []
    for i in range(NbSelect):
        n1 = randint(1,len(popul))
        n2 = randint(1,len(popul))
        if popul[n1] > popul[n2] :
            TabSelect.append(n1)
        else :
            TabSelect.append(n2)
    
    return TabSelect
        

def Croisement(PCrois,TabSelect,NbSelect,TabEnfant,NbEnfant):
    """/avec une probabilité Pcrois, croiser tout couple
    /d'individus d'indice dans TabSelect et retourner NbEnfant
    /individus-enfants dans un tableau TabEnfant"""  
    
    
    pass

def Mutation(PMut,TabEnfant,NbEnfant):
    """/avec une faible probabilité Pmut, modifier aléatoirement
/les enfants et retourner le résultat dans TabEnfant"""
    pass


def Remplacement(TabEnfant,Popul):
    """/remplacer les individus de TabEnfant dans la population (en
    /préservant la meilleure solution !)
    /exemple : garder dans Popul « les MaxPopul meilleure individus »
    /parmi les(MaxPopul+NbEnfant)individus"""    
    pass



D = [4, 3, 7, 2, 1, 9, 8, 5, 6]
Popul = Générer(100,D)
COUT = Evaluer(Popul)
S = Sélection(4,Popul)
print(S)
print(COUT)

