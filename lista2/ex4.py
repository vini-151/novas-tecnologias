nome = input("Digite seu nome\n").lower()

nome = nome.replace(" ", "")

nome = nome.replace("á", "a")
nome = nome.replace("ã", "a")
nome = nome.replace("â", "a")

nome = nome.replace("é", "e")
nome = nome.replace("ê", "e")

nome = nome.replace("í", "i")

nome = nome.replace("õ", "o")
nome = nome.replace("ô", "o")

if nome == nome[::-1]:
    print("Que legal, teu nome é um palíndromo")
else:
    print("Seu nome não é um palíndromo")

