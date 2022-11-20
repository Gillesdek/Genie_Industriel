import csv

D1 = [
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

OF1 =[
[2,1, 6, 3, 7, 5, 4, 8],
[6, 4, 5, 1, 8, 2, 7, 3],
[7, 0, 6, 4, 2, 3, 5, 1],
[6, 5, 3, 1, 4, 7, 2, 8],
[0, 2, 1, 5, 0, 3, 4, 0],
[1, 3, 2, 5, 4, 7, 6, 0],
[6, 0, 4, 5, 1, 2, 3, 0]
]

V1 = [4982, 2185, 2209, 2083, 4286, 4654, 3925]

D2 = []

with open("Distance.csv") as Distance_file:
    
    read = csv.reader(Distance_file, delimiter = ";")
    
    for line in read :
        D2.append(list(map(int, line)))
        
OF2 = []
V2 = []
with open("OF.csv") as OF_file:
            
    of_read = csv.reader(OF_file, delimiter = ";")
    count_line = 0
    for line in of_read :
        if count_line != 0:
            ligne = []
            for m in line:
                if m == '':
                    ligne.append('0')
                else : 
                    ligne.append(m)
            OF2.append(list(map(int, ligne[1:])))
        count_line += 1

with open("V.csv") as V_file:
    
    readV = csv.reader(V_file, delimiter = ";")
    count = 0
    for line in readV :
         
        if count != 0:
            
            V2.append(int(line[0]))
        
        count += 1
        
        

