n=int(input("Informe a quantidade de numeros para casos de teste:"))
for i in range(n):
    pa, pb, g1, g2 = map(float, input().split())
    pa, pb =  int(pa), int(pb)
    years=0


    while pa<=pb:
        pa+=int(pa*(g1/100))
        pb+=int(pb*(g2/100))
        years+=1


        if years>100:
            print("Mais de 1 seculo")
            break


    if years<=100:
            print(f"{years} anos")
