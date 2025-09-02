n=int(input("digite um numero para verificarmos se ele é primo:"))
x=2
d=0
while x <=n:
    if n%x==0:
        d=d+1 
    x=x+1    
        
if d>=2:
  print('Não é primo') 
else:
   print('primo')   