n=int(input("Entre com a quantidade de termos:"))
sum=0
m=1
for i in range(1,n+1):
    sum=sum+i/m
    m=m+2
print(sum)
