import random
from prettytable import PrettyTable

gano1 = 0
gano2 = 0
perder1 = 0
perder2 = 0
color = 0  # rojo - negro - verde

table1 = PrettyTable()
table1.field_names = ["iteracion", "$ Antes de girar", "Apuesta", "#alea",
                      "color", "gano?", "$ Despues de girar", "se llego a USD$1000?", "Exito++"]

table2 = PrettyTable()
table2.field_names = ["iteracion", "$ Antes de girar", "Apuesta", "#alea",
                      "color", "gano?", "$ Despues de girar", "se llego a USD$1000?", "Exito++"]

print("\t RULETA \n")

n = int(input("Introduzca la cantidad de simulaciones "))

for i in range(n):
    flag = False
    contador = 0
    dinero1 = 200
    dinero2 = 200
    apuesta1 = 1
    apuesta2 = 1

    while ((dinero1 < 1000 and dinero2 < 1000) and (dinero1 > 0 and dinero2 > 0)):
        contador += 1
        antesGirar1 = dinero1
        antesGirar2 = dinero2
        exito1S, exito2S = "No", "No"
        apuesta2Inicial = apuesta2
        alegen = round(random.uniform(0, 1), 5)

        # rojos 0 a 10/22
        if 0 <= alegen <= 10/22:
            color, colorS, gano = 0, "Rojo", "Si"
        # negros 10/22 a 20/22
        elif 10/22 < alegen <= 20/22:
            color, colorS, gano = 1, "Negro", "No"

        else:
            color, colorS, gano = 2, "Verde", "Nulo"

        # gano
        if color == 0 and not flag:
            dinero1 += apuesta1
            dinero2 += apuesta2
            apuesta2 = 1
        # perdio
        elif color == 1 and not flag:
            dinero1 -= apuesta1
            dinero2 -= apuesta2
            apuesta2 *= 2

        # verde nulo
        if color == 2:
            flag = True

        # fue nulo el anterior y gano pero no gana nada
        if color == 0 and flag:
            flag = False

        # fue nulo el anterior y perdio
        if color == 1 and flag:
            dinero1 -= apuesta1
            dinero2 -= apuesta2
            apuesta2 *= 2
            flag = False

        if dinero1 >= 1000:
            exito1S = "Si"
            gano1 += 1
            perder2 += 1

        if dinero2 >= 1000:
            exito2S = "Si"
            gano2 += 1
            perder1 += 1

        if dinero1 <= 0:
            gano2 += 1

        if dinero2 <= 0:
            gano1 += 1

        table1.add_row([contador, antesGirar1, apuesta1, alegen,
                        colorS, gano, dinero1, exito1S, "++" if exito1S == "Si" else ""])
        table2.add_row([contador, antesGirar2, apuesta2, alegen,
                        colorS, gano, dinero2, exito2S, "++" if exito2S == "Si" else ""])

print("-------------------------------------Jugador 1-------------------------------------")
print(table1)
print("-------------------------------------Jugador 2-------------------------------------")
print(table2)
print("El jugador 1 gano: ", gano1, " veces")
print("El jugador 1 perdio: ", perder1, " veces")
print("El jugador 2 gano: ", gano2, " veces")
print("El jugador 2 perdio: ", perder2, " veces")

if gano1 > gano2:
    print("La mejor estrategia es la del Jugador 1")
elif gano2 > gano1:
    print("La mejor estrategia es la del Jugador 2")
else:
    print("Ambas estrategias son válidas")
