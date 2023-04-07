import math
base=float(input("Digite o valor da base do retangulo:"))
altura=float(input("Digite o valor da altura do retangulo:"))
perimetro=(base*2)+(altura*2)
area=base*altura
diagonal=math.sqrt(base**2 + altura**2)
print(f"Perimetro={perimetro:.2f}")
print(f"Area={area:.2f}")
print(f"Diagonal={diagonal:.4f}")
