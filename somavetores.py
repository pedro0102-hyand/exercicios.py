n=int(input("Entre com a quantidade de valores:"))
vetor=[0]*n
for i in range(n):
    vetor[i]=float(input(f"Digite o {i+1}º numero:"))
print("Elementos do vetor:")
for elemento in vetor:
    print(elemento)
soma=sum(vetor)
media=soma/n
print(soma)
print(media)
