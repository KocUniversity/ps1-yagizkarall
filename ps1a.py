n=input('bir deger giriniz')
B=input('bir deger giriniz')
T=0
deger2=0
deger=0
p=[]
sure=0
for i in range(1,n+1):
  if i%2==0:
    x=2**i+1
    p.append(x)
  else:
    x=3**i+1
    p.append(x)
for j in range(len(p)):
   deger=p[j]**(n-1)
   n=n-1
   deger2=deger+deger2
while deger2*T<B:
  T+=1
print(T)