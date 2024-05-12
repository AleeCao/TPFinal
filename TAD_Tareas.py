from datetime import datetime

def registrarSalida(placa, camiones):
    for camion in camiones:
        if placa == camion["placa"]:
            print(placa)
            camion["hora_salida"] = datetime.now().strftime("%H:%M")
            print(camion['hora_salida'])
    return "El camión no existe"

def registrarLlegada(placa, camiones):
    for camion in camiones:
        if placa == camion["placa"]:
            print(placa)
            camion["hora_llegada"] = datetime.now().strftime("%H:%M")
            print(camion['hora_llegada'])
    return "El camión no existe"