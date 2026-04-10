# Ejercicios:
# 1. Crear variables de diferentes tipos: int, float, str, bool, list, dict
# 2. Convertir tipos: str a int, float a int, int a float
# 3. Usar f-strings para formatear: "El usuario tiene X años"

entero = 19
flotante = 1.0
texto = "Erick"
boleano = True
lista = ["Uno", "Dos", "Tres", "Cuatro"]
diccionario = {"Nombre": "Erick", "Edad": 19}

str_int = "1"
int(str_int)
flo_int = 1.0
int(flo_int)
int_flo = 2
int(int_flo)

print(f"El nombre del usuario es {texto} y tiene {entero}")

# # Ejercicios:
# 1. Crear un programa que determine si un número es positivo, negativo o cero
# 2. Crear un menú con if-elif-else
# 3. Usar un loop for para iterar sobre una lista
# 4. Usar while para calcular factorial

lisnumero = [1, 2, 3, 5, 6, 4, 8, 3, 5, 7, 5]
print("----------------------Menu-----------------------")
print("1. Determinar si un numero es +,- o 0")
print("2. Usar un loop for para iterar sobre una lista")
print("3. Usar un ciclo while para calcular un factorial")
op = int(input("Ingresa el numero de opcion: "))
if op == 1:
    num = int(input("Ingresa el numero a determinar: "))
    if num > 0:
        print("El numero es positivo")
    elif num < 0:
        print("El numero es negativo")
    elif num == 0:
        print("El numero es 0")
elif op == 2:
    for x in lisnumero:
        print(x)
elif op == 3:
    numf = int(input("Ingrese el numero para sacar factorial: "))
    numf2 = numf
    while numf2 > 1:
        numf2 = numf2 - 1
        print(numf2)
        numf = numf * numf2
    print(f"El numero en factorial es: {numf}")
else:
    print("Opcion no valida")

# # Crear funciones para:
# 1. Calcular el área de un círculo
# 2. Convertir Celsius a Fahrenheit
# 3. Calcular el promedio de una lista
# 4. Encontrar el valor máximo y mínimo
promlist = [10, 8, 9, 7, 10, 6]
total = 0
print("----------------------Menu-----------------------")
print("1. Calcular area de un circulo")
print("2. Conevrtir Celsius a Fahrenheit")
print("3. Calcular el promedio de una lista")
print("4. Encontrar el valor maximo y minimo")
op = int(input("Ingresa el numero de opcion: "))
if op == 1:
    radius = int(input("Ingresa el radio: "))
    pi = 3.1416
    area = pi * (radius ^ 2)
    print(f"El area del circulo es: {area}")
elif op == 2:
    tempc = int(input("Ingresa la temperatura en celsius"))
    tempf = (1.8 * tempc) + 32
    print(f"Temperatura en Fahrenheit: {tempf}")
elif op == 3:
    for x in promlist:
        total = total + x
    prom = total / len(promlist)
elif op == 4:
    for x in promlist:
        print(x)
    print(f"Valor maximo de la lista: {max(promlist)}")
    print(f"Valor minimo de la lista: {min(promlist)}")
