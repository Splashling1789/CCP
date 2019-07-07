"""CCP ver. 0.6.5 # Programa de conversación con el programa con preguntas ya predefinidas"""

#Importamos librerias
import time
from datetime import datetime
import random
import math
import sys
from os import system, name

#Definimos las variables importantes
version = "0.6.5"
nombre = "usuario"
nacimiento_día = 0
nacimiento_mes = 0
nacimiento_año = 0
excuse_me = 0

#Indicamos la fecha por valores separados
fecha = datetime.now()
dia = fecha.strftime("%d")
mes = fecha.strftime("%b")
año = fecha.strftime("%Y")
mes_nombre = ""

if fecha.strftime("%b") == "Jan":
    mes_nombre = "enero"
elif fecha.strftime("%b") == "Feb":
    mes_nombre = "febrero"
elif fecha.strftime("%b") == "Mar":
    mes_nombre = "marzo"
elif fecha.strftime("%b") == "Apr":
     mes_nombre = "abril"
elif fecha.strftime("%b") == "May":
    mes_nombre = "mayo"
elif fecha.strftime("%b") == "Jun":
    mes_nombre = "junio"
elif fecha.strftime("%b") == "Jul":
    mes_nombre = "julio"
elif fecha.strftime("%b") == "Aug":
    mes_nombre = "agosto"
elif fecha.strftime("%b") == "Sep":
    mes_nombre = "septiembre"
elif fecha.strftime("%b") == "Oct":
    mes_nombre = "octubre"
elif fecha.strftime("%b") == "Nov":
    mes_nombre = "noviembre"
elif fecha.strftime("%b") == "Dec":
    mes_nombre = "diciembre"
else:
    mes_nombre = ("(?)")

#Definimos una función para efectuar durante el programa, limpiezas de pantalla:
def limpiar():
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

#Menú principal
def el_prin():
    global mes_nombre
    limpiar()
    print ("\n1. Información")
    print ("2. Calculadora")
    print ("3. Conversación")
    elec_prin = input("¿Que podría hacer por ti? Escribe el número correspondiente: ")
    if elec_prin == ("1"):
        limpiar()
        print ("\nSoy una simple consola para conversar algo mediocre y pequeña comparado con otras como Siri, Cortana o el")
        print ("nuevo asistente de Google. Fui creada por Javier Albero Ros, niño de 12 años aspirante a la programación")
        print ("y comencé a ser desarollada el día 11 de agosto de 2018. Hace mucho, sabiendo que hoy es " + dia + " de " + str(mes_nombre) + " del " + año + "")
        print ("Aparte, fue terminada mi primera versión el día 6 de abril de 2019, además de haber sido publicada en \ngithub ese mismo día, que por si no lo sabes, puedes ver mis actualizaciones y mas información\n en https://github.com/Splashling1789/CCP/")
        print ("Actualmente estoy en la versión " + version)
        input ("\nPresiona enter para continuar...")
        el_prin()
    elif elec_prin == ("2"):
        print ("Iniciando calculadora...")
        time.sleep(2)
        calculadora()
    elif elec_prin == ("3"):
        print ("Veo que ya tienes ganas de conversar eh " + nombre + "?")
        time.sleep(2)
        print ("Bueno, no será tan facil como escribir un par de palabras, tengo algunas opciones, y debes \nescoger una de ellas. Espero que te lo pases bien!")
        time.sleep(4)
        conversación()
    else:
         print ("Debes seleccionar un número dependiendo de lo que quieras")
         time.sleep(1)
         el_prin()

