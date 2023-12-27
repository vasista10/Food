import csv 
file=open('p3.csv') 
data=list(csv.reader(file))[1:]
 
concepts=[] 
target=[] 

for i in data: 
    if len(i)>=1:    
        concepts.append(i[:-1]) 
        target.append(i[-1]) 
    else:
        print("Invalid data formatin csv file")
        
specific_h = concepts[0].copy() 
general_h= [['?' for i in range(len(specific_h))] 
for i in range(len(specific_h))] 
for i,h in enumerate(concepts): 
    if target[i]=="yes": 
       for x in range(len(specific_h)): 
           if h[x]!=specific_h[x]: 
               specific_h[x]='?' 
               general_h[x][x] = '?' 
           if target[i]=="no": 
              for x in range(len(specific_h)): 
                  if h[x]!= specific_h[x]: 
                      general_h[x][x]=specific_h[x] 
                  else: 
                    general_h[x][x]='?' 
indices=[i for i,val in enumerate(general_h) if val == ['?','?','?','?','?','?']] 
for i in indices: 
    general_h.remove(['?','?','?','?','?','?']) 
    
print("Final Specific:",specific_h,sep="\n")
print("Final General:",general_h,sep="\n")