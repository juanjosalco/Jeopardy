"""
Proyecto Final: Juego de Jeopardy
Juan José Salazar Cortés
Terminado 12/10/21
"""

#Librerias
from random import randint

# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
CYAN = '\033[36m'

#Variables
puntos1 = 0
puntos2 = 0
categorias = ["Lectura", "Matematicas", "Ciencias"]
numPreguntas = 2 #Cantidad de preguntas
turno = 1 #Ver que jugador tiene el turno
lectura = """
    A las ocho de la mañana la mamá de Laura ya se ha tomado su café con tostadas.
    Es hora de despertar a su hija o se hará tarde. Casi a oscuras, se acerca a la
    pequeña cama de madera y busca su carita bajo el edredón para darle un beso de buenos días.

    Laura se despereza, se pone sus zapatillas rojas y se sienta en la soleada cocina.
    Hoy tiene mucha hambre pero por suerte, su madre le ha preparado su desayuno favorito:
    zumo de naranja, tres nueces y un tazón de leche con cereales.

    La niña sabe que esta es la comida más importante del día y que necesita alimentarse bien para
    poder pensar con claridad. Además, hoy hay clase de gimnasia y tiene que practicar la voltereta lateral
    para la actuación de fin de curso.

    Cuando termina, se viste, se lava la cara y los dientes, y se cepilla el cabello.
    Dentro de su mochila mete un cuaderno y siete lápices de colores.

    Su madre aparece sonriendo y le da un paquetito con un par de galletas ¡Está creciendo y necesitará reponer fuerzas a media mañana!
    Laura, como todos los días, acude al colegio feliz y con ganas de aprender muchas cosas.
"""

#Funcion para obtener nombres de jugadores
def jugadores():
    print(" + + + Bienvenidos a Jeopardy! + + + \n")
    input("Presiona <ENTER> para jugar... \n")
    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")
    archivo = open('BaseDeDatos_Juego.txt','a')
    archivo.write("\n\n\tResultados del juego!\n")
    archivo.write("Jugador 1: "+jugador1+"\n")
    archivo.write("Jugador 2: "+jugador2+"\n")
    archivo.close()

    return(jugador1, jugador2)

#Funcion para mostrar tabla de preguntas
def menuPrincipal():
    print(f"+====================+====================+====================+\n|       {categorias[0]}      |     {categorias[1]}    |      {categorias[2]}      |")
    print("----------------------------------------------------------------")
    print("|       1. 100       |       2. 100       |       3. 100       |")
    print("----------------------------------------------------------------")
    print("|       4. 250       |       5. 250       |       6. 250       |")
    print("----------------------------------------------------------------")
    print("|       7. 500       |       8. 500       |       9. 500       |")
    print("----------------------------------------------------------------")
    print("|      10. 1000      |      11. 1000      |      12. 1000      |")
    print("----------------------------------------------------------------")