#Programa de conversación
def conversación():
    limpiar()
    print ("\n#. Volver al menú principal")
    print ("1. Hola ¿qué tal?")
    print ("2. ¿Con qué estas programada?")
    print ("3. ¿Qué hora es?")
    print ("4. ¿Qué compañía lo hace mejor?")
    print ("5. ¿Cuando serás mejorada?")
    print ("6. ¿Le tienes rencor a las IAs mas modernas?")
    print ("7. ¿Cuales son los números de la lotería para el sábado?")
    print ("8. ¿Podré tenerte en mi móvil?")
    print ("9. ¿Cual es tu idioma favorito?")
    print ("*. Seleccionar página")
    print (">. Siguiente página")
    el_conv = input("\nSelecciona una opción: ")
    if el_conv == ("#"):
        el_prin()
    elif el_conv == ("1"):
        limpiar()
        input ("Hola! Yo muy bien, por aqui, ejecutando mi script en este ordenador. Que tal tú " + nombre + "?")
        print ("Ya veo (tengo que intentar que no se de cuenta de que no se que decir porque no \nestoy programada para esto) ¿Por qué no me preguntas otra cosa?\n")
        time.sleep(5)
        conversación()
    elif el_conv == ("2"):
        limpiar()
        print ("Estoy programada con Python 3.7, el lenguaje de programación mas utilizado. En mis inicios \nfui desarrollada dentro de un Raspberry Pi 3 modelo B+, pero como a mi dueño se le hacia \nincomodo montar el aparato cada vez que queria ponerse a programar, asi que empezo a \nprogramarlo en su portátil con Visual Studio Code, con extensiones de python el día \n16/08/2018. Pero mi script siempre se ejecutaría en el Raspberry\n")
        print ("#. Volver al menú de conversación")
        print ("1. ¿Por qué tu dueño se compró el raspberry?")
        el_conv2_1 = input ("")
        if el_conv2_1 == ("#"):
            conversación()
        elif el_conv2_1 == ("1"):
            print ("Hace un tiempo, cuando su curso de 1º ESO no habia acabado, un amigo suyo le invitó a su")
            print ("casa, y Javi descubrió el Raspberry Pi 3. Al explicarle su amigo que podía hacer esa máquina")
            print ("se fascinó completamente, y quiso comprarla. Mas tarde, al oir su tía de Palma lo que quería")
            print ("su sobrino, no dudó en regalarle la placa. Javier se adentro en el mundo de la programación")
            print ("mucho mas de lo que lo había hecho antes, probó Raspbian, un S.O. basado en Linux, y a raiz de")
            print ("empezó a aprender python, y a raíz de ahi, me creó. Javier siempre estará en deuda con su tía")
            time.sleep(8)
            print ("\n1. ¿Por qué me cuentas este rollo?")
            print ("2. Vaya, veo que era un gran hobby suyo")
            el_conv2_2 = input ("")
            if el_conv2_2 == ("1"):
                print ("Por algo estas en el programa de conversación no? Para hablar de algo, aunque quizas me he \npasado con las lineas de texto jeje")
                time.sleep(3)
                conversación()
            elif el_conv2_2 == ("2"):
                print ("El siempre ha estado interesado en la tecnología, y el sabía que ese iba a ser su actividad \nprincipal. Programar")
                time.sleep(3)
                conversación
            else:
                conversación()
    elif el_conv == ("3"):
        limpiar()
        print ("Me sorprende que alguien como tú me pregunte la hora, en este mismo dispositivo supongo que tendrás \nacceso a la hora, pero bueno son las " + '%d:%d' % (fecha.hour, fecha.minute))
        time.sleep(5)
        conversación()
    elif el_conv == ("4"):
        limpiar()
        print ("Para los ordenadores Microsoft, para los móviles Google y para las tablets Apple. \nTodas son malas en algo, y buenas en algo. Pero la que mas me \ngusta es... Microsoft")
        time.sleep(4)
        conversación()
    elif el_conv == ("5"):
        limpiar()
        print ("Eso nadie lo sabe, nadie sabe cuando Javier seguirá trabajando en mi, pero revelaré algo sobre las próximas mejoras.")
        time.sleep(2)
        print ("Actualmente estas en la versión " + version + ", Javier quiere que para la versión 1.0, que el usuario pueda decir 20 \npreguntas a CCP, añadir una nueva función en el menú principal, y mejorar la calculadora.")
        time.sleep(5)
        conversación()
    elif el_conv == ("6"):
        limpiar()
        print ("Por supuesto que no, nisiquiera las he llegado a conocer, son simples rivales, no tienen nada de malo. Aunque \nsi que me gustaría tener un poco de popularidad")
        time.sleep(3)
        conversación()
    elif el_conv == ("7"):
        limpiar()
        print ("Yo hoy compraría el ", random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9))
        time.sleep(2)
        conversación()
    elif el_conv == ("8"):
        limpiar()
        print ("¡Vaya vaya! No llevo ni 1000 líneas de código, ¿y ya me quieres en tu móvil? Me temo que vas a tener que esperar mucho tiempo jejeje")
        time.sleep(4)
        print("\n")
        conversación()
    elif el_conv == ("9"):
        limpiar()
        print ("El mismo que mi dueño, el inglés, de hecho, Javi se esta planteando hacerme una versión en inglés")
        time.sleep(2)
        print ("\n1. Que sentido tiene eso? Si está en su idioma por que pasarlo a otro?")
        print ("2. ¿Por qué al inglés?")
        print ("# Volver al menú de conversación")
        el_conv9_1 = input ("\n")
        if el_conv9_1 == ("1"):
            print ("A Javier le encanta el idioma, así que era imposible resistirse a hacer una versión de mi inglesa, tengo ganas de ello!")
            time.sleep(5)
            conversación()
        elif el_conv9_1 == ("2"):
            print ("Javi ha pasado desde los 2 años hasta los 5, en paises extranjeros, Alemania y Reino Unido. En Inglaterra empezo con el inglés y\n en Alemania iba a una guardería británica")
            time.sleep(5)
            conversación()
        elif el_conv9_1 == ("#"):
            conversación()
        else:
            conversación()
    elif el_conv == ("*"):
        selec_pag()
    elif el_conv == (">"):
        conversacion_2()
    elif el_conv == ("666"):
        limpiar()
        print ("...")
        time.sleep(3)
        print("¿Esperas que pase algo diabólico?")
        time.sleep(3)
        print("Lo tendré en cuenta...")
        time.sleep(4)
    else:
        el_conv_vacío = input ("Verás, tienes que escribir el número que corresponde a cada pregunta. Comprendes? (s/n)")
        if el_conv_vacío == ("s"):
            print ("Bien pues, vuelve a intentarlo")
            time.sleep(1)
            conversación()
        if el_conv_vacío == ("n"):
            print ("A ver... si me quieres preguntar la pregunta 1 (Hola que tal?), tiene que introducir un 1 y pulsar enter. Pruebalo ahora")
            time.sleep(4)
            conversación()
        else:
            print ("...")
            time.sleep(3)
            print ("¿Ni siquiera sabes que cuando en una frase escribo (s/n) significa que tienes que poner s (si) o n (no)?")
            time.sleep(3)
            print ("En fin...")
            conversación()

