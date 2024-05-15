from TAD_Camion import *
from TAD_Tareas import *
from TAD_Cargado import cargarCamiones
import pprint
pp = pprint.PrettyPrinter(depth=4)

camiones = registroCamiones()
cargarCamiones(camiones)
salida = False
while not salida:
    print('======Menu======')
    print('a. Registrar partida, modificar información o eliminar camión.')
    print('b. Registrar llegada de camión.')
    print('c. Listar camiones activos.')
    print('d. Informe de movimientos por punto de distribución')
    print('e. Listar camiones activos en horario de mayor actividad.')
    print('f. Eliminar camiones por rango de tiempo.')
    print('g. Cola de camiones que superan tiempo estimado.')
    print('h. Ingresar camión.')
    print('i. Salir.')
    opcion = input('Seleccione una opcion: ')
    if opcion == 'a':
        print('a. Registrar partida\nb. Modificar información\nc. Eliminar camión')
        opcion2 = input('Seleccione una opción: ')
        if opcion2 == 'a':
            placa = input('Ingrese la placa del camión: ')
            salida = input('Ingrese la hora de salida: ')
            registrarSalida(placa, camiones, salida)
        #elif opcion == 'b':
            #placa = input('Ingrese la placa del camión: ')
            #llegada = input('Ingrese la hora de llegada: ')
            #print(registrarLlegada(placa, camiones, llegada))
        elif opcion == 'c':
            placa = input('Ingrese la placa del camión: ')
            eliminarCamion(placa ,camiones)
    elif opcion == 'b':
        placa = input('Ingrese la placa del camión: ')
        llegada = input('Ingrese la hora de llegada: ')
        registrarLlegada(placa, camiones, llegada)
    elif opcion == 'c':
        pp.pprint(listarCamiones(camiones))
    elif opcion == 'd':
        print('Informe de movimientos por punto de distribución')
    elif opcion == 'e':
        pp.pprint(listarMayAct(camiones))
    elif opcion == 'f':
        print('Eliminar camiones por rango de tiempo')
    elif opcion == 'g':
        print('Cola de camiones que superan tiempo estimado')
    elif opcion == 'h':
        placa = input('Ingrese la placa del camión: ')
        origen = input('Ingrese el lugar de origen: ')
        destino = input('Ingrese el lugar de destino: ')
        crearCamion(placa, origen, destino)
    elif opcion == 'i':
        salida = True
    else:
        print('Opción no válida')