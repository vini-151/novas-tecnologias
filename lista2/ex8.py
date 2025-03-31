num = int(input("Digite o número (tem que ser <=3): "))
interacoes = num
primeiroTermo = 1
segundoTermo = 1


if num < 3:
    print("Erro: Insira um numero >= 3")
else:
    while(num - 2):
        termoAtual = primeiroTermo + segundoTermo
        primeiroTermo = segundoTermo
        segundoTermo = termoAtual
        num = num - 1
    print(f"o {interacoes}º termo de Fibonacci é {termoAtual}")
