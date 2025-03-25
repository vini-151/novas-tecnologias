import random
num = random.randrange(1, 100)

while 1 < 2:
    guess = int(input("Insira um numero: "))
    if guess == num:
        print("Parabens, você ganhou!")
        break
    elif guess < num:
        print("O numero sorteado é maior que o inserido")
    else:
        print("O numero sorteado é menor que o inserido")