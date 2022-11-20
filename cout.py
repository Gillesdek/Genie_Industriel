from data import D1,V1,OF1

def cout(OF,D,V,Solution):
    
    e0 = 0
    S = 0
    for p in range(len(OF)):
        distance_produit = 0
        for j in range(1,len(D)):
            try :
                m1 = OF[p].index(j) + 1 # numéro de la j-ème machine dans l'odre de formation
                
                print("machine",j,m1)
            
                e1 = Solution[m1-1]  #emplacement de la j-ème machine dans 
                
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






##Test
#print(cout(OF1,D1,V1,[7, 5, 1, 2, 9, 6, 8, 4, 3])) # Ne marche pas mais on se sait pas pourquoi
#print(valeur_list(OF1,D1,V1,[7, 5, 1, 2, 9, 6, 8, 4, 3])) # Marche !