import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Preguntar el número de simulaciones
n = int(input("Cuántas veces deseas realizar la simulación: "))

# Inicializar variables
tabla = PrettyTable()
tabla.field_names = ["N", "# de cuadras recorridas", "Aleatorio", "Localización (x,y)", "Éxito"]
contador_exito = 0

for i in range(1, n + 1):
    x = 0
    y = 0
    c = 0
    cuadra_actual = 1
    camino_x = [0]
    camino_y = [0]

    while c < 10:
        c += 1
        R = round(random.uniform(0, 1), 4)  # Redondear el número aleatorio a 4 decimales
        if 0 <= R < 0.25:
            y += 1
        elif 0.25 <= R < 0.5:
            y -= 1
        elif 0.5 <= R < 0.75:
            x += 1
        elif 0.75 <= R <= 1:
            x -= 1

        # 8. Si el valor absoluto de la suma resulta mayor o igual a 2, entonces se toma como éxito. En caso contrario se toma como fracaso.
        suma = x + y
        exito = "Sí" if abs(suma) >= 2 else "No"
        tabla.add_row([i, cuadra_actual, R, f"({x},{y})", exito])
        cuadra_actual += 1
        camino_x.append(x)
        camino_y.append(y)

    # Verificar si el borracho está a 2 cuadras o más de distancia del inicio
    if abs(x) >= 2 or abs(y) >= 2:
        contador_exito += 1

# Imprimir la tabla
print(tabla)


# Calcular la probabilidad de que el borracho esté a 2 cuadras o más de distancia del inicio
probabilidad_exito = contador_exito / n
print(f"La probabilidad de que el borracho quede a 2 cuadras o más del inicio es: {probabilidad_exito}")


import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Inicializar las listas para almacenar las coordenadas
x_coords = [0]
y_coords = [0]

# Configurar la figura y los ejes
fig, ax = plt.subplots()
line, = ax.plot(x_coords, y_coords, marker="o")

# Configurar los límites del gráfico
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Función para animar el gráfico
def animate(i):
    global x_coords, y_coords

    # Generar un movimiento aleatorio
    direction = random.choice(['N', 'S', 'E', 'O'])
    if direction == 'N':
        y_coords.append(y_coords[-1] + 1)
        x_coords.append(x_coords[-1])
    elif direction == 'S':
        y_coords.append(y_coords[-1] - 1)
        x_coords.append(x_coords[-1])
    elif direction == 'E':
        x_coords.append(x_coords[-1] + 1)
        y_coords.append(y_coords[-1])
    elif direction == 'O':
        x_coords.append(x_coords[-1] - 1)
        y_coords.append(y_coords[-1])

    # Actualizar el gráfico con las nuevas coordenadas
    line.set_data(x_coords, y_coords)

    # Detener la animación después de 10 cuadras
    if len(x_coords) > 10:
        ani.event_source.stop()

    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=200, interval=500, blit=True)

# Mostrar la animación
plt.show()





