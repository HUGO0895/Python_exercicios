import random
l=[]
k=[]
for x in range(10):
    random.randint(1,100)
    l.append(random.randint(1,100))
    random.randint(1,100)
    k.append(random.randint(1,100))

j=[]
p=0
while x <19:
      j.append(l[p])
      j.append(k[p])
      p+=1
      x+=1

print(l)
print(k)
print(j)
       