#Funcion que procesa preguntas y respuestas
def preguntas(numero):
    preguntaElegida = randint(0, 2) #Elige la pregunta al azar con su respectiva respuesta

    preguntasLectura100 = [
        CYAN+"¿De qué está hecha la cama de Laura?"+BLACK,
        CYAN+"¿Quien es Laura?"+BLACK,
        CYAN+ "¿Cuál es la bebida favorita de Laura en el desayuno?"+BLACK,
            ]
    preguntasLectura250 = [
        CYAN+"¿Qué se toma la madre de Laura?"+BLACK,
        CYAN+"¿De qué color son las zapatillas de Laura?"+BLACK,
        CYAN+"¿Dónde se desarrola la historia?"+BLACK,
            ]
    preguntasLectura500 = [
        CYAN+"¿De qué tiene clase Laura?"+BLACK,
        CYAN+"¿Qué tiene que practicar Laura?"+BLACK,
        CYAN+"¿Cuántos lápices de colores mete a su mochila Laura?"+BLACK,
            ]
    preguntasLectura1000 = [
       CYAN+ "¿Qué tipo de texto es este?"+BLACK,
       CYAN+ "¿Qué quiere decir el autor con 'Laura se despereza\'?"+BLACK,
       CYAN+ "¿Qué le da la madre de Laura al despertarla?"+BLACK,
            ]
    preguntasMate100 = [
       CYAN+ "5*8+5"+BLACK,
       CYAN+ "4*3/2"+BLACK,
       CYAN+ "5+37-15"+BLACK,
            ]
    preguntasMate250 = [
       CYAN+ "5*9+15/3"+BLACK,
       CYAN+ "10+5*23+2"+BLACK,
       CYAN+ "4*7+27+9"+BLACK,
            ]
    preguntasMate500 = [
        CYAN+"6+56+76+54+32+1"+BLACK,
        CYAN+ "65*2*2/2+3"+BLACK,
        CYAN+"12*10+12-12*12"+BLACK,
            ]
    preguntasMate1000 = [
       CYAN+ "600+12+33+1+3+3+4+5+666+23+4+-4-233-1"+BLACK,
       CYAN+ "55/5*6*7/2*5*1*2"+BLACK,
       CYAN+ "5*10*2*9+7*7/4*1*6/12"+BLACK,
            ]
    preguntasCiencia100 = [
        CYAN+"¿Qué es la fotosíntesis?"+BLACK,
        CYAN+"¿Por qué el Sol es tan grande y no hay humanos viviendo allí?"+BLACK,
        CYAN+"¿Por qué brilla el Sol?"+BLACK,
            ]
    preguntasCiencia250 = [
        CYAN+"¿Cómo llegaron las estrellas al cielo?"+BLACK,
        CYAN+"¿Por qué la Luna no se cae?"+BLACK,
        CYAN+"¿Por qué el cielo es azul?"+BLACK,
            ]
    preguntasCiencia500 = [
        CYAN+"¿Quién inventó las computadoras?"+BLACK,
        CYAN+"¿Los ladrillos son de un material hecho por el hombre?"+BLACK,
        CYAN+"¿Cuántos tipos de dinosaurios existieron?"+BLACK,
            ]
    preguntasCiencia1000 = [
        CYAN+"¿Cual es el tipo de sangre mas común?"+BLACK,
        CYAN+"¿Cuantos paises hay en el mundo?"+BLACK,
        CYAN+"¿Cuantos elementos hay en la tabla periodica?"+BLACK,
            ]

    #Respuestas Lectura
    respuestasLectura100 = [
        ["1. Madera", "2.Algodón", "3.Pasto"],
        ["1. La madre", "2. La hija", "3. La maestra"],
        ["1. Chocomilk", "2. Zumo de zanahoria", "3. Zumo de naranja"]
            ]
    respuestasLectura250 = [
        ["1. Su café con tostadas", "2. Una cerveza", "3. Agua natural"],
        ["1. Negras", "2. Rojas", "3. Azules"],
        ["1. En la escuela", "2. En un parque", "3. En la casa de Laura"]
            ]
    respuestasLectura500 = [
        ["1. Gimnasia", "2. Matemáticas", "3. Español"],
        ["1. La rueda de carro", "2. La voltereta lateral", "3.El salto en paracaídas"],
        ["1. Cinco", "2. Seis", "3. Siete"]
            ]
    respuestasLectura1000 = [
        ["1. Literario", "2. Científico", "3. Histórico"],
        ["1. Se quita los zapatos", "2. Se quita el sueño", "3. Pierde la paciencia"],
        ["1. Un gato", "2. Un abrazo", "3. Un beso de buenos días"]
            ]

    #Respuestas Matematicas
    respuestasMate100 = [
        ["1. 45", "2. 65", "3. 32"],
        ["1. 3.5", "2. 6", "3. 9"],
        ["1. 43", "2. 19", "3. 27"]
            ]
    respuestasMate250 = [
        ["1. 50", "2. 40", "3. 23"],
        ["1. 111", "2. 127", "3. 144"],
        ["1. 128", "2. 49", "3. 64"]
            ]
    respuestasMate500 = [
        ["1. 225", "2. 183", "3. 442"],
        ["1. 89", "2. 133", "3. 77"],
        ["1. 32", "2. -10", "3. -12"]
            ]
    respuestasMate1000 = [
        ["1. 1117", "2. 1248", "3. -1288"],
        ["1. 3722", "2. 2310", "3. 1199"],
        ["1. 3781.112", "2. 382.755", "3. 906.125"]
            ]

    #Respuestas Ciencia
    respuestasCiencia100 = [
        ["1. Proceso químico que se produce en las plantas", "2. Arte de sacar fotos", "3. Un resumen de fotos"],
        ["1. Porque así lo quizo Dios", "2. Porque es una estrella a temperaturas muy altas", "3. Porque está muy lejos"],
        ["1.Porque la luna le da la energía necesaria", "2. Porque alguine prendió el sol", "3. Porque es una gigantesca masa de energía calorífica que produce luz"]
            ]
    respuestasCiencia250 = [
        ["1.Debido al Big Bang", "2. Las puso alguien ahí", "3. Salieron de la Tierra en cohetes"],
        ["1. Debido a las fuerzas de repulsión", "2. Si cae debido a la gravedad pero muy lento ", "3. Porque el sol la detiene"],
        ["1. Porque el agua que sube es azul", "2. Porque los mares son azules y se refleja", "3.  Porque al entra la luz del sol la luz azul tiene una longitud de onda más corta"]
            ]
    respuestasCiencia500 = [
        ["1. Fue un trabajo de mucha gente", "2. Mark Zuckerberg", "3. Elon Musk"],
        ["1. No", "2. Si", "3. Tal vez"],
        ["1. 300 a 500", "2. 100 a 200", "3. 700 a 900"]
            ]
    respuestasCiencia1000 = [
        ["1. O+", "2. AB+", "3. A-"],
        ["1. 206", "2. 195", "3. 102"],
        ["1. 200", "2. 124", "3. 118"]
            ]

    #Lectura
    if (numero % 3) == 1: #Verifica si la pregunta es de lectura
        print(lectura)
        if numero == 1:
            print(preguntasLectura100[preguntaElegida]) #Imprime la pregunta con sus respuestas
            print(respuestasLectura100[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida: #Verificar si la respuesta es correcta
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(100)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasLectura100[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 4:
            print(preguntasLectura250[preguntaElegida])
            print(respuestasLectura250[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(250)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasLectura250[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 7:
            print(preguntasLectura500[preguntaElegida])
            print(respuestasLectura500[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(500)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasLectura100[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 10:
            print(preguntasLectura1000[preguntaElegida])
            print(respuestasLectura1000[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(1000)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasLectura100[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
    #Matematicas
    elif (numero % 3) == 2:
        if numero == 2:
            print(preguntasMate100[preguntaElegida])
            print(respuestasMate100[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(100)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasMate100[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 5:
            print(preguntasMate250[preguntaElegida])
            print(respuestasMate250[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(250)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasMate250[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 8:
            print(preguntasMate500[preguntaElegida])
            print(respuestasMate500[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(500)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasMate500[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 11:
            print(preguntasMate1000[preguntaElegida])
            print(respuestasMate1000[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(1000)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasMate1000[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
    #Ciencias
    elif (numero % 3) == 0:
        if numero == 3:
            print(preguntasCiencia100[preguntaElegida])
            print(respuestasCiencia100[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(100)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasCiencia100[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 6:
            print(preguntasCiencia250[preguntaElegida])
            print(respuestasCiencia250[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(250)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasCiencia250[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 9:
            print(preguntasCiencia500[preguntaElegida])
            print(respuestasCiencia500[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(500)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasCiencia500[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)
        elif numero == 12:
            print(preguntasCiencia1000[preguntaElegida])
            print(respuestasCiencia1000[preguntaElegida])
            r = int(input("Respuesta: "))
            if r-1 == preguntaElegida:
                print(GREEN+"Elegiste la respuesta correcta!"+BLACK)
                input("Presione <ENTER> para continuar")
                return(1000)
            else:
                print(RED+"Respuesta incorrecta!"+BLACK)
                print("La respuesta correcta es:", respuestasCiencia1000[preguntaElegida][preguntaElegida])
                input("Presione <ENTER> para continuar")
                return(0)

archivo = open('BaseDeDatos_Juego.txt','a') #Crear archivo con resultados del juego
uno, dos = jugadores() #Guardar los nombres de los jugadores en dos variables
while numPreguntas > 0: #Repetir ciclo hasta llegar a los 12 preguntas
    if turno == 1:
        menuPrincipal()
        print("Es tu turno", uno)
        print(f"Tienes {puntos1} puntos")
        pregunta = int(input("Elige una pregunta: "))
        puntos = preguntas(pregunta)
        puntos1 += puntos
        numPreguntas -= 1
        turno = 2
    else:
        menuPrincipal()
        print("Es tu turno,", dos)
        print(f"Tienes {puntos2} puntos")
        pregunta = int(input("Elige una pregunta: "))
        puntos = preguntas(pregunta)
        puntos2 += puntos
        numPreguntas -= 1
        turno = 1

#Escribir los puntajes en un archivo aparte
archivo.write("Total de puntos del jugador 1: "+str(puntos1)+"\n")
archivo.write("Total de puntos del jugador 2: "+str(puntos2)+"\n")

#Verificar el ganador
if puntos1 > puntos2:
    print(BLUE+f"Felicidades {uno}, eres el ganador con {puntos1} puntos!")
    archivo.write("\nEl ganador fue el jugador 1!")
elif puntos1 < puntos2:
    print(BLUE+f"Felicidades {dos}, eres el ganador con {puntos2} puntos!")
    archivo.write("\nEl ganador fue el jugador 2!")
else:
    print(BLUE+f"Hubo un empate con {puntos1} puntos!")
    archivo.write("\nHubo un empate!")
    
#Cerrar el archivo
archivo.close()
