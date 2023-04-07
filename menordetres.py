n1=int(input("Entre com o primeiro valor:"))
n2=int(input("Entre com o segundo valor:"))
n3=int(input("Entre com o terceiro valor:"))
if n1<n2 and n1<n3:
    menor=n1
elif n2<n3:
    menor=n2
else:
    menor=n3
print("O menor dos tres é:", menor)
