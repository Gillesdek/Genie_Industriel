from genetique import genetique, Evaluer, Générer,Sélection
from data import D1,D2,OF1,OF2,V1,V2


if __name__ == "__main__":
      
    print("TEST ALGORITHME GÉNETIQUE -----------")
    print("dans le petit atelier : ")
    Popul_base = Générer(50,9)
    Popul,cout = genetique(Popul_base,50,9,30,1,0.3,D1,OF1,V1)

       
    
    
    
    
    print("dans le grand atelier : ")
    Popul_base = Générer(100,28)
    Popul,cout = genetique(Popul_base,100,28,70,1,0.5,D2,OF2,V2)
        
    
    
   