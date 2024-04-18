#cd /Users/bryanttrujillo/PYTHON\ PRACTICAS/
import random
from tabulate import tabulate as tbl
def HoraProyectada(hora, minutos, duracionAccion):
    minutos += duracionAccion
    while minutos >= 60:
        if(minutos >= 60):
             minutos -= 60
             hora += 1

    if hora > 12:
        hora = 1

    if minutos < 10:
        return str(hora) + ":0" + str(minutos)
    return str(hora) + ":" + str(minutos)


def CamionesIniciales(randomGenerado):
    if randomGenerado < 0.5:
        return 0
    if 0.5 <= randomGenerado < 0.75:
        return 1
    if 0.75 <= randomGenerado < 0.9:
        return 2
    return 3


def TiempoEntreLlegadas(randomGenerado):
    if randomGenerado < 0.02:
        return 20
    if 0.02 <= randomGenerado < 0.1:
        return 25
    if 0.1 <= randomGenerado < 0.22:
        return 30
    if 0.22 <= randomGenerado < 0.47:
        return 35
    if 0.47 <= randomGenerado < 0.67:
        return 40
    if 0.67 <= randomGenerado < 0.82:
        return 45
    if 0.82 <= randomGenerado < 0.92:
        return 50
    if 0.92 <= randomGenerado < 0.97:
        return 55
    return 60

def TiempoServicio(teamSize, randomGenerado):
    tiempoServ = 0
    if teamSize == 3:
        if randomGenerado < 0.05:
            tiempoServ = 20
        elif 0.05 <= randomGenerado < 0.15:
            tiempoServ = 25
        elif 0.15 <= randomGenerado < 0.35:
            tiempoServ = 30
        elif 0.35 <= randomGenerado < 0.60:
            tiempoServ = 35
        elif 0.60 <= randomGenerado < 0.72:
            tiempoServ = 40
        elif 0.72 <= randomGenerado < 0.82:
            tiempoServ = 45
        elif 0.82 <= randomGenerado < 0.90:
            tiempoServ = 50
        elif 0.90 <= randomGenerado < 0.96:
            tiempoServ = 55
        elif 0.96 <= randomGenerado <= 1:
            tiempoServ = 60
    elif teamSize == 4:
        if randomGenerado < 0.05:
            tiempoServ = 15
        elif 0.05 <= randomGenerado < 0.20:
            tiempoServ = 20
        elif 0.20 <= randomGenerado < 0.40:
            tiempoServ = 25
        elif 0.40 <= randomGenerado < 0.60:
            tiempoServ = 30
        elif 0.60 <= randomGenerado < 0.75:
            tiempoServ = 35
        elif 0.75 <= randomGenerado < 0.87:
            tiempoServ = 40
        elif 0.87 <= randomGenerado < 0.95:
            tiempoServ = 45
        elif 0.95 <= randomGenerado <= 1:
            tiempoServ = 50
    elif teamSize == 5:
        if randomGenerado < 0.1:
            tiempoServ = 10
        elif 0.1 <= randomGenerado < 0.28:
            tiempoServ = 15
        elif 0.28 <= randomGenerado < 0.50:
            tiempoServ = 20
        elif 0.50 <= randomGenerado < 0.68:
            tiempoServ = 25
        elif 0.68 <= randomGenerado < 0.78:
            tiempoServ = 30
        elif 0.78 <= randomGenerado < 0.86:
            tiempoServ = 35
        elif 0.86 <= randomGenerado < 0.92:
            tiempoServ = 40
        elif 0.92 <= randomGenerado < 0.97:
            tiempoServ = 45
        elif 0.97 <= randomGenerado <= 1:
            tiempoServ = 50
    elif teamSize == 6:
        if randomGenerado < 0.12:
            tiempoServ = 5
        elif 0.12 <= randomGenerado < 0.27:
            tiempoServ = 10
        elif 0.27 <= randomGenerado < 0.53:
            tiempoServ = 15
        elif 0.53 <= randomGenerado < 0.68:
            tiempoServ = 20
        elif 0.68 <= randomGenerado < 0.80:
            tiempoServ = 25
        elif 0.80 <= randomGenerado < 0.88:
            tiempoServ = 30
        elif 0.88 <= randomGenerado < 0.94:
            tiempoServ = 35
        elif 0.94 <= randomGenerado < 0.98:
            tiempoServ = 40
        elif 0.98 <= randomGenerado <= 1:
            tiempoServ = 45
            
    return tiempoServ



