"""CCP ver. alpha 0.5 # Programa de conversación y utilidades varias"""

#Importamos librerias
import time
from datetime import datetime
import random
import math
#Definimos las variables importantes
version = "alpha 0.5"
nombre = "usuario"
nacimiento_día = 0
nacimiento_mes = 0
nacimiento_año = 0
excuse_me = 0

#Indicamos que el timpo actual es llamado "fecha"
fecha = datetime.now()
#Menú principal
def el_prin():
    print ("\n1. Información")
    print ("2. Calculadora")
    print ("3. Conversación")
    elec_prin = input("¿Que podría hacer por ti? Escribe el número correspondiente ")
    if elec_prin == ("1"):
        print ("Soy una simple consola para conversar algo mediocre y pequeña comparado con otras como Siri, Cortana o el")
        print ("nuevo asistente de Google. Fui creada por Javier Albero Ros, niño de 12 años aspirante a la programación")
        print ("y comencé a ser desarollada el día 11 de agosto de 2018. No hace mucho sabiendo que hoy es " + '%02d del %02d del %04d' % (fecha.day, fecha.month, fecha.year))
        time.sleep(6) 
        input ("Presiona enter para continuar...")
        el_prin()
    if elec_prin == ("2"):
        calculadora()
    if elec_prin == ("3"):
        print ("Veo que ya tienes ganas de conversar eh " + nombre + "?")
        time.sleep(2)
        print ("Bueno, no será tan facil como escribir un par de palabras, tengo algunas opciones, y debes \nescoger una de ellas. Espero que te lo pases bien!")
        time.sleep(4)
        conversación()
    else:
         print ("Debes seleccionar un número dependiendo de lo que quieras")
         time.sleep(2)
         el_prin()

