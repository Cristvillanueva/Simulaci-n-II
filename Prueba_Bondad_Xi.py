from scipy.stats import chi2
import math
confi = int(input("Introduce la confianza de la prueba en porcentaje:")) #Confianza
#de la prueba.
xic = 0.0 #Reservamos la variable xic que sea nuestro estadistico que aplicaremos la prueba.
uno = 1

numero_tabla = [38, 33, 25, 5, 69, 35, 98, 52, 12, 79,
                50, 46, 95, 42, 49, 11, 78, 34, 2, 43,
                7, 50, 5, 91, 77, 18, 21, 4, 17, 62,
                91, 36, 48, 88, 52, 76, 99, 73, 82, 90]

#numero_tabla = [0.8797, 0.3884, 0.6289, 0.8750, 0.5999, 0.8589, 0.9996, 0.2415, 0.3808, 0.9606,
#                0.9848, 0.3469, 0.7977, 0.5844, 0.8147, 0.6431, 0.7387, 0.5613, 0.0318, 0.7401,
#                0.4557, 0.1592, 0.8536, 0.8846, 0.3410, 0.1492, 0.8681, 0.5291, 0.3188, 0.5992,
#                0.9170, 0.2204, 0.5991, 0.5461, 0.5739, 0.3254, 0.0856, 0.2258, 0.4603, 0.5027,
#                0.8376, 0.6235, 0.3681, 0.2088, 0.1525, 0.2006, 0.4720, 0.4272, 0.6360, 0.0954]
if 0 < max(numero_tabla) < 1:
    numero_tabla_decimal = numero_tabla
else:
    cantidad_digitos = len(str(int(max(numero_tabla)))) #Determina la cantidad de digitos que tienen lo numeros
    #--de la tabla
    numero_tabla_decimal = [x / (10**cantidad_digitos) for x in numero_tabla] #Pasar a decimales nuestra lista.
t = len(numero_tabla) #Número de datos totales
clase = 5#int(round(math.sqrt(t))) #Redondea a la raíz del Total de datos
#--int cambia el valor de decimal a entero.
E = t/clase #Se requiere en la formula los Ei

division_uniforme = 1/clase #Dividira la densidad uniforme entre el total de clases
#--esto nos permitira realizar intervalos. 
for i in range(clase):
    contador = 0
    for j in range(t):
        if (division_uniforme*i)<=numero_tabla_decimal[j]<(division_uniforme*(i+1)):
            contador +=1   
    xic = xic + (contador-E)**2
    #print(contador)
xic = xic/E
print("El valor del estimador es: ",xic) 

# Nivel de significancia (alpha)
alpha = 1- (confi/100) #Calcula la probabilidad de cometer error tipo I.
grados_de_libertad = clase-1  # Grados de libertad

# Calcular el valor crítico
valor_critico = chi2.ppf(1 - alpha, grados_de_libertad)
print("El valor critico es: ",valor_critico)
if xic <= valor_critico:
    print("\nNo se rechaza H_0, es decir, no hay diferencia entre la distribucion de la muestra y la distribucion teoria de U(0,1). Con un", grados_de_libertad, "grados de libertad y ", 1-alpha, "nivel de confianza.")

