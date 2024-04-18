import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Datos de la tabla
consultas = [0, 1, 2, 3, 4, 5]
frec_acumulada = [0.05, 0.15, 0.35, 0.65, 0.85, 1]
# Simulación de Monte Carlo
N = int(input("¿cuantas veces desea realizar la simulación? "))
simulaciones = []
aleatorios = []
for i in range(N):
    aleatorio = random.random()
    aleatorios.append(aleatorio)
    for j in range(len(frec_acumulada)):
        if aleatorio < frec_acumulada[j]:
            resultado = consultas[j]
            break
    simulaciones.append(resultado)

# Generar tabla con PrettyTable
tabla = PrettyTable()
tabla.field_names = ["N", "Aleatorio",  "Resultado"]
for i in range(N):
    tabla.add_row([i + 1, round(aleatorios[i], 4), simulaciones[i]])
print(tabla)

# Generar gráfica de pastel
plt.pie(frec_acumulada, labels=consultas, autopct='%1.1f%%')
plt.title('Consultas generadas en la simulación')
plt.show()
