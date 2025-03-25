num = int(input("Digite um número"))
i = 1
somatorio = 0

for i in range(num):
    if i % 2 == 0:
        somatorio = somatorio + i


print(f"A soma dos pares é {somatorio}")
