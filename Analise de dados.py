precos = [10.0, 10.5, 10.2, 11.0, 12.0, 12.9, 11.8, 10.5]
retornos = []
for i in range(1, len(precos)):
    retorno = precos[i] / precos[i - 1] - 1
    retornos.append(retorno)
print(retornos)    

media = sum(retornos)/len(retornos)
print(round(media * 100, 2), "%")