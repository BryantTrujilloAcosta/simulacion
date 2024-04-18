import math
import random

opc = 0
k = 2
valorA = 2
valorC = 2
valorM = 0
inicio = """\t ---METODO DE LAS CONGRUENCIAS--- \n
Integrantes:
*Cansdales Escobosa Ricardo
*Delgado Olivas Angel David
*Luque Ochoa Jessica Abigail
"""

print(inicio)
# obtener valor de A
while valorA % 2 == 0 or valorA % 3 == 0 or valorA % 5 == 0:
    valorA = int(input("Proporciona el valor de A: "))
    if valorA % 2 == 0 or valorA % 3 == 0 or valorA % 5 == 0:
        print("Introduce un numero valido(que no sea multiplo de 2, 3 o 5)")
# obtener valor de X
while opc != 1 and opc != 2:
    print("\n\tPARA EL VALOR DE X: \t")
    print("1 - Introducir el valor por teclado")
    print("2 - Generar un valor random")
    opc = int(input("Digite la opción deseada:"))
    if opc != 1 and opc != 2:
        print("Introduzca una opcion valida...")
if opc == 1:
    valorX = int(input("Introduce el valor de X:"))
if opc == 2:
    valorX = random.randint(0, 1000)
    print("---valor de X guardado---\n")

# obtener valor de c
while valorC % 2 == 0:
    print("\n\tPARA EL VALOR DE C: \t")
    valorC = int(input(("Digite el valor de c (impar):")))
    if valorC % 2 == 0:
        print("Introduzca un numero impar...")

# metodo que dice si el numero es primo


def esPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


opc = 0
# obtener valor de m
while opc != 1 and opc != 2:
    print("\n\tPARA EL VALOR DE M: \t")
    print("1 - Generar un valor random")
    print("2 - Introducir el valor por teclado")
    opc = int(input("Digite la opción deseada:"))
    if opc != 1 and opc != 2:
        print("Introduzca una opcion valida...")
if opc == 1:
    valorM = random.randint(0, 10000)
if opc == 2:
    while valorM > 10**63 or esPrimo(valorM) is False:
        valorM = int(input("Introduce el valor de M:"))
        if valorM > 10**63 or esPrimo(valorM) is False:
            print("Digite un numero valido...")
n = [0]
axnc = [valorX*valorA + valorC]
residuo = [axnc[-1] % valorM]
valoresX = []
valoresX.append(valorX)
valoresX.append(residuo[-1])

while valorX != valoresX[-1]:
    axnc.append((valoresX[-1] * valorA) + valorC)
    residuo.append(axnc[-1] % valorM)
    valoresX.append(residuo[-1])
    n.append(n[-1] + 1)

print("n\t| x\t| axn + c\t| axn + c / m\t\t| xn+1\t|")
for i in n:
    print("-----------------------------------------------------------------")
    print(n[i], "\t|", valoresX[i], "\t|", axnc[i], "\t\t|",
          axnc[i], "/", valorM, "\t\t|", residuo[i], "\t|")
