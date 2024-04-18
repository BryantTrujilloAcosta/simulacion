import random
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
chi5 = [3.8415, 5.9915, 7.8147, 9.4877, 11.0705, 12.5916, 14.0671, 15.5073, 16.919, 18.307, 19.6752, 21.0261,
        22.362, 23.6848, 24.9958, 26.2962, 27.5871, 28.8693, 30.1435, 31.4104, 32.6706, 33.9245, 35.1725, 36.415,
        37.6525, 38.8851, 40.1133, 41.3372, 42.5569, 43.773, 44.9853, 46.1942, 47.3999, 48.6024, 49.8018, 50.9985,
        52.1923, 53.3835, 54.5722, 55.7585]
chi10 = [2.7055, 4.6052, 6.2514, 7.7794, 9.2363, 10.6446, 12.017, 13.3616, 14.6837, 15.9872, 17.275, 18.5493,
			19.8119, 21.0641, 22.3071, 23.5418, 24.769, 25.9894, 27.2036, 28.412, 29.6151, 30.8133, 32.0069, 33.1962,
			34.3816, 35.5632, 36.7412, 37.9159, 39.0875, 40.256, 41.4217, 42.5847, 43.7452, 44.9032, 46.0588, 47.2122,
			48.3634, 49.5126, 50.6598, 51.805,]
kolmogorov5 = [0.97500, 0.84189, 0.70760, 0.62394, 0.56328, 0.51926, 0.48342, 0.45427,
			0.43001, 0.40925, 0.39122, 0.37543, 0.36143, 0.34890, 0.33750, 0.32733, 0.31796, 0.30936, 0.30143, 0.29408,
			0.28724, 0.28087, 0.27491, 0.26931, 0.26404, 0.25908, 0.25438, 0.24993, 0.24571, 0.24170, 0.23788, 0.23424,
			0.23076, 0.22743, 0.22425, 0.22119, 0.21826, 0.21544, 0.21273, 0.21012, 0.20760, 0.20517, 0.20283, 0.20056,
			0.19837, 0.19625, 0.19420, 0.19221, 0.19028, 0.18841]
kolmogorov10 = [0.95000, 0.77639, 0.63604, 0.56522, 0.50945, 0.46799, 0.43607, 0.40962,
			0.38746, 0.36866, 0.35242, 0.33815, 0.32549, 0.31417, 0.30397, 0.29472, 0.28627, 0.27851, 0.27136, 0.26473,
			0.25858, 0.25283, 0.24746, 0.24242, 0.23768, 0.23320, 0.22898, 0.22497, 0.22117, 0.21756, 0.21412, 0.21085,
			0.20771, 0.21472, 0.20185, 0.19910, 0.19646, 0.19392, 0.19148, 0.18913, 0.18687, 0.18468, 0.18257, 0.18051,
			0.17856, 0.17665, 0.17481, 0.17301, 0.17128, 0.16959]
def numeros_aleatorios(cantidad):
    numeros = [round(random.uniform(0,1),5) for _ in range(cantidad)]
    return numeros

def chicuadrada(lista,porcentaje):
    n = len(lista)
    k = round(math.sqrt(n))  # Calcular la raíz cuadrada de n y redondear al entero más cercano
    i = [f"{round((j + 1) / k, 1)}" for j in range(k)]
    o = [0] * k # Inicializar la lista de frecuencias observadas con ceros
    e = [round(n/k, 5) for _ in range(k)] # Crear la lista con n/k en cada posición
    for num in lista:
        for j in range(k):
            if j / k <= num < (j + 1) / k:
                o[j] += 1
                break
    oe = [round(obs - e_i, 5) for obs, e_i in zip(o, e)]
    oe2 = [round(obs ** 2 / e_i, 5) for obs, e_i in zip(oe, e)]
    # Calcular totales
    total_o = sum(o)
    total_e = round(sum(e))
    total_oe = round(sum(oe), 5)
    total_oe2 = round(sum(oe2), 5)
    

    # Agregar totales a las listas
    i.append("Total")
    o.append(total_o)
    e.append(total_e)  # Todos los elementos de la lista son iguales
    oe.append("∑=")
    oe2.append(total_oe2)

    # Crear la tabla
    tabla = PrettyTable()
    tabla.field_names = ["i", "o", "e", "o - e", "(o - e)^2 / e"]
    for fila in zip(i, o, e, oe, oe2):
        tabla.add_row(fila)
    print(tabla)
    if porcentaje == 5:
       chi = k - 2
       chiporcen = chi5[int(chi)]
       if total_oe2 <= chiporcen:
        print(f"{total_oe2} < {chiporcen}:Los números Están uniformemente distribuidos")
       else:
        print(f"{total_oe2} > {chiporcen}:Los números NO están uniformemente distribuidos")
    elif porcentaje ==10:
       chi = k - 2
       chiporcen = chi10[int(chi)]
       if total_oe2 <= chiporcen:
        print(f"{total_oe2} < {chiporcen}:Los números Están uniformemente distribuidos")
       else:
        print(f"{total_oe2} > {chiporcen}:Los números NO están uniformemente distribuidos")
    plt.bar(i[:-1], o[:-1], width=0.4, align='center', alpha=0.7, label='Observado')
    plt.hlines(e[:-1], xmin=i[:-1], xmax=i[1:], colors='r', label='Esperado', linewidth=2)
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title('CHI - CUADRADA')
    plt.legend()
    plt.show()
