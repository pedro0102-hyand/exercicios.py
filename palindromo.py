sequency=input("Digite uma sequencia de caracteres:")
sequency=sequency.replace(" ", "").replace(",","").replace(".","").replace("!","").replace("?","")
if sequency==sequency[::-1]:
    print("É palindromo")
else:
    print("Nao é palindromo")
