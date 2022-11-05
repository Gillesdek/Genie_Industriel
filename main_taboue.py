from Taboue import methode_taboue, test_taille_taboue, test_nb_iter, test_nb_iter_stable
from data import D1,D2,OF1,OF2,V1,V2
from cout import valeur_list

import time

if __name__ == "__main__":
    
    print("TEST ALGORITHME MÉTHODE DU TABOUE -----------")
    print("1. Dans le petit Atelier ----------------")
    
    # On initialise la méthode avec une solution naive :
    Solution_naive = [4, 3, 7, 2, 1, 9, 8, 5, 6]
    print(valeur_list(OF1, D1, V1, Solution_naive))
    print(methode_taboue(Solution_naive, D1, OF1, V1, 1000, 500, 8))
    
    
    print("a. Influence de la taille de la liste taboue : -----------")
    print(test_taille_taboue(Solution_naive, D1, OF1, V1, 50, 30))
    
    
       
       
    print("b. Influence du nombre d'itérations : -----------")
    print(test_nb_iter(Solution_naive, D1, OF1, V1, 10, 200, 10, 30, 7))
        
    
    print("c. Influence du nombre d'itérations stables : -----------")
    print(test_nb_iter_stable(Solution_naive, D1, OF1, V1, 50, 5, 105, 10, 7))
        
    
    
    
    
    print("2. Dans le grand Atelier ----------------")
    
    # On initialise la méthode avec une solution naive :
    Solution_naive2 = [i+1 for i in range(len(D2))]        # Numéro de la machine = Emplacement de la machine
    print(valeur_list(OF2, D2, V2, Solution_naive2))
    print(methode_taboue(Solution_naive2, D2, OF2, V2, 1000, 500, 8))
    
    
    print("a. Influence de la taille de la liste taboue : -----------")
    print(test_taille_taboue(Solution_naive2, D2, OF2, V2, 5, 5))
    
    
    print("b. Influence du nombre d'itérations : -----------")
    print(test_nb_iter(Solution_naive2, D2, OF2, V2, 1, 100, 2, 10, 8))
        
    
    print("c. Influence du nombre d'itérations stables : -----------")
    print(test_nb_iter_stable(Solution_naive2, D2, OF2, V2, 100, 10, 100, 10, 8))  