def Kolmogorov(lista,porcentaje):
    lista_ordenada = np.sort(lista)
    n = len(lista_ordenada)
    
    # Calcular i/n y Di
    i_n_values = np.round(np.arange(1, n + 1) / n, 5)
    D_values = np.round(np.abs(lista_ordenada - i_n_values), 5)

    # Crear la tabla
    tabla = PrettyTable()
    tabla.field_names = ["i", "u_i", "i/n", "D_i"]

    for i in range(n):
        tabla.add_row([i + 1, round(lista_ordenada[i], 5), i_n_values[i], D_values[i]])
    print(tabla)
    max_D = max(D_values)
    if porcentaje == 5:
       if n > 50:
           di2 = 1.36 / np.sqrt(n)
           if max_D <= di2:
               print(f"{max_D} < {di2}: Los números están uniformemente distribuidos")
           else:
               print(f"{max_D} > {di2}: Los números no están uniformemente distribuidos")
       else:
          kol = kolmogorov5[int(n-1)]
          if max_D <= kol:
              print(f"{max_D} < {kol}: Los números están uniformemente distribuidos")
          else:
              print(f"{max_D} > {kol}: Los números no están uniformemente distribuidos")
              
    elif porcentaje == 10:
       if n > 50:
           di2 = 1.36 / np.sqrt(n)
           if max_D <= di2:
               print(f"{max_D} < {di2}: Los números están uniformemente distribuidos")
           else:
               print(f"{max_D} > {di2}: Los números no están uniformemente distribuidos")
       else:
          kol = kolmogorov10[int(n-1)]
          if max_D <= kol:
              print(f"{max_D} < {kol}: Los números están uniformemente distribuidos")
          else:
              print(f"{max_D} > {kol}: Los números no están uniformemente distribuidos")

    # Graficar ui y i/n
    plt.plot(range(1, n + 1), lista_ordenada, label='u_i')
    plt.plot(range(1, n + 1), i_n_values, label='i/n')
    # Dibujar líneas verticales desde u_i hasta i/n

    # Resaltar el valor máximo de D en una línea vertical
    max_D_index = np.argmax(D_values)
    plt.axvline(x=max_D_index + 1, color='red', linestyle='-', label='Máx D')
    plt.title("KOLMOGOROV")
    plt.xlabel('numeros')
    plt.ylabel('ui | i/N')
    plt.legend()
    plt.show()

def Metodo_series(lista, n, percent):
    N = len(lista)

    # Paso 2: Dividir un cuadro de lado 1 en n^2 celdas.
    cuadro_lado = 1
    celdas_lado = n

    # Paso 3: Formar pares ordenados (Ui, Ui+1) hasta N pares.
    U_i = lista[:-1]
    U_i1 = lista[1:]

    # Paso 4: Calcular Oij (cantidad de números por celda observados).
    O_ij, x_edges, y_edges = np.histogram2d(U_i, U_i1, bins=[celdas_lado, celdas_lado])

    # Paso 5: Calcular Eij (cantidad de números por celda esperados).
    E_ij = N / (celdas_lado ** 2)

    # Paso 6: Calcular Xo^2
    Xo_squared = np.sum((O_ij - E_ij) ** 2 / E_ij)

    # Paso 7: Verificar la condición Xo^2 <= X_(n^2-1, %)^2
    chi_critical = chi5[celdas_lado ** 2 - 1] if percent == 5 else chi10[celdas_lado ** 2 - 1]


    # Paso 10: Imprimir la tabla con PrettyTable para U1 y U2
    tabla_U = PrettyTable()
    tabla_U.field_names = ["#", "U1", "U2"]

    for i, (u1, u2) in enumerate(zip(U_i, U_i1), start=2):
        tabla_U.add_row([i, u1, u2])

    print("Tabla de U1 y U2:")
    print(tabla_U)
    tabla_obs = PrettyTable()
    tabla_obs.field_names = [f"Intervalo {i} - {i+1}" for i in range(celdas_lado)]

     # Calcular (O_ij - E_ij)^2 / E_ij para la tabla
    tabla_o = PrettyTable()
    tabla_o.field_names = [f"Intervalo {i} - {i+1}" for i in range(celdas_lado)]
    O_minus_E_squared_over_E = (O_ij - E_ij) ** 2 / E_ij
    for i, row in enumerate(O_minus_E_squared_over_E):
        tabla_o.add_row(row)
    print("Tabla de Frecuencias Observadas:")
    print(tabla_o)
    # Paso 8: Imprimir resultados
    print(f"\nXo^2: {Xo_squared}")
    print(f"X_(n^2-1, {percent}%): {chi_critical}")
    print(f"Los números son {'independientes' if Xo_squared <= chi_critical else 'no independientes'}\n")
    # Paso 11: Crear gráfico
    l = 1  # Tamaño del cuadro
    fig, ax = plt.subplots()
    for i in range(celdas_lado + 1):
        ax.axhline(i * l / celdas_lado, color='black')
        ax.axvline(i * l / celdas_lado, color='black')

    ax.plot(U_i, U_i1, 'ro', markersize=5)

    plt.title('Gráfica Series')
    plt.show()



