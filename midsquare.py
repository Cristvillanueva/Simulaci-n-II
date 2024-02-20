#Villanueva Menodoza Cristian Arturo - Mid Square Method
import time
import sys
xnu = 1000000
cien = 100
millns = 100000000

t0 = time.time()
num = int(input("Introduce el numero de ocho digitos:")) #Semilla
cant = int(input("Introduce la cantidad de aleatorios:")) #Cantidad de numero aleatorios.
print("Los números aleatorios son:")
semilla = num
matriz = [0] * (cant+1)
matriz[0] = semilla

for i in range(cant):
    model = num % xnu
    #print(model)
    valor = model // cien
    #print(valor)
    if valor == 0:
        print("La ejecución se detiene aquí por que llegamos a un cero.")
        sys.exit()
    else:
        cuadra = valor ** 2
        #print(cuadra)
        num = cuadra
        matriz[i+1] = num
        for j in range(i):
            if matriz[i+1]==matriz[j]:
                print("La ejecución se detiene porque llegamos a un ciclo.")
                sys.exit()
        j=0
        #if num == semilla:
        #    print("La ejecución se detiene porque llegamos a un ciclo.")
        #    sys.exit()    
        aleatorio = cuadra / millns
        print(aleatorio)
        # print(valor)
        # print(cuadra)
        
t1 = time.time()
tiempo_ejecucion = t1 - t0
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")