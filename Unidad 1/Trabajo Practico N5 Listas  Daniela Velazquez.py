# Ejercicio 1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja

notas= [9,7,8,6,5,4,3,2,1,10]
print("Lista completa de notas:", notas)
promedio= sum(notas)/len(notas)
print("El promedio de las notas es:", promedio)
nota_mas_alta= max(notas)
nota_mas_baja= min(notas)
print("La nota más alta es:", nota_mas_alta)
print("La nota más baja es:", nota_mas_baja)

# Ejercicio 2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista
productos= []
for i in range(5):
    producto= input("Ingrese el nombre del producto: ")
    productos.append(producto)
print("Lista de productos ordenada alfabéticamente:", sorted(productos))
producto_a_eliminar= input("Ingrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Lista actualizada de productos:", productos)

# Ejercicio 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random
numeros= [random.randint(1, 100) for _ in range(15)]
print("Lista de números generados:", numeros)
pares= [num for num in numeros if num % 2 == 0]
impares= [num for num in numeros if num % 2 != 0]
print("Lista de números pares:", pares)
print("Cantidad de números pares:", len(pares))
print("Lista de números impares:", impares)
print("Cantidad de números impares:", len(impares))

#Ejercicio 4) Dada una lista con valores repetidos: 
# datos = [1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado

datos = [1,3,5,3,7,1,9,5,3]
datos_sin_repetidos= list(set(datos))
print("Lista sin elementos repetidos:", datos_sin_repetidos)

# Ejercicio 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

estudiantes= ["Ana", "Luis", "Carlos", "Marta", "Sofia", "Jorge", "Lucia", "Pedro"]
accion= input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").upper()
if accion == "A":
    nuevo_estudiante= input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Lista actualizada de estudiantes:", estudiantes)
elif accion == "E":
    estudiante_a_eliminar= input("Ingrese el nombre del estudiante que desea eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print("Lista actualizada de estudiantes:", estudiantes)
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Acción no válida.")
    
# Ejercicio 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).
numeros= [10, 20, 30, 40, 50, 60, 70]
numeros_rotados= [numeros[-1]] + numeros[:-1]
print("Lista original:", numeros)
print("Lista rotada una posición a la derecha:", numeros_rotados)

#Ejercicio 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.
temperaturas= [
    [15, 25],  # Día 1
    [17, 27],  # Día 2
    [14, 30],  # Día 3
    [16, 26],  # Día 4
    [18, 28],  # Día 5
    [19, 29],  # Día 6
    [13, 24]   # Día 7
]
minimas= [temp[0] for temp in temperaturas]
maximas= [temp[1] for temp in temperaturas]
promedio_minimas= sum(minimas)/len(minimas)
promedio_maximas= sum(maximas)/len(maximas)
print("Promedio de temperaturas mínimas:", promedio_minimas)
print("Promedio de temperaturas máximas:", promedio_maximas)
amplitudes= [maxi - mini for mini, maxi in temperaturas]
mayor_amplitud= max(amplitudes)
dia_mayor_amplitud= amplitudes.index(mayor_amplitud) + 1
print("El día con mayor amplitud térmica fue el día", dia_mayor_amplitud, "con una amplitud de", mayor_amplitud) 

#Ejercicio 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
notas= [
    [8, 7, 9],  # Estudiante 1
    [6, 5, 7],  # Estudiante 2
    [9, 8, 10], # Estudiante 3
    [5, 6, 4],  # Estudiante 4
    [7, 9, 8]   # Estudiante 5
]
for i, estudiante in enumerate(notas):
    promedio_estudiante= sum(estudiante)/len(estudiante)
    print("Promedio del Estudiante", i+1, ":", promedio_estudiante)
for j in range(len(notas[0])):
    promedio_materia= sum(notas[i][j] for i in range(len(notas)))/len(notas)
    print("Promedio de la Materia", j+1, ":", promedio_materia)

# Ejercicio 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.
tablero= [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()
mostrar_tablero(tablero)
for turno in range(9):
    jugador= "X" if turno % 2 == 0 else "O"
    fila= int(input(f"Jugador {jugador}, ingrese la fila (0-2): "))
    columna= int(input(f"Jugador {jugador}, ingrese la columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        mostrar_tablero(tablero)
    else:
        print("Casilla ya ocupada, intente de nuevo.")
        turno -= 1

# Ejercicio 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana
ventas= [
    [10, 15, 20, 25, 30, 35, 40],  # Producto N1
    [5, 10, 15, 20, 25, 30, 35],   # Producto N2
    [8, 12, 16, 20, 24, 28, 32],   # Producto N3
    [7, 14, 21, 28, 35, 42, 49]    # Producto N4
]
for i, producto in enumerate(ventas):
    total_producto= sum(producto)
    print("Total vendido del Producto", i+1, ":", total_producto)
ventas_diarias= [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_mayores_ventas= ventas_diarias.index(max(ventas_diarias)) + 1
print("El día con mayores ventas totales fue el día", dia_mayores_ventas)
total_semanal_productos= [sum(ventas[i]) for i in range(4)]
producto_mas_vendido= total_semanal_productos.index(max(total_semanal_productos)) + 1
print("El producto más vendido en la semana fue el Producto", producto_mas_vendido)     



      