while True:
    try:
        n = int(input("¿Cuántos números quieres generar? "))
        
        if 34 <= n <= 100:
            resultado = numeros_aleatorios(n)
            print("Números aleatorios generados:")
            for i, numero in enumerate(resultado, start=1):
                print(f"[{i}]: {numero}")
            break  # Salir del bucle si la entrada es válida
        else:
            print("Por favor, ingresa un número entre 34 y 100.")

    except ValueError:
        print("Por favor, ingresa un número entero válido.")
def Metodo_huecos(lista, a, b, percent):
    num = np.array(lista)
    t = b - a
    huecos = []

    # Paso 1: Crear la lista e
    e = np.where((num >= a) & (num <= b), 1, 0)

    # Paso 2: Imprimir tabla e
    print("i\tUi\t\te")
    for i in range(len(num)):
        print(f"{i + 1}\t{num[i]}\t\t{e[i]}")

    numhuecos = 0
    na = 2

    # Paso 3: Calcular la lista de huecos
    for i in range(len(num)):
        if e[i] != na and na != 2:
            huecos.append(numhuecos)
            numhuecos = 0
        if e[i] == 1:
            numhuecos = 0
            na = e[i]
        else:
            numhuecos += 1
            na = e[i]
    huecos.append(numhuecos)


    # Paso 5: Calcular nhuecos
    nhuecos = next(i for i in range(1, len(num)) if i not in huecos)

    # Paso 6: Calcular lista o
    o = np.zeros(nhuecos, dtype=int)
    for i in range(nhuecos):
        for j in range(len(huecos)):
            if huecos[j] == i:
                o[i] += 1

    # Paso 7: Calcular sumaoi
    sumaoi = np.sum(o)

    # Paso 8: Calcular la tabla y res
    res = 0
    tabla = PrettyTable()
    tabla.field_names = ["i", "pi", "oi", "ei", "(oi - ei)", "(oi - ei)^2 / ei"]

    for i in range(nhuecos):
        pi = (1 - t) ** i * t
        ei = len(huecos) * pi
        tabla.add_row([i, f"{pi:.4f}", o[i], f"{ei:.4f}", f"{o[i] - ei:.4f}", f"{(o[i] - ei)**2 / ei:.4f}"])
        res += (o[i] - ei) ** 2 / ei

    # Última fila de la tabla
    pi = (1 - t) ** nhuecos
    ei = len(huecos) * pi
    tabla.add_row([f"n>={nhuecos}", f"{pi:.4f}", len(huecos) - sumaoi, f"{ei:.4f}",
                   f"{(len(huecos) - sumaoi) - ei:.4f}", f"{((len(huecos) - sumaoi) - ei)**2 / ei:.4f}"])
    res += ((len(huecos) - sumaoi) - ei) ** 2 / ei

    # Paso 9: Imprimir la tabla y resultados
    print(tabla)
    print(f"\nXo^2: {res}")
    x = chi5[nhuecos - 1] if percent == 5 else chi10[nhuecos - 1]
    print(f"x^2 ({nhuecos},{percent}): {x}")
    print(f"Los números son {'no ' if res > x else ''}son independientes\n")

