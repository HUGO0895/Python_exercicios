x=33087
y=18644
l=[]
count=0
for c in range(y,x+1):
    while c!=0:
        p=c%10
        c=c//10
        l.append(p)
    if 2 in l and not 7 in l:
        count+=1
        
    
        
    l=[]
    
print(count)
     
    
