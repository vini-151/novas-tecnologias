# Algorítimo para formulário de user

nome = input("Digite seu nome: \n")

idade = int(input("Digite sua idade: \n"))

altura = float(input("Digite sua altura: \n"))

peso = float(input("Digite seu peso: \n"))

estado_civil = input("""Informe seu estado civil
                     S - Solteiro
                     C - Casado
                     D - Divorciado
                     SE - Separado
                     V - Viúvo
""").upper()

imc = peso/altura**2



if imc < 17:
    pimc = "Muito abaixo do peso"
elif imc >= 17 and imc < 18.5:
    pimc = "Abaixo do peso"
elif imc >= 18.5 and imc < 25:
    pimc = "peso normal"
elif imc >= 25 and imc < 30:
    pimc = "Acima do peso"
elif imc >= 30 and imc < 35:
    pimc = "Obesidade 1"
elif imc >= 35 and imc < 40:
    pimc = "Obesidade severa"
else:
    pimc = "Obesidade mórbida"



match estado_civil:
    case 'S':
        pcivil = "Solteiro"
    case 'C':
        pcivil = "Casado"
    case 'SE':
        pcivil = "Separado"
    case 'D':
        pcivil = "Divorciado"
    case 'V':
        pcivil = "Viúvo"
    case _:
        pcivil = "Não foi possivel identificar estado civil"


print(f"""
    **********************************
    *     FORMULÁRIO DO USUÁRIO      *
    **********************************
      
    Nome: {nome}
    Idade: {idade} anos
    IMC: {imc}: {pimc}
    Estado: {pcivil}
      
""")