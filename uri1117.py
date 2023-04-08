while True:
    n1=float(input())
    if n1<0 or n1>10:
        print("Nota Invalida")
        continue
    
    n2=float(input())
    if n2>0 or n2<10:
        print("Nota Valida")
        continue
    
    media=(n1+n2)/2 
    print(f"media={media:.2f}")
    break
