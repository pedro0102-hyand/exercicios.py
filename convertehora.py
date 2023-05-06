def conv_hora(hora,minuto):
    if hora==0:
        hora=12
        periodo='A'
    elif hora<12:
        periodo='A'
    elif hora==12:
        periodo='P'
    else:
        hora-=12
        periodo='P'
        return hora,minuto,periodo
def imprime(hora,minuto,periodo):
    print(f"{hora}:{minuto:02d}{periodo}.M.")
while True:
    hora=int(input("Digite a hora:"))
    minuto=int(input("Digite o minuto:"))
    hora_12, minuto,periodo=conv_hora(hora,minuto)
    imprime(hora_12,minuto,periodo)
    opcao=int("Deseja converter outro ?")
    if opcao.upper()=='N':
        break
