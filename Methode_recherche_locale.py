# Code pour le génie industriel, méthode de recherche par voisinage

# Dictionnaire initial, qui code une solution trouvée précedemment grâce à l'implémentation de notre méthode heuristique
D = {1:4, 2:3, 3:7, 4:2, 5:1, 6:9, 7:8, 8:5, 9:6}    # clé  = machine, valeur = emplacement


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




def complementation(D) :
    '''technique de recherche locale par complémentation :
    on met une machine dans l'emplacement vide (donc l'emplacement vide 
    devient l'acien emplacement de cette macine) et on voit si la solution est améliorée'''
    
    # On récupère la liste des machines (de 1 à 9, 9 étant la machine fictive)
    machine = list(D.keys())
    emplacement_vide = D[9]      # On récupère le numéro de l'emplacement vide

    # Le dictionnaire save sauvegardera la meilleure solution trouvée. Il renverra D s'il n'y en a pas
    save = D
    
    for n in machine :
        Ds = D.copy()
        if D[n] == emplacement_vide :
            pass
        else :
            Ds[n] = emplacement_vide
            Ds[9] = D[n]
            
            # Calcul du cout pour Ds
            if cout(Ds) < cout(D):
                save = Ds.copy()
                
    return save




from random import randint

def descente_un_pas(D) :
    '''technique de recherche locale par la méthode de descente :
    on va procéder par échange de machines deux par deux de manière aléatoire
    On choisira la première combinaison plus avantageuse et on s'arretera une fois qu'on l'aura trouvé
    On effectuera donc une descente d'un pas
    On choisi de tester 50 permutations, avant de s'arrêter si on ne trouve rien de mieux et de renvoyer 
    la solution initiale'''
    
    # Compteur
    c = 0
    while c < 50 :
        # Choix de deux machines de manière aléatoire, dont on permute les emplacements
        m1 = randint(1,9)
        m2 = randint(1,9)
        
        Ds = D.copy()
        Ds[m1], Ds[m2] = D[m2], D[m1]
        
        # Calcul du cout pour Ds
        if cout(Ds) < cout(D):
            return Ds
        c += 1
    return D



def descente(D) :
    '''technique de recherche locale par la méthode de descente :
    on effectue 200 itérations : à chaque fois, on cherche un point de descente et on prend le premier qu'on trouve.
    Le grand nombre d'itérations va permettre d'améliorer la solution initiale'''
    
    for n in range(200):
        D = descente_un_pas(D)
    return D



# Appel des fonctions : 
new_D = complementation(D)
print("Cout initial :", cout(D))

D1 = descente(new_D)

print("Nouvelle disposition :", D1, ", dont le cout est ", cout(D1))