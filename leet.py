leet = {
    'a': '4',
    'e': '3',
    'g': '6',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7'
}
text=input("digite o texto a ser convertido:")
text_leet=""
for caractere in text:
    if caractere in text:
        if caractere.lower() in leet:
            text_leet+=leet[caractere.lower()]
        else:
            text_leet+=caractere
print("Texto em leet speak: " + text_leet)


