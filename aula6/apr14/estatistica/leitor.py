import csv


def ler_csv(caminho):
    with open(caminho, newline="", encoding="utf-8") as file:
        leitor = csv.DictReader(file)

        for linha in leitor:
            print(linha)
            for chave, valor in linha.items():
                if chave != "nome":
                    linha[chave] = valor







