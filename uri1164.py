n=int(input())
for i in range(n):
    x=int(input())
    divs=[d for d in range(1,x) if x%d==0]
    if sum(divs)==x:
        print("É perfeito")
    else:
        print("Nao é perfeito")
