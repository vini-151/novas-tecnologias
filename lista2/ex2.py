numLados = int(input("Insira o número de lados (1 - 20): "))

for i in range(numLados):
    if i == 0 or i == numLados - 1:
        print("* " * numLados)
    else:
        print("* " + "  " * (numLados - 2) + "*")