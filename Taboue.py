# Présentation de la méthode du taboue pour résoudre le problème de flux dans l'atelier


# Solution codée sous forme de liste avec indice = num_machine et Valeur = emplacement
Solution_opt = [7,5,1,2,9,6,8,4,3]            # Solution optimale pour la petite instance du problème
Solution_naive = [4, 3, 7, 2, 1, 9, 8, 5, 6]  # Solution naïve trouvée précédement pour la petite instance du problème
Solution_naive2 = [1, 3, 2, 4, 6, 5, 8, 7, 9]  

from cout import valeur_list
from data import D1,D2,OF1,OF2,V1,V2



def meilleur_voisin(init, D, OF, V, Taboue=[]) :
    """Un voisin est une permutation entre deux machines
    Pour choisir le meilleur voisin, il faut donc tester toutes les permutations.
    Cependant, il ne faut pas retenir une solution qui est dans la liste Taboue"""
    import math
      
    best_vois = init
    comparatif = math.inf  # Valeur infinie
    
    for machine1 in range(1, len(D)-1) :
        for machine2 in range(1, len(D)-1) :
            x = init.copy()
            x[machine1 -1], x[machine2 -1] = x[machine2 - 1], x[machine1 - 1]       # Permutation de deux machines     # On met des -1 parce que les numéros d'indices dans la liste commencent à 0
            
            ajout = True                 # indicateur qui prend la valeur vrai si la solution candidate n'est pas dans la liste taboue, faux sinon
            for interdit in Taboue :     # on vérifie que la solution proposée n'est pas dans le taboue
                if x == interdit :
                    ajout = False
            
            if ajout == True :
                if valeur_list(OF, D, V, x) < comparatif :
                    comparatif = valeur_list(OF, D, V, x)   # cout du meilleur voisin qui n'est pas dans le taboue et qui n'est pas la solution initiale
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
     

def methode_taboue(x0, D, OF, V, Nb_max_iter, Nb_max_iter_stable, taille_taboue) :
    """ Fonction qui implémente la méthode du taboue
    Les arguments sont une solution de départ, le nombre maximum d'itération et le nombre maximum d'itérations stables et la taille de la liste taboue"""
    
    xm = x0                  # xm contiendra la meilleure solution trouvée
    fm = valeur_list(OF, D, V, x0)            # fm contiendra le cout de la meilleure solution trouvée
    T = []                   # liste taboue initialisée à vide
    Nb_iteration = 0         # Compte le nombre d'itération
    Nb_iteration_stable = 0  # Compte le nombre d'itérations stables
    
    while Nb_iteration < Nb_max_iter and Nb_iteration_stable < Nb_max_iter_stable :
        x1 = meilleur_voisin(x0, D, OF, V, T)         # Recherche du meilleur voisin de x0
        Nb_iteration += 1
        
        T = MiseAJour(T, x1, taille_taboue)                # Mise à jour de la liste Taboue, avec ajout du nouvel élément x1
        
        if valeur_list(OF, D, V, x1) < fm :
            xm = x1                         # Mise à jour de la meilleure solution
            fm = valeur_list(OF, D, V, x1)  
            Nb_iteration_stable = 0         # On a amélioré la solution, donc on réinitialise le nombre d'itération stables à 0.
        else :
            Nb_iteration_stable += 1
        
        x0 = x1             # On recommence avec la nouvelle solution
    
    return xm, fm





## Fonctions pour l'affichage (tracé de graphiques pour évaluer l'impact des différents paramètres)
def test_nb_iter(Sol, D, OF, V, iter_min, iter_max, pas, Nb_iter_stable, taille_taboue) :
    """ Fonction qui permet de tracer un graphique du cout en fonction 
    du nombre d'itération maximum """
    x = list(range(iter_min, iter_max, pas))
    y=[]
    for Nb_iter in range(iter_min, iter_max, pas):
        y.append(methode_taboue(Sol, D, OF, V, Nb_iter, Nb_iter_stable,taille_taboue)[1])
    
    graphique(x,y,"Nombre maximum d'itérations", "variable", Nb_iter_stable, taille_taboue)
       

def test_nb_iter_stable(Sol, D, OF, V, Nb_iter, iter_stable_min, iter_stable_max, pas, taille_taboue) :
    """ Fonction qui permet de tracer un graphique du cout en fonction 
    du nombre d'itération stable maximum """
    x = list(range(iter_stable_min, iter_stable_max, pas))
    y=[]
    for Nb_iter_Stable in range(iter_stable_min, iter_stable_max, pas):
        y.append(methode_taboue(Sol, D, OF, V, Nb_iter, Nb_iter_Stable,taille_taboue)[1])
    
    graphique(x,y,"Nombre maximum d'itérations stables", Nb_iter, "variable", taille_taboue)
    
    
    
def test_taille_taboue(Sol, D, OF, V, Nb_iter, Nb_iter_stable) :
    """ Fonction qui permet de tracer le graphique du cout en fonction 
    de la taille de la liste taboue """    
    x = list(range(5, 15))
    y=[]
    for taille in range(5, 15):
        y.append(methode_taboue(Sol, D, OF, V, Nb_iter, Nb_iter_stable, taille)[1])
    
    graphique(x,y,"Taille de la liste taboue", Nb_iter, Nb_iter_stable, "variable")  


def graphique(x, y, representation, Nb_iter, Nb_iter_stable, taille):
    """Fonction qui permet de tracer un graphique"""
    import matplotlib.pyplot as plt
    
    plt.figure()
    plt.plot(x, y)
    plt.title(f"Cout en fonction du {representation}\navec les paramètres Nb_iter = {Nb_iter}, Nb_iter = {Nb_iter_stable} et taille = {taille}")
    plt.xlabel(representation)
    plt.ylabel("Coût")
    plt.show()               # affiche la figure à l'écran    




if __name__ == "__main__":

    print(valeur_list(OF1, D1, V1, Solution_opt))
    print(valeur_list(OF1, D1, V1, Solution_naive))
    print(methode_taboue(Solution_naive, D1, OF1, V1, 20, 100,8))
    
    
    # Affichage des graphiques
    #print(test_nb_iter(Solution_naive, D1, OF1, V1, 100, 10000, 100, 100, 14))
    #print(test_taille_taboue(Solution_naive, D1, OF1, V1, 5000, 1000))
    #print(test_nb_iter_stable(Solution_naive, D1, OF1, V1, 1000, 60, 500, 20, 14))
    
    


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