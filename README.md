# Empresa de logística

En una empresa de logística, se gestiona el movimiento diario de camiones que transportan
mercancías entre diferentes puntos de distribución. Cada camión tiene asignada una placa, un
punto de distribución Origen, un punto de distribución Destino, una hora de salida de origen, una
hora de llegada a destino, y un tiempo estimado de viaje. Al llegar al punto de distribución de destino
se calcula el tiempo de viaje.

***

Se deberá desarrollar una aplicación utilizando las estructuras de datos necesarias. Se desea tener
un menú con las siguientes opciones:
- a. Registrar partidas de puntos de distribución, modificar información y eliminar camión: Permite
registrar la salida de un nuevo camión, modificar su información o eliminarlo, utilizando su
placa como referencia.
- b. Registrar llegada de camión: Registra la llegada de un camión al punto de distribución destino,
calculando el tiempo de viaje.
- c. Listado de camiones: Muestra un listado completo de todos los camiones que están registrados
con viaje asignado, incluyendo su placa, hora de salida, punto de origen/destino y hora de llegada
(en caso que haya finalizado el viaje).
- d. Informe de movimientos por punto de distribución: Genera un informe que indica la cantidad
de camiones que han llegado o salido de cada punto de distribución durante un período de horas
determinado.
- e. Camiones en horario de mayor actividad: Muestra los camiones que han llegado al punto de
distribución durante el horario de mayor actividad, que comprende desde las 8:00 hasta las
12:00 y desde las 14:00 hasta las 18:00.
- f. Eliminar camiones que llegaron después de cierto horario: Permite eliminar los registros de
camiones que han ingresado al centro logístico después de un horario específico, liberando
espacio en la base de datos.
- g. Generar una cola de camiones que superan el tiempo estimado de viaje. Listar la cola cada vez
que se elija esta opción (tengan cuidado de no dejar la cola vacía al terminar de listar).

> La consigna del ejercicio era hacerlo solo usando Python y sus estructuras basicas
