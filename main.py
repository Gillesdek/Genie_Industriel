from genetique import genetique, Evaluer, Générer,Sélection
from data import D1,D2,OF1,OF2,V1,V2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
      
    print("TEST ALGORITHME GÉNETIQUE -----------")
    print("1. Influence de Pmut ----------------")
    
    print("a. dans le petit atelier : -----------")
    # Parmètres fixes :
    
    n1 = 9
    MaxPopul = 50
    NbSelect = 30
    Pcrois = 1
    
    # La population de base pour tous les tests sera la même
    # Pour pouvoir comparer ce qui est comparable
    
    Popul_base = Générer(MaxPopul,n1)
    
    X = np.linspace(0,1,30) # valeurs suucessive de Pmut
    Y = []
    for x in X :
        Popul,cout = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,x,D1,OF1,V1)
        Y.append(cout[0]) # On mesure seulement le premier cout
    
    plt.plot(X,Y)
    plt.show()
    
       
    
    
    
    
    print("b. dans le grand atelier : -----------")
    # Paramètre fixe :
    
    n2 = 28
    MaxPopul = 150
    NbSelect = 100
    Pcrois = 1
    Popul_base = Générer(MaxPopul,n2)
    
    X = np.linspace(0,1,30)
    Y = []
    for x in X :
        Popul,cout = genetique(Popul_base,MaxPopul,n2,NbSelect,Pcrois,x,D2,OF2,V2)
        Y.append(cout[0])
    
    plt.plot(X,Y)
    plt.show()    
        
    
    
   