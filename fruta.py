morango=float(input("Quantidade de morango em Kg:"))
maca=float(input("Quantidade de maca em Kg:"))
if morango<=5:
    p_mo=2.50
else:
    p_mo=2.20
if maca <=5:
    p_ma=1.80
else:
    p_ma=1.50
sem_desconto=(morango*p_mo)+(maca*p_ma)
if (morango+maca)>8 or sem_desconto>25:
    desconto=sem_desconto*-.1
else:
    desconto=0
com_desconto=sem_desconto-desconto
print("Valor a ser pago: R$ {:.2f}".format(com_desconto))
