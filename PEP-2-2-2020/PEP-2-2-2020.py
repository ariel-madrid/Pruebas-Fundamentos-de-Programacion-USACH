import Jojojo as jojo

#FALTA DOCUMENTAR

def mediaBondad():
    archivoBondad = jojo.leer_archivo("bondad.txt")
    data = []
    k = 0
    while k < len(archivoBondad):
        archivoBondad[k] = archivoBondad[k].split(",")
        data.append(archivoBondad[k])
        k += 1
    

    mediaPorPersona = []
    p = 0
    while p < len(data):
        suma = 0
        media = 0
        contador = 0
        i = 1
        while i < len(data[p]):
            if (i==(len(data[p])-1)):
                aux = data[p][i].split(" ")
                data[p][i] = aux[0]
            contador += 1
            suma += float(data[p][i])
            i += 1
        media = suma/contador

        listaAux = []
        listaAux.append(data[p][0])
        listaAux.append(str(media))
        mediaPorPersona.append(listaAux)

        p += 1
    return mediaPorPersona

def asignarRegalos(mediaPorPersona):
    pedidos = jojo.leer_archivo("pedidos.txt")
    
    numRegalosPorPersona = []
    k = 0
    while k < len(mediaPorPersona):
        if float(mediaPorPersona[k][1])>=6.5 and float(mediaPorPersona[k][1])<=7.0:
            numRegalosPorPersona.append(5)
        elif float(mediaPorPersona[k][1])>=6.0 and float(mediaPorPersona[k][1])<=6.4:
            numRegalosPorPersona.append(4)
        elif float(mediaPorPersona[k][1])>=5.5 and float(mediaPorPersona[k][1])<=5.9:
            numRegalosPorPersona.append(3)
        elif float(mediaPorPersona[k][1])>=5.0 and float(mediaPorPersona[k][1])<=5.4:
            numRegalosPorPersona.append(2)
        elif float(mediaPorPersona[k][1])>=4.0 and float(mediaPorPersona[k][1])<=4.9:
            numRegalosPorPersona.append(1)
        elif float(mediaPorPersona[k][1])>=1.0 and float(mediaPorPersona[k][1])<=3.9:
            numRegalosPorPersona.append("Carbon")
        k+=1
        
    regalos = []
    k = 0
    while k < len(pedidos):
        pedidos[k] = pedidos[k].split(",")
        regalos.append(pedidos[k][0:len(pedidos[k])])
        k +=1
    k = 0
    while k < len(regalos):
        tam = len(regalos[k])-1
        aux = regalos[k].pop(tam)
        aux = aux.split("\n")
        regalos[k].append(aux[0])
        k += 1

    totalRegalos = []

    i = 0
    while i < len(regalos):
        flag = 0
        k = 0
        while k < len(mediaPorPersona):
            if (regalos[i][0] == mediaPorPersona[k][0]):
                flag = 1
            k += 1

        if (flag == 1):
            gift = []
            #Por aqui pasan solo los que reciben regalos
            if numRegalosPorPersona[i] == "Carbon":
                gift.append(regalos[i][0])
                gift.append("Carbon")
            elif (len(regalos[i])-1) <= numRegalosPorPersona[i]:
                gift.append(regalos[i][0])
                j = 1
                while j < len(regalos[i]):
                    gift.append(regalos[i][j])
                    j += 1
            elif (len(regalos[i])-1) == 0:
                gift.append(regalos[i][0])
                gift.append("Bicicleta")
            elif (len(regalos[i])-1) >= numRegalosPorPersona[i]:
                j = 1
                gift.append(regalos[i][0])
                while j < (numRegalosPorPersona[i]+1):
                    gift.append(regalos[i][j])
                    j +=1
            totalRegalos.append(gift)
        i += 1

    salida = []
    k = 0
    while k < len(totalRegalos):
        string = ""
        i = 0
        while i < len(totalRegalos[k]):
            string += totalRegalos[k][i]+", "
            i += 1
        string = string[0:len(string)-2]
        string = string+"\n"
        salida.append(string)
        k += 1

    jojo.escribir_archivo("regalos.txt",salida)

def main():

    mediaPorPersona = mediaBondad()
    asignarRegalos(mediaPorPersona)

if __name__ == "__main__":
    main()