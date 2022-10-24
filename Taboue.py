# Présentation de la méthode du taboue pour résoudre le problème de flux dans l'atelier

# Dictionnaire initial, qui code une solution trouvée précedemment grâce à l'implémentation de notre méthode heuristique
D = {1:4, 2:3, 3:7, 4:2, 5:1, 6:9, 7:8, 8:5, 9:6}    # clé  = machine, valeur = emplacement
D0 = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

#from Cout import cout
# Calcul du cout avec le dictionnaire fourni en argument
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


def meilleur_voisin(init, Taboue=[]) :
    """Un voisin est une permutation entre deux machines
    Pour choisir le meilleur voisin, il faut donc tester toutes les permutations.
    Cependant, il ne faut pas retenir une solution qui est dans la liste Taboue"""
    import math
      
    best_vois = init
    comparatif = math.inf  # Valeur infinie
    
    for machine1 in range(1, 10) :
        for machine2 in range(1, 10) :
            x = init.copy()
            x[machine1], x[machine2] = x[machine2], x[machine1]       # Permutation de deux machines
            
            ajout = True                 # indicateur qui prend la valeur vrai si la solution candidate n'est pas dans la liste taboue, faux sinon
            for interdit in Taboue :     # on vérifie que la solution proposée n'est pas dans le taboue
                if x == interdit :
                    ajout = False
            
            if ajout == True :
                if cout(x) < comparatif :
                    comparatif = cout(x)   # cout du meilleur voisin qui n'est pas dans le taboue et qui n'est pas la solution initiale
                    best_vois = x
                
    return best_vois

def MiseAJour(Taboue, nouvelle_valeur, taille_Taboue = 10) :
    """Cette fonction met à jour la liste des taboue, en suprimant la valeur la plus ancienne et en ajoutant la plus récente
    La première valeur de la liste est la plus ancienne, la dernière est la plus récente
    On choisit de stocker par défaut 10 éléments dans la liste Taboue"""
    
    if len(Taboue) < 15 :
        Taboue.append(nouvelle_valeur)
        
    else :
        for e in range(len(Taboue) - 1) :       # On fait "tourner" les valeurs, en ajoutant la nouvelle valeur à la fin de la liste tout en décalant les autres
            Taboue[e] = Taboue[e+1]
            Taboue[len(Taboue) - 1] = nouvelle_valeur
            
    return Taboue
     

def methode_taboue(x0, Nb_max_iter, Nb_max_iter_stable, taille_taboue) :
    """ Fonction qui implémente la méthode du taboue
    Les arguments sont une solution de départ, le nombre maximum d'itération et le nombre maximum d'itérations stables et la taille de la liste taboue"""
    
    xm = x0                  # xm contiendra la meilleure solution trouvée
    fm = cout(x0)            # fm contiendra le cout de la meilleure solution trouvée
    T = []                   # liste taboue initialisée à vide
    Nb_iteration = 0         # Compte le nombre d'itération
    Nb_iteration_stable = 0  # Compte le nombre d'itérations stables
    
    while Nb_iteration < Nb_max_iter and Nb_iteration_stable < Nb_max_iter_stable :
        x1 = meilleur_voisin(x0, T)         # Recherche du meilleur voisin de x0
        Nb_iteration += 1
        
        T = MiseAJour(T, x1, taille_taboue)                # Mise à jour de la liste Taboue, avec ajout du nouvel élément x1
        
        if cout(x1) < cout(x0) :
            xm = x1                         # Mise à jour de la meilleure solution
            fm = cout(x1)
            Nb_iteration_stable = 0         # On a amélioré la solution, donc on réinitialise le nombre d'itération stables à 0.
        else :
            Nb_iteration_stable += 1
        
        x0 = x1             # On recommence avec la nouvelle solution
    
    return xm, fm


def test_nb_iter(D, iter_min, iter_max, pas, Nb_iter_stable, taille_taboue) :
    import matplotlib.pyplot as plt
    x = list(range(iter_min, iter_max, pas))
    y=[]
    for Nb_iter in range(iter_min, iter_max, pas):
        y.append(methode_taboue(D, Nb_iter, Nb_iter_stable,taille_taboue)[1])
    
    plt.plot(x, y)
    plt.show() # affiche la figure à l'écran    
    
    
def test_taille_taboue(D, Nb_iter, Nb_iter_stable) :
    import matplotlib.pyplot as plt
    x = list(range(5, 15))
    y=[]
    for taille in range(5, 15):
        y.append(methode_taboue(D, Nb_iter, Nb_iter_stable, taille)[1])
    
    plt.plot(x, y)
    plt.show() # affiche la figure à l'écran    

    
print(cout(D))
print(methode_taboue(D, 100, 100,8))
#print(test_nb_iter(D, 100, 3000, 50, 10, 7))
print(test_taille_taboue(D, 100, 50))
'''
m = nombre de machines
e = nombre d'emplacement
p = nombre de produits
t = taille de la liste taboue

Complexité de la méthode :
- fonction cout : O(p*m)
- fonction meilleur voisin : O(t*m^2)
- fonction MiseAJour : O(t)
- fonction methode_Taboue : O(Nb_max_iter * Nb_max_iter_stable *t^2 * m^3 * p)

'''