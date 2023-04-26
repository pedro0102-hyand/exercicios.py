while True:
    name=input("Name:")
    if name=="" :
        break
    saltos=[]
    for i in range(5):
        distancia=float(input(f"Diga a distancia do {i+1} salto: "))
        saltos.append(distancia)
        media=sum(saltos)/len(saltos)
    print(f"\nResultado final:\nAtleta: {name}")
    print(f"Saltos : {'- '.join(str(s)+'m' for s in saltos)}")
    print(f"Media dos saltos:{media:.1f} m\n")
