def media_pond(**kwargs):
    m = 0
    for peso, valor in kwargs.items():
        m += int(peso) * valor
    return m/len(kwargs.values())
    
dic = {'2':6, '8':6, '3':9}

print(media_pond(**dic))