def Metodo_poker(lista, percent):
    nnums = [format(int(x * 100000), '05') for x in lista]
    totales = [0, 0, 0, 0, 0, 0, 0]

    # Recorrer la lista de números y calcular repeticiones
    for i, num in enumerate(lista):
        repeticiones = np.zeros(10, dtype=int)
        for j in range(5):
            repeticiones[int(nnums[i][j])] += 1

        pares = np.count_nonzero(repeticiones == 2)
        tercias = np.count_nonzero(repeticiones == 3)
        pok = np.count_nonzero(repeticiones == 4)
        quintilla = np.count_nonzero(repeticiones == 5)

        # Agregar fila a la tabla de eventos
        
        # Imprimir información del evento actual
        print(f"{i + 1}\t{num}\t\t", end="")
        if pares == 1 and tercias == 0:
            print("1 Par")
            totales[1] += 1
        elif pares == 2:
            print("2 Pares")
            totales[3] += 1
        elif pares == 0 and tercias == 1:
            print("Tercia")
            totales[2] += 1
        elif pares == 1 and tercias == 1:
            print("Full")
            totales[4] += 1
        elif pok == 1:
            print("Poker")
            totales[5] += 1
        elif quintilla == 1:
            print("Quintilla")
            totales[6] += 1
        else:
            print("Pachuca")
            totales[0] += 1

    # Crear tabla de resultados
    tabla_resultados = PrettyTable()
    tabla_resultados.field_names = ["Evento", "FO", "PE", "FE", "(FO-FE)", "(FO-FE)^2/FE"]

    # Definir nombres y valores esperados para la tabla de resultados
    nombres = ["Pachuca", "1 Par", "Tercia", "2 Pares", "Full", "Poker", "Quintilla"]
    esperados = [0.3024, 0.504, 0.072, 0.108, 0.009, 0.0045, 0.0001]

    # Calcular resultados y agregar filas a la tabla de resultados
    res = 0
    formato = "{:.5f}"
    for i in range(7):
        tabla_resultados.add_row([nombres[i],
                 totales[i],
                                  formato.format(esperados[i]),
                                  formato.format(esperados[i] * len(lista)),
                                  formato.format(totales[i] - (esperados[i] * len(lista))),
                                  formato.format((totales[i] - (esperados[i] * len(lista)))**2 / (esperados[i] * len(lista)))])
        res += (totales[i] - (esperados[i] * len(lista)))**2 / (esperados[i] * len(lista))

    # Imprimir la tabla de resultados
    print(tabla_resultados)

    # Imprimir resultados finales
    print("\nxo^2:", formato.format(res))
    x = chi5[5] if percent == 5 else chi10[5]
    print(f"x^2 (6, {percent}): {formato.format(x)}")
    print("Los numeros " + ("no " if res > x else "") + "son independientes\n")


while True:
    try:
        print("¿Qué prueba deseas aplicar? ")
        print("1.- Chi-cuadrada")
        print("2.- Kolmogorov")
        print("3.- Series")
        print("4.- Distancias o Huecos")
        print("5.- Poker")
        print("6.- Salir")
        n = int(input())

        if n == 6:
            print("Saliendo del programa.")
            break  # Salir del bucle si la opción es 6
        elif n == 1:
            # Realizar la prueba chi-cuadrada
            while True:
                try:
                    porcentaje = int(input("Cuánto porcentaje de fallo 5% o 10%: "))
                    if porcentaje == 5 or porcentaje == 10:
                        chicuadrada(resultado, porcentaje)
                        break
                    else:
                        print("Por favor, elige 5 o 10.")
                except ValueError:
                    print("Por favor, ingresa un número entero válido.")
        elif n == 2:
            # Realizar la prueba chi-cuadrada
            while True:
                try:
                    porcentaje = int(input("Cuánto porcentaje de fallo 5% o 10%: "))
                    if porcentaje == 5 or porcentaje == 10:
                        Kolmogorov(resultado, porcentaje)
                        break
                    else:
                        print("Por favor, elige 5 o 10.")
                except ValueError:
                    print("Por favor, ingresa un número entero válido.")
        elif n == 3:
            while True:
                try:
                    porcentaje = int(input("Cuánto porcentaje de fallo 5% o 10%: "))
                    if porcentaje == 5 or porcentaje == 10:
                        Metodo_series(resultado, 5, porcentaje)
                        break
                    else:
                        print("Por favor, elige 5 o 10.")
                except ValueError:
                    print("Por favor, ingresa un número entero válido.")
        elif n == 4:
            while True:
                try:
                    porcentaje = int(input("Cuánto porcentaje de fallo 5% o 10%: "))
                    alfa = float(input("Valor de alfa: "))
                    beta = float(input("Valor de beta: "))
                    if porcentaje == 5 or porcentaje == 10:
                        Metodo_huecos(resultado, alfa, beta, porcentaje)
                        break
                    else:
                        print("Por favor, elige 5 o 10.")
                except ValueError:
                    print("Por favor, ingresa un número entero válido.")
        elif n == 5:
            while True:
                try:
                    porcentaje = int(input("¿Cuánto porcentaje de fallo 5% o 10%: "))
                    if porcentaje == 5 or porcentaje == 10:
                        Metodo_poker(resultado, porcentaje)
                        break
                    else:
                        print("Por favor, elige 5 o 10.")
                except ValueError:
                    print("Por favor, ingresa un número entero válido.")
        else:
            print("Por favor, ingresa una opción válida (1-6).")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
