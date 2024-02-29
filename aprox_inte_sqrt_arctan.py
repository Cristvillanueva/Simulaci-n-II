import math
import random
suma = 0
n = 100000000 #Cantidad de numeros aleatorios
error = 10E-16 #Error para determinar el valor de n significativo.
for i in range(1,n+1):
    x = math.sqrt(math.atan(random.random())); #aplica raiz de arctan(x) donde x es un uniforme(0,1)
    suma += x; #Va sumando los valores de g(xi)
    if i>1 and abs(suma/i - (suma-x)/(i-1)) < error: #Determina si la aproximacion de la integral
        # con i numeros es mejor a la de i-1 numeros. Buscando una convergencia por la ley fuerte de los grandes numeros.
        break #Sale del ciclo y la condicion porque encontramos una aproximacion a la integral adecuado
print("El tamaño de una muestra buena es ",i-1, "para un error de ", error) 
aprox = (suma-x)/(i-1) #Valor aproximado de la integral raiz de arctan(x) de 0 a 1. 
print("El valor aproximado de la integral es:", aprox)