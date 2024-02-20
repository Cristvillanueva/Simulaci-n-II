#Villanueva Mendoza Cristian Arturo - Determinar los números de 4 cifras que se ciclen 
#inmediatamente con Mid Square Method.

import time

xnu = 1000000
cien = 100
ultimo = 9999
matriz = [] #Reservamos una matriz para guardar los números que se ciclen inmeditamente.

t0 = time.time()
print("Los números entre 0001 y 9999 que se ciclan inmediatamente son:") #Recordando que la tarea
#especificaba número de cuatro digitos. 
for i in range(1, ultimo): 
    var = i #Semilla
    num = var ** 2 #Se eleva al cuadrado el número, esto proviene del método de Von Neumman. 
    model = num % xnu #Al sacar el modulo con xnu nos dara el residuo que hay entre un número de 1000000
    valor = model // cien #Al dividirlo entre 100, eliminara dos cero de la izquierda, quedandose asi con
    #las cuatro cifras centrales
    if valor == var: #Si el número de cuatro cifras es la semilla, entonces se ciclo inmediatamente.
        matriz.append(var) #Guardamos el valor que se ciclo inmediatamente. 
        print(matriz[-1])  # Imprimimos el último elemento agregado a la matriz
t1 = time.time()
tiempo_ejecucion = t1 - t0
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")