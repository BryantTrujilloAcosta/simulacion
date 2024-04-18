def generar_pseudoaleatorio(r1, r2, iteraciones):
    numeros_generados = []
    for i in range(iteraciones):
        producto = r1 * r2
        r1 = r2
        resultado = int(producto % 10000) / 10000
        r2 = resultado
        numeros_generados.append(r2)
        print(f"X{i+1}: {r2}")
    return numeros_generados

def calcular_media(numeros_generados):
    return sum(numeros_generados) / len(numeros_generados)

if __name__ == "__main__":
    r1 = int(input("Introduce la primera semilla de 4 dígitos: "))
    r2 = int(input("Introduce la segunda semilla de 4 dígitos: "))
    iteraciones = 1000

    numeros_generados = generar_pseudoaleatorio(r1, r2, iteraciones)
    media = calcular_media(numeros_generados)
    print(f"\nLa media de los {iteraciones} números pseudoaleatorios generados es: {media}")
