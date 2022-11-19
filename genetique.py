from random import *
import operator
from cout import cout,valeur_list
from data import D1,D2,OF1,OF2,V1,V2
import csv



def Générer(MaxPopul,n):
    """générer aléatoirement MaxPopul individus :
    Générer un ensemble de permutations aléatoires à partir d'une solution de base"""
    
    L= []
    for i in range(MaxPopul):
        D = list(range(1,n+1))
        ind = []
        for j in range(n):
            k = choice(D)
            ind.append(k)
            D.remove(k)
        
        L.append(ind)
            
        
                    
    
    
    return L    

    


def Evaluer(Popul,D,OF,V):
    """Calculer f(Popul(i)) pour i allant de 1 à MaxPolul"""
    T = []
    for i in range(len(Popul)):
        
        T.append(valeur_list(OF,D,V,Popul[i]))
        
    
    
    
    return T





def Sélection(NbSelect,popul,OF,D,V):
    """/sélectionner NbSelect (nombre paire) d'individus et retourner  /les indices dans TabSelect
    Methode de tournoi binaire"""
            
    TabSelect = []
    List_index = list(range(len(popul)))
    for i in range(NbSelect):
        n1 = choice(List_index)
        n2 = choice(List_index)
        if valeur_list(OF,D,V,popul[n1]) > valeur_list(OF,D,V,popul[n2]) :
            TabSelect.append(n1)
            List_index.remove(n1)
        else :
            TabSelect.append(n2)
            List_index.remove(n2)
        
    
    return TabSelect
        

def Croisement(PCrois,NbSelect,TabSelect,popul):
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
            coupure = randint(1,len(parent1))
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

def Mutation(PMut,TabEnfant,n):
    """/avec une faible probabilité Pmut, modifier aléatoirement
    /les enfants et retourner le résultat dans TabEnfant
    Permutation """
    for i in range(len(TabEnfant)):
        D = list(range(n))
        p = random()
        if p < PMut :
            n1 = choice(D)
            D.remove(n1)
            n2 = choice(D)
            TabEnfant[i][n1],TabEnfant[i][n2] = TabEnfant[i][n2], TabEnfant[i][n1]
        
        
    return TabEnfant


def Remplacement(TabEnfant,Popul,MaxPopul,D,OF,V):
    
    """remplacer les individus de TabEnfant dans la population (en
    préservant la meilleure solution !)
    exemple : garder dans Popul « les MaxPopul meilleure individus »
    parmi les(MaxPopul+NbEnfant)individus"""    
    newPopul = TabEnfant + Popul
    TabPopul_value = []
    cout = Evaluer(newPopul,D,OF,V)
    for i in range(len(newPopul)):
        
        TabPopul_value.append((newPopul[i],cout[i]))
        
    
    
    TabPopul_value.sort(key = operator.itemgetter(1))
    
    TabPopul = []
    
    for couple in TabPopul_value: 
        TabPopul.append(couple[0])
        
    
    return (TabPopul[:MaxPopul])
    







def genetique(Popul,MaxPopul,n,NbSelect,PCrois,PMut,Nbiter,D,OF,V,afficher = False):
    
    
    
    arret = False
    i = 0
    L = []
    while i < Nbiter :
        
        
        Tabselect = Sélection(NbSelect,Popul,OF,D,V)
        
        
        Tabenfants = Croisement(PCrois,NbSelect,Tabselect,Popul)
        
        Tabenfants = Mutation(PMut,Tabenfants,n)
        
        newPopul = Remplacement(Tabenfants,Popul,MaxPopul,D,OF,V)
        
        Popul = newPopul
        
        L.append(Evaluer(Popul[0:1],D,OF,V))
        
        i += 1
    if afficher :
        print("Populutation finale : ", Popul)
        print("cout des 3 premiers : ", Evaluer(Popul[:3],D,OF,V)) 
    
    return Popul,Evaluer(Popul[:3],D,OF,V),L




