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

def cout(OF,D,V,Solution):
    
    e0 = 0
    S = 0
    for p in range(len(OF)):
        distance_produit = 0
        for j in range(1,len(D)):
            try :
                m1 = OF[p].index(j) + 1 # numéro de la j-ème machine 
                
                print("machine",j,m1)
            
                e1 = Solution[m1-1]  #emplacement de la j-ème machine
                
                print("emplacement",j,e1)
                
                distance_produit += D[e0][e1]
                print("distance",j,D[e0][e1])
                
                e0 = e1                
            except :
    
                distance_produit += 0
        
        distance_produit += D[e0][10]
        print("dernière machine :",m1)
        print("emplacement de la dernière machine :",e0)
        print("Distance dernière machine - sortie",D[e0][10])
        
        
        S += distance_produit * V[p]
                
            
            
    
    return S


def valeur_list(F,D,V,perm):
    
    distance_machines = []  # liste qui contient la suite des distance entre les machine pour chaque produit (liste de listes)
    for i in range(0,len(V)): # i produit (0 produits)
        distance_machines_i = []
        for j in range(1,len(D)): # emplacements dans la fabrication ! (première machine utilisée, deuxième,...)
            if j == 1: # si on est à la première machine dans l'ordre de fabrication
                z = F[i].index(j) # on récupère la place de la première machine dans la fabrication pour le produit i
                distance_machines_i.append(D[0][perm[z]]) # on prend la distance entre l'entrée et la première machine
                y = F[i].index(j+1) #idem avec la deuxième machine (c'est ce qu'on avait oublié)
                distance_machines_i.append(D[perm[z]][perm[y]])
            elif j+1 not in F[i]: # si il n'y a pas de machine suivante on va vers la sortie
                x = F[i].index(j) # on récupère la place de la dernière machine dans la fabrication pour le produit i
                distance_machines_i.append(D[perm[x]][len(D)-1]) # on prend la distance entre la dernière machine et la sortie
                break #on sort
            else:
                a = F[i].index(j) 
                b = F[i].index(j+1) 
                distance_machines_i.append(D[perm[a]][perm[b]])

        distance_machines.append(distance_machines_i)
    somme = 0
    for t in range (0,len(V)):
        somme += sum(distance_machines[t]) * V[t]
    return somme







