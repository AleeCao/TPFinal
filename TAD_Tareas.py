import pprint
from datetime import datetime, date 
pp = pprint.PrettyPrinter(depth=4)

def registrarSalida(placa, camiones, salida, tiempo_estimado):
    horasalida = str(date.today()) + ' ' + salida
    tiempoEstimado = str(date.today()) + ' ' + tiempo_estimado
    for camion in camiones:
        if placa == camion["placa"]:
            camion["hora_salida"] = datetime.strptime(horasalida,'%Y-%m-%d %H:%M')
            camion["tiempo_estimado"] = datetime.strptime(tiempoEstimado,'%Y-%m-%d %H:%M')
    return "El camión no existe"

def eliminarCamion(placa, camiones):
    for camion in camiones:
        if placa == camion["placa"]:
            camiones.remove(camion)
            return "Camión eliminado"
    return "El camión no existe"

def registrarLlegada(placa, camiones, llegada):
    horallegada = str(date.today()) + ' ' + llegada
    for camion in camiones:
        if placa == camion["placa"]:
            camion["hora_llegada"] = datetime.strptime(horallegada, '%Y-%m-%d %H:%M')
            camion['tiempo_real'] = camion['hora_llegada'] - (camion['hora_salida'])
    return "El camión no existe"

def listarCamiones(camiones):
    activos = []
    for camion in camiones:
        if camion['hora_salida'] != '':
            activos.append(camion)
    return activos

def listarMayAct(camiones):
    activos = []
    horario1 = datetime.strptime(str(date.today()) + ' 08:00', '%Y-%m-%d %H:%M')
    horario2 = datetime.strptime(str(date.today()) + ' 12:00', '%Y-%m-%d %H:%M')
    horario3 = datetime.strptime(str(date.today()) + ' 14:00', '%Y-%m-%d %H:%M')
    horario4 = datetime.strptime(str(date.today()) + ' 18:00', '%Y-%m-%d %H:%M')
    for camion in camiones:
        if (camion['hora_salida'] >= horario1 and camion['hora_salida'] <= horario2) or (camion['hora_salida'] >= horario3 and camion['hora_salida'] <= horario4):
            activos.append(camion)
    return activos

def modificarCamion(placa, camiones, atributo, valor):
    for camion in camiones:
        if placa == camion["placa"]:
            camion[atributo] = valor
            return "Camión modificado"
        
def eliminarCamionXRango(camiones, limite):
    hora1 = str(date.today()) + ' ' + limite
    horario1 = datetime.strptime(hora1, '%Y-%m-%d %H:%M')
    for camion in camiones:
        if camion['hora_llegada'] >= horario1:
            camiones.remove(camion)