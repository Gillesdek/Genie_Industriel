from random import *
import operator
from cout import cout,valeur_list

### Données
D = [
[0, 9, 4, 9, 9, 4, 15, 4, 11, 9, 12],
[7, 0, 6, 11, 14, 5, 9, 12, 7, 7, 8],
[4, 13, 0, 9, 9, 14, 15, 12, 5, 14, 8],
[7, 5, 8, 0, 4, 15, 12, 5, 5, 7, 8],
[11, 8, 7, 13, 0, 11, 10, 11, 6, 5, 6],
[13, 4, 6, 15, 10, 0, 4, 10, 9, 7, 8],
[9, 4, 10, 15, 5, 13, 0, 14, 7, 15, 8],
[11, 7, 7, 10, 13, 15, 10, 0, 12, 11, 4],
[9, 6, 10, 10, 11, 10, 7, 7, 0, 5, 14],
[10, 10, 11, 9, 7, 9, 5, 7, 8, 0, 10],
[10, 9, 9, 15, 8, 6, 7, 9, 10, 10, 0]
]

OF =[
[2,1, 6, 3, 7, 5, 4, 8],
[6, 4, 5, 1, 8, 2, 7, 3],
[7, 0, 6, 4, 2, 3, 5, 1],
[6, 5, 3, 1, 4, 7, 2, 8],
[0, 2, 1, 5, 0, 3, 4, 0],
[1, 3, 2, 5, 4, 7, 6, 0],
[6, 0, 4, 5, 1, 2, 3, 0]
]

V = [4982, 2185, 2209, 2083, 4286, 4654, 3925]


def Générer(MaxPopul,n):
    """générer aléatoirement MaxPopul individus :
    Générer un ensemble de permutations aléatoires à partir d'une solution de base"""
    
    L= []
    for i in range(MaxPopul):
        D = [1,2,3,4,5,6,7,8,9]
        ind = []
        for j in range(n):
            k = choice(D)
            ind.append(k)
            D.remove(k)
        
        L.append(ind)
            
        
                    
    
    
    return L    

    


def Evaluer(Popul):
    """Calculer f(Popul(i)) pour i allant de 1 à MaxPolul"""
    T = []
    global OF
    global D
    global V
    for i in range(len(Popul)):
        
        T.append(valeur_list(OF,D,V,Popul[i]))
        
    
    
    
    return T





def Sélection(NbSelect,popul):
    """/sélectionner NbSelect (nombre paire) d'individus et retourner  /les indices dans TabSelect
    Methode de tournoi binaire"""
    TabSelect = []
    for i in range(NbSelect):
        n1 = randint(1,len(popul)-1)
        n2 = randint(1,len(popul)-1)
        if popul[n1] > popul[n2] :
            TabSelect.append(n1)
        else :
            TabSelect.append(n2)
    
    return TabSelect
        

def Croisement(PCrois,NbSelect,TabSelect,popul,coupure):
    """/avec une probabilité Pcrois, croiser tout couple
    /d'individus d'indice dans TabSelect et retourner NbEnfant
    /individus-enfants dans un tableau TabEnfant
    Croisement X1 sans répétitions """  
    
    # Changer coupure 
    Tabenfants = []
    p = random()
    if p <= PCrois :
        for i in range(0,NbSelect,2):
            parent1 = popul[TabSelect[i]]
            parent2 = popul[TabSelect[i+1]]
            enfant1=parent1[:coupure]
            enfant2=parent2[:coupure]
            for j in parent2:
                if j not in enfant1:
                    enfant1.append(j)
            for k in parent1:
                if k not in enfant2:
                    enfant2.append(k)
            Tabenfants.append(enfant1)
            Tabenfants.append(enfant2)
            
        
    
    
    return Tabenfants

def Mutation(PMut,TabEnfant):
    """/avec une faible probabilité Pmut, modifier aléatoirement
    /les enfants et retourner le résultat dans TabEnfant
    Permutation """
    for i in range(len(TabEnfant)):
        D = [0,1,2,3,4,5,6,7,8]
        p = random()
        if p < PMut :
            n1 = choice(D)
            D.remove(n1)
            n2 = choice(D)
            TabEnfant[i][n1],TabEnfant[i][n2] = TabEnfant[i][n2], TabEnfant[i][n1]
        
        
    return TabEnfant


def Remplacement(TabEnfant,Popul,MaxPopul):
    """remplacer les individus de TabEnfant dans la population (en
    préservant la meilleure solution !)
    exemple : garder dans Popul « les MaxPopul meilleure individus »
    parmi les(MaxPopul+NbEnfant)individus"""    
    newPopul = TabEnfant + Popul
    TabPopul_value = []
    cout = Evaluer(newPopul)
    for i in range(len(newPopul)):
        
        TabPopul_value.append((newPopul[i],cout[i]))
        
    
    
    TabPopul_value.sort(key = operator.itemgetter(1))
    
    TabPopul = []
    
    for couple in TabPopul_value: 
        TabPopul.append(couple[0])
        
    
    return (TabPopul[:MaxPopul])
    







### Paramètres
MaxPopul = 30
n = 9
NbSelect = 30
PCrois = 1
coupure = 4 # à changer
PMut = 0.3

### Algorithme 
Popul = Générer(MaxPopul,n)
Tabselect = Sélection(NbSelect,Popul)
arret = False
while n < 100 :
    
    
    
    Tabenfants = Croisement(PCrois,NbSelect,Tabselect,Popul,coupure)
    
    Tabenfants = Mutation(PMut,Tabenfants)
    
    newPopul = Remplacement(Tabenfants,Popul,MaxPopul)
    
    Popul = newPopul
    
    
    n += 1


print(newPopul)
print(Evaluer(Popul))

