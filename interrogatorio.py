print("Responda as perguntas de maneira adequada")
p1=input("Voce ligou para a vitima ?")
p2=input("Voce tava no local do crime?")
p3=input("Mora perto da vitima ?")
p4=input("Já deveu dinheiro para a vitima?")
p5=input("Já trabalhou com a vitima ?")
positivo=0
if p1.lower()=="Yes":
    positivo+=1
if p2.lower()=="Yes":
    positivo+=1
if p3.lower()=="Yes":
    positivo+=1
if p4.lower()=="Yes":
    positivo+=1
if p5.lower()=="Yes":
    positivo+=1

if positivo==2:
    print("Suspeito")
elif positivo>=3 and positivo<=4:
    print("Cúmplice")
elif positivo==5:
    print("Assassino")
else:
    print("Inocente")
