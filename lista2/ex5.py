string1 = input("Digite primeira frase: ").lower()

string2 = input("Digite segunda frase: ").lower()

string1 = string1.replace(" ", "")
string2= string2.replace(" ", "")


string1 = ''.join(sorted(string1))
string2 = ''.join(sorted(string2))

if string1 == string2:
    print(f"{string1} e {string2} São anagramas")
else:
    print(f"{string1} e {string2} Não são anagramas")


