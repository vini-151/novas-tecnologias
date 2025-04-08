palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

anagramas = {}

for palavra in palavras:
    if tuple(sorted(palavra)) in anagramas:
        anagramas[tuple(sorted(palavra))].append(palavra)
    else:
        anagramas[tuple(sorted(palavra))] = [palavra]

for chave, valor in anagramas.items():
    print(f"{chave} : {valor}")