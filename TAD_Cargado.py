from datetime import datetime, date 

def crearCamion (placa, origen, destino, hora_salida, hora_llegada, tiempo_estimado, tiempo_real):
    horaSalida = str(date.today()) + ' ' + hora_salida
    horaLlegada = str(date.today()) + ' ' + hora_llegada
    tiempoEstimado = str(date.today()) + ' ' + tiempo_estimado
    tiempoReal = str(date.today()) + ' ' + tiempo_real
    camion = {
        "placa": placa,
        "origen": origen,
        "destino": destino,
        "hora_salida": datetime.strptime(horaSalida,'%Y-%m-%d %H:%M'),
        "hora_llegada": datetime.strptime(horaLlegada, '%Y-%m-%d %H:%M'), 
        "tiempo_estimado": datetime.strptime(tiempoEstimado, '%Y-%m-%d %H:%M'),
        "tiempo_real": datetime.strptime(tiempoReal, '%Y-%m-%d %H:%M')
    }
    return camion

def cargarCamiones(camiones):
    camion1 = crearCamion("ABC548", "Bodega 1", "Bodega 2", "08:00", "10:00", "01:35" ,"02:00")
    camion2 = crearCamion("AAF456", "Bodega 3", "Bodega 4", "08:30", "12:00", "03:50", "03:30")
    camion3 = crearCamion("LSO789", "Bodega 5", "Bodega 6", "12:00", "16:00", "03:45", "04:00")
    camion4 = crearCamion("JKL012", "Bodega 7", "Bodega 8", "10:00", "16:15", "06:20", "06:15")
    camion5 = crearCamion("MNO345", "Bodega 9", "Bodega 10", "09:45", "18:00", "08:53", "08:15")
    camion6 = crearCamion("PQR678", "Bodega 11", "Bodega 12", "10:33", "20:00", "06:35", "09:27")
    camion7 = crearCamion("STU901", "Bodega 13", "Bodega 14", "08:24", "13:41", "04:45", "05:17")
    camion8 = crearCamion("VWX234", "Bodega 15", "Bodega 16", "07:18", "15:36", "08:32", "08:18")
    camion9 = crearCamion("YZA567", "Bodega 17", "Bodega 18", "11:25", "12:08", "01:15", "00:43")
    camion10 = crearCamion("BCD890", "Bodega 19", "Bodega 20", "12:26", "14:00", "01:45", "01:34")
    camiones.append(camion1)
    camiones.append(camion2)
    camiones.append(camion3)
    camiones.append(camion4)
    camiones.append(camion5)
    camiones.append(camion6)
    camiones.append(camion7)
    camiones.append(camion8)
    camiones.append(camion9)
    camiones.append(camion10)

camiones = []
cargarCamiones(camiones)