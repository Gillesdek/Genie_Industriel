from genetique import genetique, Evaluer, Générer,Sélection
from data import D1,D2,OF1,OF2,V1,V2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    n1 = 9
    n2 = 29
      

   
    #print("1. Petit atelier: -------")
   
    #print("a. Nombre d'itération : ------")
    
    #MaxPopul = 50
    #NbSelect = 30
    #Nbiter = 150
    #Pmut = 0.3
    #Pcrois = 1
    #Popul_base = Générer(MaxPopul,n1)
    
    #Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,Pmut,Nbiter,D1,OF1,V1,afficher=True)
    
    #X = list(range(Nbiter))
    
    #plt.plot(X,L)
    #plt.show()
    
    #print("b. pourcentage d'obtention de la solution optimal: ------")
    #reussi = 0
    #S = 0
    #C = []
    #for i in range(50):
        #Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,Pmut,Nbiter,D1,OF1,V1,afficher=True)
        #S += cout[0]
        #C.append(cout[0])
        #if cout[0] == 1335193 :
            #reussi += 1
    
    #plt.plot(list(range(50)),C)
    #plt.show()
    #print("pourcentage de réussite : " + "---------" + str((reussi/50)*100) + "% " + "-----------")
    #print("Moyenne Générale : " + "----------------" + str(S/50) + "-------------")
    
    print("c. Influence de Pmut ----------------")
    # Paramètre fixe :
    
    MaxPopul = 50
    NbSelect = 30
    Nbiter = 150
    Pcrois = 1
    Popul_base = Générer(MaxPopul,n1)
    
    X = np.linspace(0,0.5,50)
    Y = []
    for x in X :
        Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,x,Nbiter,D1,OF1,V1)
        Y.append(cout[0])
    
    plt.plot(X,Y)
    plt.show()    
        
    print("conclusion : on choisi pmut entre 0.2 et 0.4 pour de meilleur résultat")    
    
    
    #print("2. Grand atelier: -------")
   
    #print("a. Nombre d'itérations : ------")
    
    #MaxPopul = 150
    #NbSelect = 100
    #Nbiter = 500
    #Pmut = 0.3
    #Pcrois = 1
    #Popul_base = Générer(MaxPopul,n1)
    
    #Popul,cout,L = genetique(Popul_base,MaxPopul,n2,NbSelect,Pcrois,Pmut,Nbiter,D2,OF2,V2,afficher=True)
    
    #X = list(range(Nbiter))
    
    #plt.plot(X,L)
    #plt.show()
    
    #print("b. Statistique: ------")
    #reussi = 0
    #S = 0
    #C = []
    #for i in range(50):
        #Popul,cout,L = genetique(Popul_base,MaxPopul,n1,NbSelect,Pcrois,Pmut,Nbiter,D1,OF1,V1,afficher=True)
        #S += cout[0]
        #C.append(cout[0])
        #if cout[0] == 1335193 :
            #reussi += 1
    
    #plt.plot(list(range(50)),C)
    #plt.show()
    #print("pourcentage de réussite : " + "---------" + str((reussi/50)*100) + "% " + "-----------")
    #print("Moyenne Générale : " + "----------------" + str(S/50) + "-------------")    
        
        
    
    
    
    
    
    
    
   
   