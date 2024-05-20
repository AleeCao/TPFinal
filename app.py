from TAD_Camion import *
from TAD_Tareas import *
import os
from TAD_Cargado import cargarCamiones

camiones = registroCamiones()
cargarCamiones(camiones)
salida = False
while not salida:
    os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')
        print('a. Registrar partida\nb. Modificar información\nc. Eliminar camión')
        opcion2 = input('Seleccione una opción: ')
        if opcion2 == 'a':
            placa = input('Ingrese la placa del camión: ')
            salida = input('Ingrese la hora de salida: ')
            tiempoEst = input('Ingrese el tiempo estimado de viaje: ')
            print(registrarSalida(placa, camiones, salida, tiempoEst))
        elif opcion == 'b':
            placa = input('Ingrese la placa del camión: ')
            atributo = input('Ingrese el atributo a modificar: ')
            valor = input('Ingrese el nuevo valor: ')
            print(registrarLlegada(placa, camiones, atributo, valor))
        elif opcion == 'c':
            placa = input('Ingrese la placa del camión: ')
            print(eliminarCamion(placa ,camiones))
    elif opcion == 'b':
        os.system('cls' if os.name == 'nt' else 'clear')
        placa = input('Ingrese la placa del camión: ')
        llegada = input('Ingrese la hora de llegada: ')
        print(registrarLlegada(placa, camiones, llegada))
    elif opcion == 'c':
        os.system('cls' if os.name == 'nt' else 'clear')
        for camion in camiones:
            for keys, value in camion.items():
                print(keys,':', value)
            print('====================')
        input('\nPresione ENTER para continuar')
    elif opcion == 'd':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Informe de movimientos por punto de distribución')
    elif opcion == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        mayAct = listarMayAct(camiones)
        for camion in mayAct:
            for keys, value in camion.items():
                print(keys,':', value)
            print('====================')
        input('\nPresione ENTER para continuar')
    elif opcion == 'f':
        os.system('cls' if os.name == 'nt' else 'clear')
        limite = input('Ingrese la hora de llegada limite: ')
        print(eliminarCamionXRango(camiones, limite))
    elif opcion == 'g':
        os.system('cls' if os.name == 'nt' else 'clear')
        cola = colaSupTmpEst(camiones)
        for camion in cola:
            for keys, value in camion.items():
                print(keys,':', value)
            print('====================')
        input('\nPresione ENTER para continuar')
    elif opcion == 'h':
        os.system('cls' if os.name == 'nt' else 'clear')
        placa = input('Ingrese la placa del camión: ')
        origen = input('Ingrese el lugar de origen: ')
        destino = input('Ingrese el lugar de destino: ')
        camionX = crearCamion(placa, origen, destino)
        camiones.append(camionX)
    elif opcion == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        input('Gracias por usar el sistema\n\nPresione ENTER para salir')
        salida = True
    else:
        print('Opción no válida')