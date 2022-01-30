# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA - PRUEBA RECUPERATIVA - ARIEL ARGOMEDO ESTUDIANTE DE CUARTO AÑO
# CARRERA: Ingeniería Civil Informatica

#Registro de usuario: ID interno del usuario, cada linea de registro contiene: 
#                     - Fecha y hora en que se escucho cada cancion
#                     - La cancion y su artista
#                     - Genero al que pertenece
#                     - Duracion de la cancion
# (Separados por coma)

# Se solicita:
# Spotify desea generar un programa que permita al usuario, a
# partir de su ID y un mes del año, ver su actividad durante ese período en específico: 
# - Un gráfico de los minutos escuchados por cada género.
# - Su Top 10 de artistas de ese período.

import matplotlib.pyplot as plt

def leerArchivo(archivoEntrada):
    entr = "User"+archivoEntrada+".txt"
    usuario = open(entr,'r')
    
    fecha_horaReproduccion = []
    nombreCancion = []
    artistaCancion = []
    generoCancion = []
    duracionCancion = []
    #Los datos estan separados por linea, cada dato importante está separado por comas.
    for linea in usuario:
        separatedData = linea.split(',')
        fecha_horaReproduccion.append(separatedData[0])
        nombreCancion.append(separatedData[2])
        artistaCancion.append(separatedData[1])
        generoCancion.append(separatedData[3])
        duracionCancion.append(separatedData[4])

    return fecha_horaReproduccion,nombreCancion,artistaCancion,generoCancion,duracionCancion

def tiempoPorGenero(generoCancion,duracionCancion):
    
    totalGeneros = []
    for genero in generoCancion:
        flag = 0
        if len(totalGeneros) == 0:
            totalGeneros.append(genero)
        for elemento in totalGeneros:
            if elemento == genero:
                flag = 1
        if flag == 0:
            totalGeneros.append(genero)

    tiempoTotalPorGenero = []

    for em in totalGeneros:
        tiempoTotalPorGenero.append(0)

    for k in range(len(generoCancion)):
        id = 0
        
        for i in range(len(totalGeneros)):
            if generoCancion[k] == totalGeneros[i]:
                id = i

        tiempo = duracionCancion[k].split(':')
        tiempo[0] = int(tiempo[0])
        tiempo[1] = int(tiempo[1])

        #Debo pasar a segundos el tiempo
        tiempoSegundo = tiempo[0]*60 + tiempo[1]
        tiempoTotalPorGenero[id] += tiempoSegundo
    

    minutos = []
    for seg in tiempoTotalPorGenero:
        resto = seg%60
        if resto != 0:
            time = seg//60

        minutos.append(time)

    plots = plt.bar(totalGeneros,minutos)

    plt.legend("Tiempo en minutos")
    plt.xlabel("Genero")
    plt.ylabel("Tiempo total escuchado")
    plt.title("Comparación tiempo escuchado por genero")
    plt.show()

def ranking(fecha_horaReproduccion, artistaCancion,year,month):
    totalArtistas = []

    for artista in artistaCancion:
        flag = 0
        if (len(totalArtistas) == 0):
            totalArtistas.append(artista)
        else:
            for i in range(len(totalArtistas)):
                if artista == totalArtistas[i]:
                    flag = 1

            if flag == 0:
                totalArtistas.append(artista)

    totalReproducciones = []

    for elem in totalArtistas:
        totalReproducciones.append(0)

    for k in range(len(fecha_horaReproduccion)):
        fecha = fecha_horaReproduccion[k].split(' ')[0]
        fecha = fecha.split('-')
        anio = int(fecha[0])
        mes = int(fecha[1])

        if (year >= anio):
            if (month >= mes):
                #Se busca al artista 
                id = 0
                for i in range(len(totalArtistas)):
                    if (artistaCancion[k] == totalArtistas[i]):
                        id = i 
                totalReproducciones[id] += 1
 
    if month < 10:
        month = "0"+str(month)
    ficheroSalida = "TOP-"+"10-"+str(year)+"-"+str(month)+".txt"
    salida = open(ficheroSalida,'w')

    top = 1
    flag = 0
    counter = 1
    while top<=10:
        max = 0
        for i in range(len(totalReproducciones)):
            if totalReproducciones[i]>max:
                max = totalReproducciones[i] 
                id = i
                flag = 1

        if (flag == 1):
            escribir = str(counter)+". "+totalArtistas[id]+", "+str(max)+" reproducciones\n"
            salida.write(escribir)
            flag = 0
            totalReproducciones.pop(id)
            totalArtistas.pop(id)
            counter += 1

        top += 1

def main():
    archivoEntrada = input('Ingrese ID usuario: ')
    anhoMes = input('Ingrese fecha: ')
    
    #Se lee la informacion del fichero de entrada
    fecha_horaReproduccion,nombreCancion,artistaCancion,generoCancion,duracionCancion = leerArchivo( archivoEntrada)

    #Generar grafico que muestre minutos por genero escuchados.
    tiempoPorGenero(generoCancion,duracionCancion)

    anhoMes = anhoMes.split('-')
    anho = int(anhoMes[0])
    mes = int(anhoMes[1])


    fecha = fecha_horaReproduccion[0].split(' ')[0]
    fecha = fecha.split('-')
    anio = int(fecha[0])
    mes2 = int(fecha[1])


    #Generar archivo de salida "TOP-10-AÑO-MES.TXT" con los 10 artistas mas escuchados
    if (anho < anio):
        print("No se encuentran registros para la fecha indicada")
    else:
        ranking(fecha_horaReproduccion,artistaCancion,anho,mes)

#Validacion
if (__name__ == '__main__'):
    main()
