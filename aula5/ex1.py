def exp(a,b=0):
    """
    Funcao para calcular o exponencial de a elevado a b
    """
    return a**b

print(exp(2,10))

print(exp.__doc__)

expV2 = lambda a,b:a**b

print(expV2(2,10))