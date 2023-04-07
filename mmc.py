a=int(input("Digite o valor de a:"))
b=int(input("Digite o valor de b:"))
maior=max(a,b)
resultado=maior
while resultado%a!=0 or resultado%b!=0 :
    resultado+=maior
print("O mmc entre estes dois numeros é :", resultado)