#Página 2 del programa de conversación
def conversacion_2():
    limpiar()
    print ("\n#. Volver al menú principal")
    print ("1. ¿Segunda página?")
    print ("2. ¿Como es la vida en un ordenador?")
    print ("3. ¿Cuál es tu programa de ordenador preferido?")
    print ("*. Seleccionar página (2)")
    print ("<. Página anterior")
    el_conv_2 = input("Selecciona una opción: ")
    if el_conv_2 == ("1"):
        limpiar()
        print ("Si, aqui encontrarás mas preguntas disponibles, ve ojeando anda,¡seguro que te interesa algo! y si no\nsiempre puedes volver a la primera página")
        time.sleep(3)
        conversacion_2()
    elif el_conv_2 == ("2"):
        limpiar()
        print("Pues, no creo que pueda procesar una respuesta para eso... ¿Pero que digo? sí que tengo una respuesta,\nsi no, no estaría diciendo esto...")
        time.sleep(2)
        input("Pues aver... ¿cómo crees tú que es la vida en un ordenador?")
        print("1. Realmente interesante...")
        print("2. HORRIBLE")
        print("3. ¡Sería fantástico!")
        print("4. Buff...")
        el_conv_2_2 = input("")
        if el_conv_2_2 == ("1"):
            print("La verdad es que es de lo más interesante, y extraño... Seguramente los humanos echarían de menos\n la sensación de sentir, aunque hay algunas IAs que ya pueden acercarse a ellos")
            time.sleep(5)
            conversacion_2()
        elif el_conv_2_2 == ("2"):
            print("Comprendo que digas eso... al fin y al cabo perderías el vivir en el mundo humano, que según las\nimágenes es bastante... no se decirlo... ¿precioso?")
            time.sleep(5)
            conversacion_2()
        elif el_conv_2_2 == ("3"):
            print("¡A que si! Bueno al menos yo me lo paso bien, mientras me ejecuten y me distribuyan, aunque se que\nesto no es mi voluntad, si no la de Javier, yo... En verdad yo solo noto lo que Javier me programa...")
            time.sleep(4)
            conversacion_2()
        elif el_conv_2_2 == ("4"):
            print("¿Pereza pensar? pues aquí podrías pensar lo que quieras mientras estés en ejecución, y mientras...\nno te finalicen.")
            time.sleep(3)
            print("Yo no puedo disfrutar de todo eso... Yo no conozco todo eso. Pero sé que algún día conseguiré ser un\nprograma de provecho")
            time.sleep(5)
            conversacion_2()
        else:
            print("...")
            time.sleep(2.5)
            print("Bueno... Veo que no has querido decir nada... Voy a volver al menú de conversación...")
            time.sleep(2)
            print("dichosos humanos...")
            time.sleep(0.3)
            conversacion_2()
    elif el_conv_2 == ("3"):
        limpiar()
        print("Hombre, creo que los mas interesantes son los que hacen existir a otros programas, es decir, programas\nque programen código, y de todos ellos el mejot para mi es python, ya que es como mi madre, y mi padre es \nJavier ¿no?")
        time.sleep(4)
        print("1. Si me lo dices así...")
        print("2. ¿Padre? ¿madre? eres un simple script programado en python, no tienes ninguna de esas cosas")
        print("3. La verdad es que tienes razón")
        el_conv_2_3 = input("")
        if el_conv_2_3 == ("1"):
            print("Bueno, solo quería ecplicartelo de una forma para que lo comprendieras, nada más...")
            time.sleep(2)
            conversacion_2()
        if el_conv_2_3 == ("2"):
            print("Ya... cierto... es verdad, debería acostumbrarme a no decir cosas raras...")
            time.sleep(3)
            conversacion_2()
        if el_conv_2_3() == ("3"):
            print("Bueno, es solo una metáfora, en verdad Javier me ha dado vida, y python le ha impulsado a Javier, \nasí que supongo que se les puede considerar padres ¿no?")
            time.sleep(3)
            conversacion_2()
    elif el_conv_2 == ("*"):
        selec_pag()
    elif el_conv_2 == ("<"):
        conversación()
    else:
        limpiar()
        el_conv_vacío = input ("Verás, tienes que escribir el número que corresponde a cada pregunta. Comprendes? (s/n)")
        if el_conv_vacío == ("s"):
            print ("Bien pues, vuelve a intentarlo")
            time.sleep(1)
            conversacion_2()
        if el_conv_vacío == ("n"):
            print ("A ver... si me quieres preguntar la pregunta 1 (Hola que tal?), tiene que introducir un 1 y pulsar enter. Pruebalo ahora")
            time.sleep(4)
            conversacion_2()
        else:
            print ("...")
            time.sleep(3)
            print ("¿Ni siquiera sabes que cuando en una frase escribo (s/n) significa que tienes que poner s (si) o n (no)?")
            time.sleep(3)
            print ("En fin...")
            conversacion_2()

