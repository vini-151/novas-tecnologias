num = int(input("Insira um número: "))
contador = 0

if num < 0:
    print("Erro, número tem que ser positivo")
else:
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        contador += 1
        print(f"Passo {contador}: {num}")


print(f"Total de passos necessários: {contador}")