# Pregunta 1
# - a) El tipo de dato int corresponde a enteros de 32 bits. En cambio, long se usa para evitar overflow donde el tamaño 
# está limitado por el tamaño de la memoria de la maquina. 
# Double es usado para valores númericos de coma flotante que es capaz de abordar un gran espectro evitando rapidamente el overflow.

# Pregunta 2
# Los elementos mas importantes que componen una CPU según el modelo de Von Neumann son la Unidad Logica Aritmetica y la Unidad de Control.

#Pregunta 3
import math
import numpy as np
#Area de un octagono
t = int(input("Ingrese un valor de t: "))
A = (8*pow(t,2))/(4*math.tan((np.pi/8)))

print("El area del octagono para el valor de t ingresado es: "+str(A))