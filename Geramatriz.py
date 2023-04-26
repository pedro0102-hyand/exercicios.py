import random
n=int(input("informe o tamanho:"))
mat=[[random.randint(0,9) for j in range(n)] for i  in range(n)]
for i in range(n):
    for j in range(n):
        print(f"{ mat [i] [j] }",end=" ")
    print()
