import datetime


#data = "14-5-2025"
#hoje = datetime.datetime.strptime(data, "%d-%m-%Y")
#print(hoje)

def formatar_data(dia, mes, ano):
    data = datetime.date(ano,mes,dia)
    print(data.strftime("%d/%m/%Y"))

formatar_data(14,4,2025)
formatar_data(ano=2025,mes=5,dia=5)