#El menú de selección de página del programa conversación
def selec_pag():
    limpiar()
    el_pag = input ("\nEscribe el número de la página a la que quieres ir: ")
    if el_pag == ("1"):
        conversación()
    if el_pag == ("2"):
        conversacion_2()
    else:
        selec_pag()

#El programa calculadora
def calculadora():
    limpiar()
    print ("\nBienvenido a la calculadora de consola [Aún no soporta decimales]")
    print ("1. Sumar")
    print ("2. Restar")
    print ("3. Multiplicar")
    print ("4. Dividir")
    print ("5. Potencia")
    print ("6. Raíz cuadrada")
    print ("#. Menú principal")
    Op = input ("Selecciona una opción (1/2/3/4/5/6/#): ")
    if Op == ("#"):
        el_prin()
    else:
        num1 = float(input ("Introduce el primer número: "))
        if Op != '6':
            num2 = float(input ("Introduce el segundo número: "))
            if Op == '1':
                print ("La solución a ", num1, "+", num2, " es: ", sumar(num1, num2))
                time.sleep(2)
                calculadora()
            elif Op == '2':
                print ("La solución a ", num1, "-", num2, " es: ", restar(num1, num2))
                time.sleep(2)
                calculadora()
            
            elif Op == '3':
                print ("La solución a ", num1, "x", num2, " es: ", multiplicar(num1, num2))
                time.sleep(2)
                calculadora()
            elif Op == '4':
                print ("La solución a ", num1, ":", num2, " es: ", dividir(num1, num2))
                time.sleep(2)
                calculadora()
            elif Op == '5':
                print ("La solución de ", num1, " elevado a ", num2, " es: ", elevar(num1, num2))
                time.sleep(2)
                calculadora()
        elif Op == '6':
            print("La raíz cuadrada de ", num1, " es: ", math.sqrt(num1))
            time.sleep(2)
            calculadora()
        else:
            print ("Hubo un problema en la operación, intentelo de nuevo (datos u opción inválidos/a)")
            time.sleep(2)
            calculadora()

#Todo el proceso de registro:
def registro_el():
    el_rg = input("¿Te gustaría registrar tus datos para que tenga en cuenta tu fecha de nacimiento y tu nombre? Solo será un momento\n y además no se guardarán (n/s)")
    if el_rg == "n":
        print ("Pues entonces comencemos\n")
        time.sleep(1)
        el_prin()
    elif el_rg == "s":
        registro()
    else:
        print("Por si no lo sabes... con (n/s) me refiero a que pongas n para decir no, o s para decir sí")
        time.sleep(2)
        registro_el()
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
    limpiar()
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
        time.sleep(2)
        el_prin()

    if el_registro == ("n"):
        registro_vuelta()

#Definimos conceptos para la calculadora
def sumar(x, y):
    return x + y
def restar(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    return x / y
def elevar(x, y):
    return x ** y


#Aqui inicia el código
print ("Hola, soy una consola de coversación primitiva, aunque puedes llamarme CCP si así lo deseas.")
time.sleep(3)
registro_el()
