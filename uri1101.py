while True:
    x,y=map(int, input().split())
    if x<=0 or y<=0:
        break
    if x>y:
        x,y = y,x        
    soma=sum(range(x,y+1))
    sequencia=' '.join(str(i) for i in range(x,y+1))
    print(f"{sequencia} Soma={soma}")