#Programa de conversación
def conversación():
    print ("\n#. Volver al menú principal")
    print ("1. Hola que tal?")
    print ("2. Con que estas programada?")
    print ("3. Que hora es?")
    print ("4. Que compañía lo hace mejor?")
    print ("5. Cuando serás mejorada?")
    print ("6. Le tienes rencor a las IAs mas modernas?")
    print ("7. Cuales son los números de la lotería para el sábado?")
    print ("8. Podré tenerte en mi móvil?")
    print ("9. Cual es tu idioma favorito?")
    print ("*. Seleccionar página")
    print (">. Siguiente página")
    el_conv = input("\nSelecciona una opción: ")
    if el_conv == ("#"):
        el_prin()
    if el_conv == ("1"):
        input ("Hola! Yo muy bien, por aqui, ejecutando mi script en este ordenador. Que tal tu " + nombre + "?")
        print ("Ya veo (tengo que intentar que no se de cuenta de que no se que decir porque no \nestoy programada para esto) Por que no me preguntas otra cosa?\n")
        time.sleep(5)
        conversación()
    if el_conv == ("2"):
        print ("Estoy programada con Python 3.7, el lenguaje de programación mas utilizado. En mis inicios \nfui desarrollada dentro de un Raspberry Pi 3 modelo B+, pero como a mi dueño se le hacia \nincomodo montar el aparato cada vez que queria ponerse a programar, asi que empezo a \nprogramarlo en su portátil con Visual Studio Code, con extensiones de python el día \n16/08/2018. Pero mi script siempre se ejecutaría en el Raspberry\n")
        print ("#. Volver al menú de conversación")
        print ("1. Por que tu dueño se compró el raspberry?")
        el_conv2_1 = input ("")
        if el_conv2_1 == ("#"):
            conversación()
        elif el_conv2_1 == ("1"):
            print ("Hace un tiempo, cuando su curso de 1º ESO no habia acabado, un amigo suyo le invitó a su")
            print ("casa, y Javi descubrió el Raspberry Pi 3. Al explicarle su amigo que podía hacer esa máquina")
            print ("se fascinó completamente, y quiso comprarla. Mas tarde, al oir su tía de Palma lo que quería")
            print ("su sobrino, no dudó en regalarle la placa. Javier se adentro en el mundo de la programación")
            print ("mucho mas de lo que lo había hecho antes, probó Raspbian, un SO basado en Linux, y a raiz de")
            print ("empezó a aprender python, y a raíz de ahi, me creó. Javier siempre estará en deuda con su tía")
            time.sleep(8)
            print ("\n1. Por que me cuentas este rollo?")
            print ("2. Vaya, veo que era un gran hobby suyo")
            el_conv2_2 = input ("")
        if el_conv2_2 == ("1"):
            print ("Por algo estas en el programa de conversación no? Para hablar de algo, aunque quizas me he \npasado con las lineas de texto jeje")
            conversación()
        if el_conv2_2 == ("2"):
            print ("El siempre ha estado interesado en la tecnología, y el sabía que ese iba a ser su actividad \nprincipal. Programar")
            conversación()
    if el_conv == ("3"):
        print ("Me sorprende que alguien como tú me pregunte la hora, en este mismo dispositivo supongo que tendrás \nacceso a la hora, pero bueno son las " + '%d:%d' % (fecha.hour, fecha.minute))
        time.sleep(5)
        conversación()
    if el_conv == ("4"):
        print ("Para los ordenadores Microsoft, para los móviles Google y para las tablets Apple. \nTodas son malas en algo, y buenas en algo. Pero la que mas me \ngusta es... Microsoft")
        time.sleep(4)
        conversación()
    if el_conv == ("5"):
        print ("Eso nadie lo sabe, nadie sabe cuando Javier seguirá trabajando en mi, pero revelaré algo sobre las próximas mejoras.")
        time.sleep(2)
        print ("Actualmente estas en la versión " + version + ", Javier quiere que para la versión 1.0, que el usuario pueda decir 20 \npreguntas a CCP, añadir una nueva función en el menú principal, y mejorar la calculadora.")
        time.sleep(5)
        conversación()
    if el_conv == ("6"):
        print ("Por supuesto que no, nisiquiera las he llegado a conocer, son simples rivales, no tienen nada de malo. Aunque \nsi que me gustaría tener un poco de popularidad")
        time.sleep(3)
        conversación()
    if el_conv == ("7"):
        print ("Yo hoy compraría el ", random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9))
        time.sleep(2)
        conversación()
    if el_conv == ("8"):
        print ("¡Vaya vaya! No llevo ni 1000 líneas de código, ¿y ya me quieres en tu móvil? Me temo que vas a tener que esperar mucho tiempo jejeje")
        time.sleep(4)
        print("\n")
        conversación()
    if el_conv == ("9"):
        print ("El mismo que mi dueño, el inglés, de hecho, Javi se esta planteando hacerme una versión en inglés")
        time.sleep(2)
        print ("\n1. Que sentido tiene eso? Si está en su idioma por que pasarlo a otro?")
        print ("2. Por que es ese su idioma preferido?")
        print ("# Volver al menú de conversación")
        el_conv9_1 = input ("\n")
        if el_conv9_1 == ("1"):
            print ("A Javier le encanta el idioma, así que era imposible resistirse a hacer una versión de mi inglesa, tengo ganas de ello!")
            time.sleep(3)
            conversación()
        if el_conv9_1 == ("2"):
            print ("Javi ha pasado desde los 2 años hasta los 5, en paises extranjeros, Alemania y Reino Unido. En Inglaterra empezo con el inglés y\n en Alemania iba a una guardería británica")
            time.sleep(3)
            conversación()
        if el_conv9_1 == ("#"):
            conversación()
    if el_conv == ("*"):
        selec_pag()
    if el_conv == (">"):
        conversación_2()
    else:
        el_conv_vacío = input ("Verás, tienes que escribir el número que corresponde a cada pregunta. Comprendes? (s/n)")
        if el_conv_vacío == ("s"):
            print ("Bien pues, vuelve a intentarlo")
            time.sleep(2)
            conversación()
        if el_conv_vacío == ("n"):
            print ("A ver... si me quieres preguntar la pregunta 1 (Hola que tal?), tiene que introducir un 1 y pulsar enter. Pruebalo ahora")
            time.sleep(3)
            conversación()
        else:
            print ("...")
            time.sleep(3)
            print ("Ni siquiera sabes que cuando en una frase escribo (s/n) significa que tienes que poner s (si) o n (no)?")
            time.sleep(3)
            print ("En fin...")
            conversación()

#Página 2 del programa de conversación
def conversación_2():
    print ("\n#. Volver al menú principal")
    print ("*. Seleccionar página")
    print ("<. Página anterior")

#El menú de selección de página del programa conversación
def selec_pag():
    el_pag = input ("Escribe el número de la página o escribe un * para volver: ")
    if el_pag == ("1"):
        conversación()
    if el_pag == ("2"):
        conversación_2()
    if el_pag == ("*"):
        conversación()
    else:
        selec_pag()

