# Code pour le génie industriel, méthode de recherche par voisinage

# Liste initiale, qui code une solution trouvée précedemment grâce à l'implémentation de notre méthode heuristique, avec indice = num_machine et Valeur = emplacement
L = [4, 3, 7, 2, 1, 9, 8, 5, 6]
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

from cout import valeur_list
from data import D1,D2,OF1,OF2,V1,V2
from random import randint



def descente_un_pas(Sol, D, OF, V, nb_perm) :
    '''technique de recherche locale par la méthode de descente :
    on va procéder par échange de machines deux par deux de manière aléatoire
    On choisira la première combinaison plus avantageuse et on s'arretera une fois qu'on l'aura trouvé
    On effectuera donc une descente d'un pas
    On choisi de tester nb_perm permutations, avant de s'arrêter si on ne trouve rien de mieux et de renvoyer 
    la solution initiale'''
    
    # Compteur
    c = 0
    while c < nb_perm :
        # Choix de deux machines de manière aléatoire, dont on permute les emplacements
        m1 = randint(0, len(D)-3)
        m2 = randint(0, len(D)-3)
        
        new_Sol = Sol.copy()
        new_Sol[m1], new_Sol[m2] = Sol[m2], Sol[m1]
        
        # Calcul du cout pour new_Sol
        if valeur_list(OF, D, V, new_Sol) < valeur_list(OF, D, V, Sol):
            return new_Sol
        c += 1
    return Sol



def descente(Sol, D, OF, V, n, nb_perm_max) :
    '''technique de recherche locale par la méthode de descente :
    on effectue n itérations : à chaque fois, on cherche un point de descente et on prend le premier qu'on trouve.
    Le grand nombre d'itérations va permettre d'améliorer la solution initiale'''
    
    for n in range(n):
        Sol = descente_un_pas(Sol, D, OF, V, nb_perm_max)
    return Sol




if __name__ == "__main__":
    # Appel des fonctions : 
    print("Cout initial :", valeur_list(OF1, D1, V1, L1))
    new_L = descente(L1, D1, OF1, V1, 1000, 100)
    
    print("Nouvelle disposition :", new_L, ", dont le cout est ", valeur_list(OF1, D1, V1, new_L))