from genetique import genetique, Evaluer, Générer,Sélection,Générer_sdb
from data import D1,D2,OF1,OF2,V1,V2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    
    # Parametre de taille des permutaions
    n1 = 9 # petite instance
    n2 = 29 #Grande instance
    
    
      

   
    print("1. Petit atelier: -------")
   
    print("a. Affichage du cout à chaque itération: ------")
    
    
    #Paramètres
    MaxPopul = 50
    NbSelect = 30
    Nbiter = 150
    Pmut = 0.3
    Pcrois = 1
    
    # Population de base qui restera la même pour tous les tests
    Popul_base = Générer_sdb(MaxPopul,n1,D1,OF1,V1)
    
    # Lancement de l'algorithme
    Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,Pmut,Nbiter,D1,OF1,V1,afficher=True,doublons=False)
    
    X = list(range(Nbiter))
    
    # Affichage de la courbe
    plt.plot(X,L)
    plt.show()
    
    print("b. Performances : ------")
      
    
    NbTest = 50
    reussi = 0
    S = 0
    C = []
    Optimal = 1335193
    # Test sans doublons dans la pop
    print("Sans doublons dans la population : ")
    for i in range(NbTest):
        Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,Pmut,Nbiter,D1,OF1,V1,afficher=False,doublons=False)
        S += cout[0]
        C.append(cout[0])
        if cout[0] == Optimal :
            reussi += 1
    print("pourcentage de réussite : " + str((reussi/NbTest)*100) + "%") 
    print("Moyenne Générale : " + str(S/NbTest))
    

    
    # Test avec doublons ( pas de gestion des doublons )
    
    reussi = 0
    S = 0
    C = []    
    print("Avec doublons dans la population : ")
    for i in range(NbTest):
        Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,Pmut,Nbiter,D1,OF1,V1,afficher=False,doublons=True)
        S += cout[0]
        C.append(cout[0])
        if cout[0] == Optimal :
            reussi += 1    

    print("pourcentage de réussite: " +  str((reussi/NbTest)*100) + "% ")
    print("Moyenne Générale : " + str(S/NbTest))
    
    print("c. Influence de Pmut ----------------")
    
    
    X = np.linspace(Pmin,Pmax,Nbpoint)
    Y = []
    for x in X :
        Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,x,Nbiter,D1,OF1,V1,doublons=False)
        Y.append(cout[0])
    
    plt.plot(X,Y)
    plt.show()    
        
    
    
    
    print("2. Grand atelier: -------")
   
    print("a. Affichage du coût pour chaque itération : ------")
    
    MaxPopul = 150
    NbSelect = 100
    Nbiter = 500
    Pmut = 0.2
    Pcrois = 1
    Popul_base = Générer_sdb(MaxPopul,n2,D2,OF2,V2)
    
    Popul,cout,L = genetique(Popul_base,MaxPopul,n2,NbSelect,Pcrois,Pmut,Nbiter,D2,OF2,V2,afficher=True,doublons=False)
    
    X = list(range(Nbiter))
    
    plt.plot(X,L)
    plt.show()
    
    print("b. Performances")
    
    continuer = str(input("le temps d'execution de cette partie et très longue (20 fois plus long que l'execution précédente) \nVoulez-vous tout de même l'executer ? (O/N) \n"))
                    
    
    if continuer == 'O' :
       
        
        T = Evaluer(Popul_base,D2,OF2,V2)
        print("cout moyen de la population de base : ",sum(T)/len(T))
        
        NbTest = 10 
        
        # Calcul des différents indicateurs : moyenne et minimum
        S = 0
        G = []
        for i in range(NbTest):
                Popul,cout,L = genetique(Popul_base,MaxPopul,n2,NbSelect,Pcrois,Pmut,Nbiter,D2,OF2,V2,afficher=True,doublons=True)
                S += cout[0]
                G.append(cout[0])
        
        print('avec doublons : ')
        print("Moyenne : ", S/NbTest)
        print("Minimum : ", min(G))
        
        S = 0
        G = []
        
        for i in range(NbTest):
            Popul,cout,L = genetique(Popul_base,MaxPopul,n2,NbSelect,Pcrois,Pmut,Nbiter,D2,OF2,V2,afficher=True,doublons=False)
            S += cout[0]
            G.append(cout[0])
        print("sans doublon : ")
        print("Moyenne : ", S/NbTest)
        print("Minimum : ", min(G))
        
    else:
        print("Merci pour votre réponse les résultats du test précédent sont dans le rapport partie 3.3.4.2")
            
           
    
    
    
        
        
    
    
    
    
    
    
    
   
   