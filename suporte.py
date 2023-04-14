op=1
total=0
esfera=0
limpeza=0
troca=0
quebrado=0
while op!=0:
    op=int(input("Identifique o mouse"))
    if op==0:
        break
    defeito=int(input("Informe o tipo de defeito(1;2;3;4)"))
    total+=1
    if defeito==1:
        esfera+=1
    elif defeito==2:
        limpeza+=1
    elif defeito==3:
        troca+=1
    elif defeito==4:
        quebrado+=1
print(total)
print("Situação\t\tQuantidade\t\tPercentual")
print("1- necessita da esfera\t\t", esfera, "\t\t", (esfera/total)*100, "%")
print("2- necessita de limpeza\t\t", limpeza, "\t\t", (limpeza/total)*100, "%")
print("3- necessita troca do cabo ou conector\t", troca, "\t\t", (troca/total)*100, "%")
print("4- quebrado ou inutilizado\t\t", quebrado, "\t\t", (quebrado/total)*100, "%")
