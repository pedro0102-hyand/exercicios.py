import os
palavra = 'paralelepipedo'
corretos = ''
tentativas = 0
while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra in palavra:
        corretos += letra
    formada = ''
    for letra_secreta in palavra:
        if letra_secreta in corretos:
            formada += letra_secreta
        else:
            formada += '*'
    print('Palavra formada:', formada)
    if formada == palavra:
        os.system('clear')
        print('VOCÊ GANHOU')
        print(palavra)
        print('Tentativas:', tentativas)
        corretos = ''
        tentativas = 0
