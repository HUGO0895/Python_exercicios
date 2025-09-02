p='The Python Software Foundation and the global Pythoncommunity welcome and encourage participation by everyone. Our community is based onmutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, andwhatever your background, we welcome you.'

p=p.lower()

p=p.replace(',','')

p=p.replace('.','')
p=p.split()
k=[]

for x in p:
    for y in x:
        if x[0] in 'python':
            k.append(x)
            break
        elif x[-1] in 'python':
            k.append(x)
            break

            



print(k)