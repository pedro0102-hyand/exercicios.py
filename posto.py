combustivel=input("Me diga o combustivel de sua preferencia (A, G):")
litro=float(input("Digite a quantidade de litros que deseja:"))
if combustivel=="A":
    preco=1.90
    if litro <=20:
        desconto=litro*0.03
    else:
        desconto=litro*0.05
else:
    preco=2.50
    if litro <=20:
        desconto=litro*0.04
    else:
        desconto=litro*0.06
valor_sem_desconto=litro*preco
valor_com_desconto=valor_sem_desconto-desconto
print("Valor a ser pago: R$ {:.2f}".format(valor_com_desconto))