r = random.Random()
NUMTURNOS = 60
equipos = [[],[],[],[]]

costesAcumulado = [[3, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0]]
# Se realizará la simulación por turnos, turno 1: equ ipo 3, 4, 5, 6....
for turnoActual in range(1, NUMTURNOS + 1):
    punteroMatriz = 0
    # Hace la simulación de un turno para cada equipo
    print()
    print("TURNO ACTUAL:", turnoActual)
    for equipoActual in range(3, 7):
        if punteroMatriz > 3:
            punteroMatriz = 0

        print()
        print("Tamaño del equipo:", equipoActual)
        #print("Num. Aleatorio | T/Llegadas | Tiempo de Llegada | Inic. Serv. | Num. Aleatorio | T. del Serv | Term. del Serv. | Ocio personal | T. esp camión | cola")
        print()
        horasTrabajadas = 0
        minutosTrabajados = 0
        tiempoExtra = 0
        ocioPersonal = 0
        esperaCamion = 0
        esperaCamionAcumulada = 0
        horaReloj = 11
        minutosReloj = 0
        lonche = False
        ajusteLonche = False
        randomColaInicial = r.random()
        longitudCola = CamionesIniciales(randomColaInicial)
        randomTiempoServicio = r.random()
        tiempoLlegada = 0
        tiempoServicio = 0

        horaInicioServicio = ""
        tiempoServicio = TiempoServicio(equipoActual, randomTiempoServicio)
        horaFinServicio = HoraProyectada(horaReloj, minutosReloj, tiempoServicio)

        equipos = [[],[],[],[]]
        #print(f"   |    | 11:00 \t | 11:00  | {randomTiempoServicio} | {tiempoServicio}\t | {horaFinServicio}\t| {ocioPersonal}\t | {esperaCamion}\t| {longitudCola}")
        equipos[equipoActual-3].append([0.0, 0.0, "11:00", "11:00", randomTiempoServicio, tiempoServicio, horaFinServicio, ocioPersonal, esperaCamion, longitudCola])
        print()
        # Jornada normal de 11 a 7:30
        while minutosTrabajados < 480 or (horaReloj >= 7 and horaReloj <= 9) or longitudCola > 0:
            if ((horaReloj >= 7 and horaReloj <= 9 and minutosReloj + tiempoServicio >= 30) or minutosTrabajados / 60 >= 8):
                break
            else:
                # Obtiene el tiempo entre llegadas
                randomTiempoLlegada = r.random()
                tiempoLlegada = TiempoEntreLlegadas(randomTiempoLlegada)
                horaLlegada = HoraProyectada(horaReloj, minutosReloj, tiempoLlegada)
                #print(minutosTrabajados)
                minutosTrabajados += (tiempoLlegada)
                
                if (minutosTrabajados >= 480 or (horaReloj >= 7 and minutosReloj >= 30 and lonche)):
                    print(tbl(equipos[equipoActual-3], headers=["Num. Aleatorio ","T/Llegadas "," Tiempo de Llegada "," Inic. Serv. ","Num. Aleatorio "," T. del Serv "," Term. del Serv. "," Ocio personal ","T. esp camión ","cola"]))
                    print(f"Terminando simulación. Siguiente cargamento llegará a las {horaLlegada}")
                    break

                if minutosReloj >= 60:
                    horaReloj += 1
                    if horaReloj > 12:
                        horaReloj = 1
                    minutosReloj -= 60
                # Saca el tiempo de inicio del servicio:
                if (horaReloj >= 3 and horaReloj <= 5 and not lonche):
                    lonche = True
                    minutosReloj += 30
                    esperaCamion = 30
                    esperaCamionAcumulada += esperaCamion

                    if minutosReloj >= 60:
                        horaReloj += 1
                        if horaReloj > 12:
                            horaReloj = 1
                        minutosReloj -= 60

                if tiempoServicio > tiempoLlegada:
                    ocioPersonal = 0
                    longitudCola += 1
                    esperaCamion = tiempoServicio - tiempoLlegada
                    esperaCamionAcumulada += esperaCamion
                    horaInicioServicio = HoraProyectada(horaReloj, minutosReloj, tiempoServicio + esperaCamion)
                
                elif tiempoLlegada > tiempoServicio:
                    if longitudCola > 0:
                        longitudCola -= 1
                    if longitudCola == 0:
                        esperaCamion = 0
                    else:
                        esperaCamion += tiempoServicio
                    if esperaCamion == 0:
                        ocioPersonal = tiempoLlegada - tiempoServicio
                    else:
                        esperaCamionAcumulada += esperaCamion
                    horaInicioServicio = HoraProyectada(horaReloj, minutosReloj, tiempoLlegada)

                else:
                    if longitudCola > 0:
                        horaInicioServicio = HoraProyectada(horaReloj, minutosReloj, tiempoLlegada)
                    ocioPersonal = 0
                    esperaCamion = 0

                minutosReloj += tiempoLlegada
                horaFinServicio = HoraProyectada(horaReloj, minutosReloj, tiempoServicio)

                equipos[equipoActual-3].append([randomTiempoLlegada, tiempoLlegada, horaLlegada, horaInicioServicio, randomTiempoServicio, tiempoServicio, horaFinServicio, ocioPersonal, esperaCamion, longitudCola])

                if lonche and not ajusteLonche:
                    ajusteLonche = True
                else:
                    randomTiempoServicio = r.random()
                    tiempoServicio = TiempoServicio(equipoActual, randomTiempoServicio)

        horasTrabajadas = round(minutosTrabajados / 60)
                
        if minutosTrabajados > 480:
            tiempoExtra = minutosTrabajados - 480
            horasTrabajadas = 8
        else:
            tiempoExtra = 0

        salarioNormal = 25 * 8 * equipoActual
        salarioExtra = equipoActual * tiempoExtra / 60 * 37.5
        costoEspera = 8 * 100 + (100 * esperaCamionAcumulada / 60)
        costoOperativo = 8 * 500 + (500 * tiempoExtra / 60)
        costosTotales = salarioNormal + salarioExtra + costoEspera + costoOperativo

        costesAcumulado[equipoActual - 3][1] += salarioNormal
        costesAcumulado[equipoActual - 3][2] += salarioExtra
        costesAcumulado[equipoActual - 3][3] += costoEspera
        costesAcumulado[equipoActual - 3][4] += costoOperativo
        costesAcumulado[equipoActual - 3][5] += costosTotales    
                         
                          
print()
print("\t COSTES PROMEDIO \n") 

costoMenor = 999999999.999
mejorEquipo = 0

for i in range(4):
    for j in range (1, 6):
        costesAcumulado[i][j] /= 60
        costoMenor = min(costoMenor, costesAcumulado[i][5])
        if(costoMenor == costesAcumulado[i][5]):
            mejorEquipo = i+3

print(tbl(costesAcumulado, headers=["Equipo", "Sal. Normal", "Sal. Extra","Ocio Camión","Op. de Almacen","Costos Totales"]))
print(f"\nEl equipo mas barato es el {mejorEquipo} con un costo de ${costoMenor:,.2f}")
                
