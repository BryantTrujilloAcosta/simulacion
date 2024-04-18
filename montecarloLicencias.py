import random
import numpy as np
from prettytable import PrettyTable

n = int(input("Cuantas veces se va a realizar la simulacion? "))
licencias = 0

while licencias not in [100, 150, 200, 250, 300]:
    licencias = int(
        input("Cuantas licencias se va a comprar (100/150/200/250/300)? "))
    if licencias not in [100, 150, 200, 250, 300]:
        print("esa cantidad no es valida")

tabla = PrettyTable()
tabla.field_names = ["N", "#alegen", "Licencias Ven", "Licencias Dev", "Costo", "ing x vta", "ing x dev", "Utilidad"]
arreglo_utilidades = []
for i in range(n):
    alegen = random.uniform(0, 1)
    lv = 0
    while lv > licencias or lv == 0:
        alegen = random.uniform(0, 1)
        if 0 <= alegen < 0.30:
            lv = 100
        elif 0.30 <= alegen < 0.50:
            lv = 150
        elif 0.50 <= alegen < 0.80:
            lv = 200
        elif 0.80 <= alegen < 0.95:
            lv = 250
        elif 0.95 <= alegen <= 1.00:
            lv = 300

    lic_dev = licencias - lv
    costo = licencias * 75
    ing_vta = lv * 100
    ing_dev = lic_dev * 25
    utilidad = ing_vta + ing_dev - costo
    arreglo_utilidades.append(utilidad)
    alegen2 = round(alegen, 4)
    tabla.add_row([i+1, alegen2, lv, lic_dev, costo, ing_vta, ing_dev, utilidad])
print(tabla)
media = np.mean(arreglo_utilidades)
varianza = np.var(arreglo_utilidades)
print(f"\nLa media de utilidades es: {media}")
print(f"La varianza de utilidades es: {varianza}")
