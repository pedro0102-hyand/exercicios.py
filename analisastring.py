frase=input("Digite uma frase:")
total=0
maiusculas=0
minusculas=0
for letras in frase:
    if letras.isalpha():
        total+=1
        if letras.isupper():
            maiusculas+=1
        else:
             minusculas+=1
print("Quantidade total:", total)
print("Maiusculas:", maiusculas)
print("Minusculas:", minusculas)
if maiusculas==0:
    print("Nao possui letras maiusculas")
