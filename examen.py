import random
from prettytable import PrettyTable

print("E.U.P. que realice la simulación 100 veces")

litros = [10, 12, 14, 16, 18, 20, 22, 24]
frecuencia = [2, 6, 10, 32, 13, 9, 6, 2]
total = sum(frecuencia)
costo = 15
venta = 35
aleatorio = []
litrosvendidos = []
costoPreparacion = []
ingreso = []
utilidad = []

for i in range(100):
    alegen = random.uniform(0, 1)
    aleatorio.append(alegen)

    acumulado = 0
    for j in range(len(frecuencia)):
        acumulado += frecuencia[j]
        if alegen < acumulado / total:
            litrosvendidos.append(litros[j])
            costos = litros[j] * costo
            costoPreparacion.append(costos)
            ingresos = litros[j] * venta
            ingreso.append(ingresos)
            utilidad.append(ingresos - costos)
            break


tabla = PrettyTable()

tabla.field_names = ["N", "#Alea", "Litros vendidos", "Costo de Preparación", "Ingreso x Venta", "Utilidad"]
for i in range(100):
    tabla.add_row([i+1, f"{aleatorio[i]:.4f}", litrosvendidos[i], costoPreparacion[i], ingreso[i], utilidad[i]])
print(tabla)

print("¿Cuánto debe tener en existencia? " + str(sum(litrosvendidos)))
print("¿Cuál será la ganancia esperada promedio? " + str(sum(utilidad) / 100))