def numeros_aleatorios(cantidad):
    numeros = [round(random.uniform(0,1),5) for _ in range(cantidad)]
    return numeros




numeros = ["3","2","1"]

print(len(numeros))