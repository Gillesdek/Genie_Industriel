from random import sample

def Générer(MaxPopul,Popul):
    """/générer aléatoirement MaxPopul individus dans un tableau Popul"""
    return sample(Popul, 3)
    


def Evaluer(Popul):
    """Calculer f(Popul(i)) pour i allant de 1 à MaxPolul"""
    
    pass





def Sélection(NbSelect,TabSelect):
    """/sélectionner NbSelect (nombre paire) d'individus et retourner  /les indices dans TabSelect"""
    pass


def Croisement(PCrois,TabSelect,NbSelect,TabEnfant,NbEnfant):
    """/avec une probabilité Pcrois, croiser tout couple
    /d'individus d'indice dans TabSelect et retourner NbEnfant
    /individus-enfants dans un tableau TabEnfant"""    
    pass

def Mutation(PMut,TabEnfant,NbEnfant):
    """/avec une faible probabilité Pmut, modifier aléatoirement
/les enfants et retourner le résultat dans TabEnfant"""
    pass


def Remplacement(TabEnfant,Popul):
    """/remplacer les individus de TabEnfant dans la population (en
    /préservant la meilleure solution !)
    /exemple : garder dans Popul « les MaxPopul meilleure individus »
    /parmi les(MaxPopul+NbEnfant)individus"""    
    pass



