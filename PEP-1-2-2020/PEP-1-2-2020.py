#No se pueden usar ciclos for y funciones propias. 
# Para esta evaluación se le solicita construir un programa en Python en el cual el usuario
# pueda ingresar cuántas palabras desee y que entregue como resultado cuál es la palabra
# con la puntuación más alta, y el valor de esa puntuación. Para ello considere que la tabla 1
# muestra el valor asociado a cada letra, donde el símbolo “?” denota a un comodín (que
# puede reemplazar cualquier letra).

#------------------------------------------------------------------------------------------------
#                                           Desarrollo
# (Se utilizó la forma mas primitiva para implementar la solución, dado que, en primera instancia es la mas intuitiva.)
palabras = []
opcion = 0
puntaje = 0
num = 0
while opcion!=1:
    p = input("Ingrese una palabra: ")
    palabras.append(p)
    num += 1
    print("\n")

    choise = input("¿Desea ingresar otra palabra? S/N: ")
    
    if (choise == "N"):
        #Aqui se realiza el calculo del puntaje

        while(num != 0):
            word = palabras[num-1]

            word = word.upper()

            tamP = len(word)
            i = 0
            while (i != tamP):
                flag = 0
                if (tamP > 1 and i<(tamP-1)):
                    if ((word[i]+word[i+1]) == "CH"):
                        puntaje += 5
                        i +=2
                        if (i>=tamP):
                            break
                        else:
                            if (word[i] == "C" or word[i] == "L" or word[i] == "R"):
                                flag = 1
                                i -= 1
                    if (((word[i]+word[i+1]) == "LL") and i<(tamP-1)):
                        puntaje += 8
                        i +=2
                        if (i>=tamP):
                            break
                        else:
                            if (word[i] == "C" or word[i] == "L" or word[i] == "R"):
                                flag = 1
                                i -=1
                    if (((word[i]+word[i+1]) == "RR") and i<(tamP-1)):
                        puntaje += 8
                        i +=2
                        if (i>=tamP):
                            break
                        else:
                            if (word[i] == "C" or word[i] == "L" or word[i] == "R"):
                                flag = 1
                                i -= 1
                if (flag == 0):
                    if (word[i] == "A"):
                        puntaje += 1
                    if (word[i] == "B"):
                        puntaje += 3
                    if (word[i] == "C"):
                        puntaje += 3
                    if (word[i] == "D"):
                        puntaje += 2
                    if (word[i] == "E"):
                        puntaje += 1
                    if (word[i] == "F"):
                        puntaje += 4
                    if (word[i] == "G"):
                        puntaje += 2
                    if (word[i] == "H"):
                        puntaje += 4
                    if (word[i] == "I"):
                        puntaje += 1
                    if (word[i] == "J"):
                        puntaje += 8
                    if (word[i] == "K"):
                        puntaje += 8
                    if (word[i] == "L"):
                        puntaje += 1
                    if (word[i] == "M"):
                        puntaje += 3
                    if (word[i] == "N"):
                        puntaje += 1
                    if (word[i] == "Ñ"):
                        puntaje += 8
                    if (word[i] == "O"):
                        puntaje += 1
                    if (word[i] == "P"):
                        puntaje += 3
                    if (word[i] == "Q"):
                        puntaje += 5
                    if (word[i] == "R"):
                        puntaje += 1
                    if (word[i] == "S"):
                        puntaje += 1
                    if (word[i] == "T"):
                        puntaje += 1
                    if (word[i] == "U"):
                        puntaje += 1
                    if (word[i] == "V"):
                        puntaje += 4
                    if (word[i] == "W"):
                        puntaje += 10
                    if (word[i] == "X"):
                        puntaje += 8
                    if (word[i] == "Y"):
                        puntaje += 4
                    if (word[i] == "Z"):
                        puntaje += 10
                i+=1
            num -= 1
        print("El puntaje total obtenido es: "+str(puntaje))
        opcion = 1
        
