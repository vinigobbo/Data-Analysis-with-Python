import numpy as np
etf = np.array([443.90, 440.60, 442.50, 443.66, 444.30, 445.61, 448.06])

hoje = etf[1:]
ontem = etf [:-1]

retorno = hoje / ontem - 1
retorno = retorno * 100
print("Retornos:", np.round(retorno, 2))

media = retorno.mean()
volatilidade = retorno.std() 

print("Media:", np.round(media, 2), "%")
print("Volatilidade:", np.round(volatilidade, 2), "%")