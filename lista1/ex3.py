print("Digite os valores de P1 (X1 e Y2) e P2 (X2 e Y2) ")

x1 = float(input("X1: "))
x2 = float(input("X2: "))
y1 = float(input("Y1: "))
y2 = float(input("Y2: "))

dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

print(f"A distância entre os dois pontos é de {dist}")
