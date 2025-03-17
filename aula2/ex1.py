# x in x[::-1] -> confere se é palíndromo

nome = input("Digite seu nome\n")

if nome in nome[::-1]:
    print("Que legal, teu nome é um palíndromo")
else:
    print("Seu nome não é um palíndromo")