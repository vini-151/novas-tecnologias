frase = input("Entre com uma frase: ").lower()

print(f"Na frase \"{frase}\" tem:\n",
      f"Vogal: a: {frase.count('a')+frase.count('ã')+frase.count('á')+frase.count('â') }\n",
      f"Vogal: e: {frase.count('e') }\n",
      f"Vogal: i: {frase.count('i') }\n",
      f"Vogal: o: {frase.count('o') }\n",
      f"Vogal: u: {frase.count('u') }\n")