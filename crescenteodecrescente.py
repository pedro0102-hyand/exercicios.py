input("Digite dois valores:")
n1=int(input())
n2=int(input())
while n1!=n2:
    if n1>n2:
        print("Decrescente")
    else:
        print("Crescente")
    print("Digite outros dois valores:")
    n1=int(input())
    n2=int(input())
