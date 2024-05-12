def crearCamion (placa, origen, destino, hora_salida, hora_llegada, tiempo_estimado):
    camion = {
        "placa": placa,
        "origen": origen,
        "destino": destino,
        "hora_salida": hora_salida,
        "hora_llegada": hora_llegada, 
        "tiempo_estimado": tiempo_estimado
    }
    return camion

def cargarCamiones(camiones):
    camion1 = crearCamion("ABC123", "Bodega 1", "Bodega 2", "08:00", "10:00", "02:00")
    camion2 = crearCamion("DEF456", "Bodega 3", "Bodega 4", "08:30", "12:00", "03:30")
    camion3 = crearCamion("GHI789", "Bodega 5", "Bodega 6", "12:00", "16:00", "04:00")
    camion4 = crearCamion("JKL012", "Bodega 7", "Bodega 8", "10:00", "16:15", "06:15")
    camion5 = crearCamion("MNO345", "Bodega 9", "Bodega 10", "09:45", "18:00", "08:15")
    camion6 = crearCamion("PQR678", "Bodega 11", "Bodega 12", "10:33", "20:00", "09:27")
    camion7 = crearCamion("STU901", "Bodega 13", "Bodega 14", "08:24", "13:41", "05:17")
    camion8 = crearCamion("VWX234", "Bodega 15", "Bodega 16", "07:18", "15:36", "08:18")
    camion9 = crearCamion("YZA567", "Bodega 17", "Bodega 18", "11:25", "12:08", "00:43")
    camion10 = crearCamion("BCD890", "Bodega 19", "Bodega 20", "12:26", "14:00", "01:34")
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
    return camiones