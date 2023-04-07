nome=input("Nos diga o seu nome :")
matricula=input("Digite aqui a sua matricula:")
freq=float(input("Nos informe a sua frequencia:"))
n1=float(input("n1:"))
n2=float(input("n2:"))
n3=float(input("n3:"))
n4=float(input("n4:"))
media=(n1+n2+n3+n4)/4
if media>=5.0 and freq >=0.75:
    situacao="APROVADO"
elif media>=5.0 and freq<0.75:
    situacao="REPROVADO POR FREQUENCIA"
elif media<5.0 and freq>=0.75:
    situacao="REPROVADO POR MEDIA"
else:
    situacao="REPROVADO"
print("\n===== BOLETIM ======")
print("Nome:", nome)
print("Matricula:", matricula)
print("Frequencia:{:.2f}".format(freq))
print("Média:{:.2f}".format(media))
print("Situacao:", situacao)
