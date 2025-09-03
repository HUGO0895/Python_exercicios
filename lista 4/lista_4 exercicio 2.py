import random
l=[]
m=[]
n=[]
for x in range(20):
            m.append(random.randint(1,100))
            
for x in m:
        if x%2==0:
                l.append(x)
        else:
                n.append(x)
print(f'lista principal:{m}')
print(f'lista secundaria(par) {l}')
print(f'lista secundaria (impar): {n}')

