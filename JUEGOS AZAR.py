import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

def lanzar_moneda(num_lanzamientos):
    tabla = PrettyTable()
    tabla.field_names = ["No", "# Aleatorio", "Evento"]
    resultados = []
    for i in range(1, num_lanzamientos + 1):
        aleatorio = random.uniform(0, 1)
        evento = "Aguila" if aleatorio <= 0.5 else "Sello"
        tabla.add_row([i, f"{aleatorio:.4f}", evento])
        resultados.append(evento)  
    return tabla, resultados

def lanzar_dado(num_lanzamientos):
    tabla = PrettyTable()
    tabla.field_names = ["No", "# Aleatorio", "Evento"]
    resultados = []
    for i in range(1, num_lanzamientos + 1):
        aleatorio = random.uniform(0, 1)
        if aleatorio <= 1/6:
            evento = 1
        elif aleatorio <= 2/6:
            evento = 2
        elif aleatorio <= 3/6:
            evento = 3
        elif aleatorio <= 4/6:
            evento = 4
        elif aleatorio <= 5/6:
            evento = 5
        else:
            evento = 6
        tabla.add_row([i, f"{aleatorio:.4f}", evento])
        resultados.append(evento)  
    return tabla, resultados

def lanzar_ruleta(num_lados, num_lanzamientos):
    tabla = PrettyTable()
    tabla.field_names = ["No", "# Aleatorio", "Evento"]
    resultados = []
    for i in range(1, num_lanzamientos + 1):
        aleatorio = random.uniform(0, 1)
        evento = int(aleatorio * num_lados) + 1
        tabla.add_row([i, f"{aleatorio:.4f}", evento])
        resultados.append(evento)  
    return tabla, resultados

while True:
    print("E.U.P. DE JUEGOS DE AZAR:")
    print("1. Moneda")
    print("2. Dado")
    print("3. Ruleta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        num_lanzamientos = int(input("¿Cuántas veces deseas lanzar la moneda? "))
        tabla, resultados = lanzar_moneda(num_lanzamientos)
        print(tabla)

    elif opcion == '2':
        num_lanzamientos = int(input("¿Cuántas veces deseas lanzar el dado? "))
        tabla, resultados = lanzar_dado(num_lanzamientos)
        print(tabla)

    elif opcion == '3':
        num_lados = int(input("¿De cuántos lados es la ruleta? "))
        num_lanzamientos = int(input("¿Cuántas veces deseas girar la ruleta? "))
        tabla, resultados = lanzar_ruleta(num_lados, num_lanzamientos)
        print(tabla)

    elif opcion == '4':
        print("Saliste del programa")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    # Crear una gráfica  con los eventos
    if resultados:
        eventos = list(set(resultados))  # Obtener eventos únicos
        counts = [resultados.count(evento) for evento in eventos]
        plt.pie(counts, labels=[str(evento) for evento in eventos], autopct='%1.1f%%')
        plt.title("Gráfica")
        plt.show()
