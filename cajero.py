import random
from math import log
from prettytable import PrettyTable

n = int(input("Ingrese la cantidad de simulaciones: "))
i = 1

def Tiemplleg(ale):
    fun = (-log(1 - ale) / 30) * 60
    return round(fun, 5)

while i <= n:
    momllant = 0
    tt = 0
    tiet = 0
    k = 1

    table = PrettyTable()
    table.field_names = ['Usuario', '#Alea1', 'Tiempo entre llegada', 'Momento de llegada', 'Tiempo inicia servicio',
                         'Tiempo espera / atencion', '#Ale2', 'Operacion', 'Tiempo de Operacion', 'Tiempo Termina el Servicio']

    while k <= 100:
        ale1 = round(random.random(), 5)
        tiel = Tiemplleg(ale1)
        momll = round(tiel + momllant, 5)
        ale2 = round(random.random(), 5)

        if ale2 <= 0.25:
            op = "Consulta de Saldo"
            top = 80
            topm = 1.33
        elif ale2 <= 0.5:
            op = "Otros"
            top = 50
            topm = 0.83
        elif ale2 <= 0.85:
            op = "Retiros"
            top = 120
            topm = 2
        else:
            op = "Transferencia"
            top = 60
            topm = 1

        if momll >= tt:
            ti = momll
        else:
            ti = tt

        ti = round(ti, 5)
        tie = round(ti - momll, 5)
        tt = round(ti + topm, 5)
        tiet += tie

        table.add_row([k, ale1, tiel, momll, ti, tie, ale2, op, top, tt])

        momllant = momll
        k += 1

    tiet = round(tiet, 5)

    print("Simulacion #", i)
    print(table)
    print("\nTiempo de espera: ", tiet, "\n")
    i += 1
