n= input("Digite um número : ")
if n.isdigit():
    invertido = int(n[::-1])
    print(invertido)
else:
    print("Invalido")
