
#Cada camión tiene asignada una placa, un punto de distribución Origen, un punto de distribución Destino, una hora de salida de origen, una hora de llegada a destino, y un tiempo estimado de viaje
def crearCamion (placa, origen, destino):
    camion = {
        "placa": placa,
        "origen": origen,
        "destino": destino,
        "hora_salida": "",
        "hora_llegada": "", 
        "tiempo_estimado": "",
        "tiempo_real": ""
    }
    return camion

def registroCamiones():
    camiones = []
    return camiones

