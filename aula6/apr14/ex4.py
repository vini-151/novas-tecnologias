import time



def sequencia(n, memo = {}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        resultado = memo[n]
    else: 
        resultado =  sequencia (n - 1, memo) + 2 * sequencia(n - 2, memo)
        memo[n] = resultado
    return resultado

n = int(input("Insira o valor de n: "))

t1 = time.time()

print(f"T({n}) = {sequencia(n)}")

t2 = time.time()

print(f"{t2-t1}")