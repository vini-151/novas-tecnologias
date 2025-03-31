num = input("Digite um número: ")
contador = 0

for i in num: contador = contador + int(i)**3

if contador == int(num): print(f"{num} é número de Armstrong")
else: print(f"{num} não é número de Armstrong")