num = int(input("Digite um número: "))

primos = [True] * (num + 1)

primos[0:2] = [False, False]

for i in range(2, int((num**0.5)) + 1):
    if primos[i]:
        for j in range(i * i, num + 1, i):
            primos[j] = False

print([i for i, primo in enumerate(primos) if primo])