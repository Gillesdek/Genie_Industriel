from genetique import genetique, Evaluer, Générer,Sélection
from data import D1,D2,OF1,OF2,V1,V2


if __name__ == "__main__":
      
    
    Popul = genetique(100,28,70,1,0.5,D2,OF2,V2)
    print("Populutation finale : ", Popul)
    print("cout des 3 premiers : ", Evaluer(Popul[:3],D2,OF2,V2))
    
   