n=int(input("Ordem da matriz:"))
matriz=[[0 for x in range(n)] for x in range(n)]
for i in range(0,n):
    for j in range(0,n):
        matriz[i][j]=int(input(f"Elemento[{i},{j}]:"))
print("Diagonal principal:")
for i in range(0,n):
    print(f"{matriz[i][j]}",end="")
print()
cont=0
for i in range(0,n):
    for j in range(0,n):
        if matriz[i][j]<0:
            cont+=1
print(f"Quantidade de negativos:{cont}")
