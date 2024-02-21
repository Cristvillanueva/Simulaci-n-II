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
cantidad_digitos = len(str(numero_tabla[0])) #Determina la cantidad de digitos que tienen lo numeros
#--de la tabla
if 0 < numero_tabla[0] < 1:
    numero_tabla_decimal = numero_tabla
else:
    numero_tabla_decimal = [x / (10**cantidad_digitos) for x in numero_tabla] #Pasar a decimales nuestra lista.
t = len(numero_tabla) #Número de datos totales
clase = int(round(math.sqrt(t))) #Redondea a la raíz del Total de datos
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
#print(xic) 

# Nivel de significancia (alpha)
alpha = 1- (confi/100) #Calcula la probabilidad de cometer error tipo I.
grados_de_libertad = clase-1  # Grados de libertad

# Calcular el valor crítico
valor_critico = chi2.ppf(1 - alpha, grados_de_libertad)
#print(valor_critico)
if xic <= valor_critico:
    print("\nNo se rechaza H_0, es decir, no hay diferencia entre la distribucion de la muestra y la distribucion teoria de U(0,1). Con un", grados_de_libertad, "grados de libertad y ", 1-alpha, "nivel de confianza.")

