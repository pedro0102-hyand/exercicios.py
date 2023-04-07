n=int(input("Digite a quantidade de numeros a serem escolhidos:"))
numeros=[]
for i in range(n):
    valor=int(input("Entre com o valor"+str(i+1)+":"))
    numeros.append(valor)
for num in numeros():
    print("Tabuada do numero:", num)
    for i in range(11):
        print(num,"x",i,"=", num*i)
        print()