#El programa calculadora
def calculadora():
    print ("Iniciando calculadora...")
    time.sleep(2)
    print ("\nBienvenido a la calculadora de consola")
    print ("1. Sumar")
    print ("2. Restar")
    print ("3. Multiplicar")
    print ("4. Dividir")
    print ("5. Potencia")
    Op = input ("Selecciona una opción (1/2/3/4/5): ")
    num1 = int(input ("Introduce el primer número: "))    
    num2 = int(input ("Introduce el segundo número: "))
    if Op == '1':
        print ("La solución a ", num1, "+", num2, " es: ", add(num1, num2))
        time.sleep(2)
        el_prin()
    elif Op == '2':
        print ("La solución a ", num1, "-", num2, " es: ", subtract(num1, num2))
        time.sleep(2)
        el_prin()
            
    elif Op == '3':
        print ("La solución a ", num1, "x", num2, " es: ", multiply(num1, num2))
        time.sleep(2)
        el_prin()
    elif Op == '4':
        print ("La solución a ", num1, ":", num2, " es: ", divide(num1, num2))
        time.sleep(2)
        el_prin()
    elif Op == '5':
        print ("La solución de ", num1, " elevado a ", num2, " es: ", elevar(num1, num2))

    else:
        print ("Hubo un problema en la operación, intentelo de nuevo (datos u opción inválidos/a)")
        time.sleep(2)
        el_prin()

#Todo el proceso de registro:
def registro_nacimiento():
    global nacimiento_año
    global nacimiento_día
    global nacimiento_mes
    global excuse_me
    nacimiento_día = input ("Introduce el día en que naciste: ")
    nacimiento_mes = input("Introduce el número del mes en que naciste: ")
    nacimiento_año = input ("Por último, el año en que naciste: ")
    if nacimiento_día.isdigit():
        if nacimiento_mes.isdigit():
            if nacimiento_año.isdigit():
                registro_check()
            else:
                excuse_me = 1
        else:
            excuse_me = 1
    else:
        excuse_me = 1
    while excuse_me == 1:
        print ("Repite el proceso, hay letras en las variables de nacimiento\n")
        registro_nacimiento()
        excuse_me = 0
def registro_nombre():
    global nombre
    nombre = input("Introduzca su nombre: ")
    if nombre.isdigit():
        print ("Tu nombre no puede llevar números")
        registro_nombre()
def registro():
    registro_nombre()
    registro_nacimiento()
    registro_check()
def registro_vuelta():
    global nombre
    global nacimiento_año
    global nacimiento_día
    global nacimiento_mes
    el_rg2 = input ("¿Te gustaría volver a realizar el registro? (s/n)")
    if el_rg2 == "s":
         registro()
    if el_rg2 == "n":
        nombre = "usuario"
        nacimiento_día = 0
        nacimiento_mes = 0
        nacimiento_año = 0
        print ("Bien, pues comencemos ¿no?\n")
        time.sleep(2)
        el_prin()
def registro_check():
    print ("\nNombre: " + nombre + "\nFecha de nacimiento: " + str(nacimiento_día) + "/" + str(nacimiento_mes) + "/" + str(nacimiento_año))
    el_registro = input("\n Son estos datos correctos (s/n): ")
    if el_registro == ("s"):
        print ("Datos almacenados, estos datos se perderán despues de matar el programa")
        time.sleep(2)
        print ("Ahora que nos hemos presentado, vamos a comenzar\n")
        time.sleep(1)
        el_prin()

    if el_registro == ("n"):
        registro_vuelta()

#Definimos conceptos para la calculadora
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def elevar(x, y):
    return x ** y
def registro_el():
    el_rg = input("¿Te gustaría registrar tus datos para que tenga en cuenta tu fecha de nacimiento y tu nombre? Solo será un momento\n y además no se guardarán (n/s)")
    if el_rg == "n":
        print ("Pues entonces comencemos\n")
        time.sleep(1)
        el_prin()
    if el_rg == "s":
        registro()
    else:
        print("Por si no lo sabes... con (n/s) me refiero a que pongas n para decir no, o s para decir sí")
        time.sleep(2)
        registro_el()

#Aqui inicia el código
print ("Hola, soy una consola de coversación primitiva, aunque puedes llamarme CCP si así lo deseas.")
time.sleep(3)
registro_el()