def criador(multplica):
    def mult(numero):
        return numero*multplica
    return mult
duplica=criador(2)
triplica=criador(3)
quadruplica=criador(4)
print(duplica(2))
print(triplica(2))
print(quadruplica(2))
