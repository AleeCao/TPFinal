from TAD_Camion import *
from TAD_Tareas import *
from TAD_Cargado import cargarCamiones
import pprint
pp = pprint.PrettyPrinter(depth=4)

camion1 = crearCamion("ABC123", "Bodega 1", "Bodega 2")
camion2 = crearCamion("DEF456", "Bodega 3", "Bodega 4")
camion3 = crearCamion("GHI789", "Bodega 5", "Bodega 6")
camiones = registroCamiones()
camiones.append(camion1)
camiones.append(camion2)
camiones.append(camion3)
cargarCamiones(camiones)

pp.pprint(camiones)

registrarSalida(camion1['placa'], camiones)