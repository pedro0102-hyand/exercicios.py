def soma (x,y):
    return x+y
def mult (x,y):
    return x*y
def build (funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna
soma_com_dois=build(soma,2)
multiplica_por_seis=build(mult,6)
print(soma_com_dois(4))
print(multiplica_por_seis(7))
