from dis import dis
import matplotlib.pyplot as plt
from datetime import datetime

#FALTA DOCUMENTAR


#El bote puede navegar por 3 dias.
#Avanza "a" millas en tres dias
#Cuando se detiene por un dia, se mueve "b" millas hacia atras
#El destino está a "c" millas.

#Tiempo en microsegundos
def calcular_tiempo_transcurrido(inicio, termino):
    return (termino - inicio).total_seconds() * 1000000

def leerFichero():
    entrada = open("entrada.txt","r")
    line = []
    for linea in entrada:
        aux = []
        linea = linea.split(" ")
        ultimo = linea.pop(len(linea)-1).split("\n")[0]
        for dato in linea:
            dato = int(dato)
            aux.append(dato)
        aux.append(int(ultimo))
        line.append(aux)
    
    return line

def formaIterativa(barco):
    distanciaRecorrida = 0
    dia = 0
    #Si la distancia que avanza es menor a la distancia que se devuelve en el dia de reposo, entonces no va a llegar
    if (barco[0] <= barco[1]):
        dia = -1
    else:
        #Empezar a tomar tiempo
        while distanciaRecorrida <= barco[2]:
            #Luego de tres dias ha recorrido una distancia adicional de barco[i][0]
            dia += 3
            distanciaRecorrida += barco[0]

            #Al cuarto dia se le descuentan barco[i][1] millas
            dia += 1
            distanciaRecorrida -= barco[1]
        #Terminar toma de tiempo
    return dia

def formaRecursiva(barco,distanciaRecorrida, dias):
    if barco[0] <= barco[1]:
        return -1
    if distanciaRecorrida > barco[2]:
        return dias
    else:
        d = distanciaRecorrida+barco[0]-barco[1]
        dias += 4
        return formaRecursiva(barco,d,dias)

def escribirArchivoSalida(datosEntrada,diasIter,tiempoIter,diasRecur,tiempoRecur):
    salida = open("salida.txt","w")
    for i in range(len(datosEntrada)):
        string = ""
        string = str(datosEntrada[i][0])+" "+str(datosEntrada[i][1])+" "+str(datosEntrada[i][2])+" "+str(diasIter[i])+" "+str(tiempoIter[i])+" "+str(tiempoRecur[i])+"\n"
        salida.write(string)
    
def graficoLineas(tiempoIter, tiempoRecur):
    #Ordenar de menor a mayor tiempoIter
    for i in range(len(tiempoIter)):
        for j in range(len(tiempoIter)):
            if (tiempoIter[i] < tiempoIter[j]):
                aux = tiempoIter[i]
                tiempoIter[i] = tiempoIter[j]
                tiempoIter[j] = aux
    
    #Ordenar de menor a mayor tiempoRecur
    for i in range(len(tiempoRecur)):
        for j in range(len(tiempoRecur)):
            if (tiempoRecur[i] < tiempoRecur[j]):
                aux = tiempoRecur[i]
                tiempoRecur[i] = tiempoRecur[j]
                tiempoRecur[j] = aux

    barco = []
    for i in range(0,len(tiempoIter)):
        barco.append(i)

    plt.plot(barco,tiempoIter,"-o")
    plt.plot(barco,tiempoRecur,"-o")

    for i in range(len(tiempoIter)):
        plt.text(barco[i], tiempoIter[i], "Barco "+str(i), fontsize=6, color = "g", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='right', rotation=90)

    for i in range(len(tiempoIter)):
        plt.text(barco[i], tiempoRecur[i], "Barco "+str(i), fontsize=6, color = "g", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='right', rotation=90)

    plt.title("Tiempos ejecucion funcion Iterativa y Recursiva")
    plt.xlabel("Id barco (Según orden de aparicion en fichero)")
    plt.ylabel("Tiempo (microsegundo)")
    plt.legend(["Tiempo Iterativo","Tiempo Recursivo"])
    plt.show()

def main():
    datosEntrada = leerFichero()
    i = 0
    diasIter = []
    #Para cada barco 
    tiempoIter = []
    while i<len(datosEntrada):
        inicio = datetime.now()
        dias = formaIterativa(datosEntrada[i])
        termino = datetime.now()
        tiempo = calcular_tiempo_transcurrido(inicio, termino)
        tiempoIter.append(tiempo)
        diasIter.append(dias)
        i+=1
    
    i = 0
    diasRecur = []
    #Para cada barco
    tiempoRecur = []
    while i<len(datosEntrada):
        inicio = datetime.now()
        dias = formaRecursiva(datosEntrada[i],0,0)
        termino = datetime.now()
        tiempo = calcular_tiempo_transcurrido(inicio, termino)
        tiempoRecur.append(tiempo)
        diasRecur.append(dias)
        i+=1

    escribirArchivoSalida(datosEntrada,diasIter,tiempoIter,diasRecur,tiempoRecur)

    #Grafico de lineas
    graficoLineas(tiempoIter,tiempoRecur)
if __name__ == "__main__":
    main()