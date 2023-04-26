import random
resultados = [0] * 6
for i in range(100):
    resultado = random.randint(1, 6)
    resultados[resultado - 1] += 1
for i in range(6):
    print(f"O valor {i+1} foi obtido {resultados[i]} vezes.")

