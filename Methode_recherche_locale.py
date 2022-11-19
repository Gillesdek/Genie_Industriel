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
    On part de sol, on a les paramètres D, Of et V qui représente le problème.
    On choisit de tester nb_perm permutations, avant de s'arrêter si on ne trouve rien de mieux et de renvoyer 
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



def descente(Sol_init, D, OF, V, n, nb_perm_max, m = 5) :
    '''technique de recherche locale par la méthode de descente :
    on effectue n itérations : à chaque fois, on cherche un point de descente et on prend le premier qu'on trouve.
    Le grand nombre d'itérations va permettre d'améliorer la solution initiale.
    nb_perm_max correspond au nombre d'itérations stables de permutations à effectuer avant de relancer une nouvelle itération
    Le paramètre m correspond au nombre de fois que l'on veut lancer l'algorithme complet, pour ensuite pouvoir faire une moyenne'''
    
    y = []                      # On garde trace des différents couts trouvés
    x = [i for i in range(n)]
    
    
    # On va effectuer une moyenne sur m itérations
    for k in range(m) :
        y_k =[]
        Cout_Sol = valeur_list(OF, D, V, Sol_init)
        Sol = Sol_init  
        
        for i in range(n):
            y_k.append(Cout_Sol)
            Sol = descente_un_pas(Sol, D, OF, V, nb_perm_max)
            Cout_Sol = valeur_list(OF, D, V, Sol)
            
        y.append(y_k)
        
    graphe(x, y, nb_perm_max)
    
    moy = 0                # moyenne des couts finaux trouvés
    for i in range(m):
        moy += y[i][-1]
    return Sol, moy/m



def graphe(x, y, nb_perm_max):
    """"Fonction dont l'objectif est d'afficher de manière visuelle la performance 
    de la méthode de descente à l'aide d'un graphe   """
    import matplotlib.pyplot as plt
    
    # Tracé du graphique
    fig, ax = plt.subplots()
    for i in range(5) :
        ax.plot(x, y[i])
            
    plt.title(f"Cout en fonction du nombre d'itérations avec \n un nombre de permutations stables maximum de {nb_perm_max}")
    plt.xlabel("Nombre d'itérations")
    plt.ylabel("Coût")
    plt.show()               # affiche la figure à l'écran    
    
    
    
    
if __name__ == "__main__":
    # Appel des fonctions : 
    # Petite instance
    print("Cout initial :", valeur_list(OF1, D1, V1, L1))
    new_L, cout_moy = descente(L1, D1, OF1, V1, 50, 10)
    
    print("Nouvelle disposition :", new_L, ", dont le cout est ", valeur_list(OF1, D1, V1, new_L))
    print(f"En moyenne, le cout final observé est de {cout_moy}")
    
    
    # Grande instance
    Solution_naive2 = [i+1 for i in range(len(D2))] 
    print("Cout initial :", valeur_list(OF2, D2, V2, Solution_naive2))
    new_L2, cout_moy2 = descente(Solution_naive2, D2, OF2, V2, 150, 100)
    print("Nouvelle disposition :", new_L2, ", dont le cout est ", valeur_list(OF2, D2, V2, new_L2))
    print(f"En moyenne, le cout final observé est de {cout_moy2}")  