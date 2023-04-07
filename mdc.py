a=int(input("Informe o valor de a:"))
b=int(input("Informe o valor de b:"))
menor=min(a,b)
resposta=1
for i in range(1,menor+1):
    if a%i==0 and b%i==0:
        resposta=i
print("O mmc é:", resposta)
