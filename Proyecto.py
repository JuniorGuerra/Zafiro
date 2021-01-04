import pyautogui
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def Intro():
    pass

def Audio():
    IA = "Puedes decir que quiere hacer: "
    #Codigo para decir el audio
    tts = gTTS(IA,lang="es-ES")
    #Codigo para guardar
    tts.save("Audio.mp3")
    Archivo = "Audio.mp3"
    #Reproducimos el archivo "Nombre".mp3
    playsound(Archivo)

def error():
    ArchivoError = "error.mp3"
    playsound(ArchivoError)

def error2():
    ArchivoError = "error2.mp3"
    playsound(ArchivoError)

def Inicio():
    Archivo = "Audio.mp3"
    playsound(Archivo)

def audioEscribir():
    Archivo = "Escribir.mp3"
    playsound(Archivo)

def audioRepetir():
    Archivo = "bajar.mp3"
    playsound(Archivo)

def audioRepetir2():
    Archivo = "subir.mp3"
    playsound(Archivo)

def audioRepetir3():
    Archivo = "izquierda.mp3"
    playsound(Archivo)

def audioRepetir4():
    Archivo = "derecha.mp3"
    playsound(Archivo)

def audioRepetir5():
    Archivo = "borrar.mp3"
    playsound(Archivo)

def ReconconerVoz(Texto):
    #definimos el reconocimiento
    r = sr.Recognizer()
    #source = Fuente
    with sr.Microphone() as Fuente:
        #Definimos como funcionara hablar:
        print("Hablar")
        hablar = r.listen(Fuente,timeout=1,phrase_time_limit=2)

        #Creamos un try except por si existe un error
        try:
            #Usamos la conexion de google porque es la mejor
            TextoHabla = r.recognize_google(hablar,key=None,language="es-ES")
            #imprimimos lo hablado
            print("has dicho: ",TextoHabla)
            Hacer(TextoHabla)

            #si se encuentra un error, marca error
        except:
            error()

def Hacer(Texto):
    #Traemos los valores de Reconocer voz
    print(Texto)

    #Comenzaremos a hacer el codigo para cada cosa que diga del pc, el programa lo valla haciendo
    #es basicamente dirigir que tiene que escribir, hacer, y ejecutar, usaremos mas codigo e implementaremos
    #miles de linea de codigo como muchos programas

    if Texto == "inicio".lower() or Texto == "abrir window".lower() or Texto == "abrir windows".lower():
        pyautogui.press("win")

    #Codigo para escribir en el programa
    if Texto == "escribir".lower():
        audioEscribir()
        LLamar()
    #codigo para presionar la segunda tecla
    if Texto == "enter".lower() or Texto == "presionar enter".lower():
        pyautogui.press("enter")
    #codigo para guardar
    if Texto == "guardar".lower() or Texto == "guardar programa".lower():
        pyautogui.hotkey("ctrl", "G")
    #codigo para cerrar
    if Texto == "cerrar".lower() or Texto == "cerrar programa".lower():
        pyautogui.hotkey("alt","f4")
    #codigo para bajar el con las flechitas de abajo, arriba, izauierda, derecha
    if Texto == "bajar".lower():
        audioRepetir()
        repetir("bajar")
    #codigo subir
    if Texto == "subir".lower() or Texto == "arriba".lower():
        audioRepetir2()
        repetir("subir")
    #codigo izquierda
    if Texto == "izquierda".lower():
        audioRepetir3()
        repetir("izquierda")
    #codigo derecha
    if Texto == "derecha".lower():
        audioRepetir4()
        repetir("derecha")
    #codigo espacio
    if Texto == "espacio".lower():
        pyautogui.press("space")
    #codigo para borrar
    if Texto == "Borrar".lower():
        audioRepetir5()
        repetir("borrar")
    #codigo para tabular
    if Texto == "tabular".lower():
        pyautogui.press("tab")

    if Texto == "abrir exclamación".lower() or Texto == "exclamación".lower():
        pyautogui.hotkey("shift","1")

    if Texto == "comillas".lower():
        pyautogui.hotkey("shift","2")

    if Texto == "numeral".lower():
        pyautogui.hotkey("shift", "3")

    if Texto == "signo peso".lower():
        pyautogui.hotkey("shift","4")

    if Texto == "porcentaje".lower():
        pyautogui.hotkey("shift","5")

    if Texto == "ampersand".lower():
        pyautogui.hotkey("shift","6")

    if Texto == "diagonal derecha".lower():
        pyautogui.hotkey("shift","7")

    if Texto == "abrir paréntesis".lower():
        pyautogui.hotkey("shift","8")

    if Texto == "cerrar paréntesis".lower():
        pyautogui.hotkey("shift","9")

    if Texto == "igual".lower():
        pyautogui.hotkey("shift","0")

    if Texto == "pregunta".lower():
        pyautogui.press("¿")
#error en este por el momento
    if Texto == "diagonal izquierda".lower():
        pyautogui.hotkey("Alt Graph","'")

    if Texto == "2 puntos".lower() or Texto == "dos puntos".lower():
        pyautogui.hotkey("shift",".")

    if Texto == "comilla simple".lower() or Texto == "comillas simples".lower():
        pyautogui.press("'")

    if Texto == "punto y coma".lower():
        pyautogui.hotkey("shift",",")

    if Texto == "coma".lower():
        pyautogui.press(",")

    if Texto == "punto".lower():
        pyautogui.press(".")

    if Texto == "interrogracion".lower():
        pyautogui.hotkey("shift", "'")

    if Texto == "cerrar exclamacion".lower():
        pyautogui.hotkey("shift", "¿")

    if Texto == "más".lower() or Texto == "+":
        pyautogui.press("+")

    if Texto == "por".lower() or Texto == "*":
        pyautogui.hotkey("shift","+")

#error grabe a partir de esta linea de codigo // sale [] en ves de {}
    if Texto == "corchete".lower():
        pyautogui.press("{")

    if Texto == "cerrar corchete".lower():
        pyautogui.press("}")

    if Texto == "documentos".lower():
        pyautogui.hotkey("win","e")

    if Texto == "esperar".lower():
        time.sleep(10)



def escribir(Escribir):
    #Escribimos el valor de Escribir
    pyautogui.write(Escribir)

    #Codigo para codicionar tecla de control subir, bajar, izquierda, derecha
def bajar(texto,veces):
#codigo bajar
    if texto == "bajar":
        a = int(veces)
        for x in range(veces):
            pyautogui.press("down")
#codigo subir
    if texto == "subir":
        a = int(veces)
        for x in range(veces):
            pyautogui.press("up")
#codigo izquierda
    if texto == "izquierda":
        a = int(veces)
        for x in range(veces):
            pyautogui.press("left")
#codigo derecha
    if texto == "derecha":
        a = int(veces)
        for x in range(veces):
            pyautogui.press("right")

    if texto == "borrar":
        a = int(veces)
        for a in range(veces):
            pyautogui.press("backspace")


def repetir(rtexto):
    #definimos el reconocimiento
    r = sr.Recognizer()
    #source = Fuente
    with sr.Microphone() as Fuente:
        #Definimos como funcionara hablar:
        print("Hablar")
        hablar = r.listen(Fuente,timeout=1,phrase_time_limit=2)

        #Creamos un try except por si existe un error
        try:
            #Usamos la conexion de google porque es la mejor
            TextoHabla = r.recognize_google(hablar,key=None,language="es-ES")
            #imprimimos lo hablado
            print("has dicho: ",TextoHabla)
            # LLamamos a escribir
            a = int(TextoHabla)
            bajar(rtexto,a)

            #si se encuentra un error, marca error
        except:
            error2()

def LLamar():
    #definimos el reconocimiento
    r = sr.Recognizer()
    #source = Fuente
    with sr.Microphone() as Fuente:
        #Definimos como funcionara hablar:
        print("Hablar")
        hablar = r.listen(Fuente,timeout=4,phrase_time_limit=8)

        #Creamos un try except por si existe un error
        try:
            #Usamos la conexion de google porque es la mejor
            TextoHabla = r.recognize_google(hablar,key=None,language="es-ES")
            #imprimimos lo hablado
            print("has dicho: ",TextoHabla)
            # LLamamos a escribir
            escribir(TextoHabla)

            #si se encuentra un error, marca error
        except:
            error2()

while True:
    try:
        #llamamos a inicio que es el mensaje principal del IA
        Inicio()
        #Reconocemos lo que dice
        ReconconerVoz("")
        #Por ahora llamamos el dato desde la otra funcion
        Hacer("")
    except:
        print("No te he escuchado bien :/")

#"""Error prioritaro, no manda los valores del return, gracias""" -->Primer error cumplido,arreiglado :)<--

#Ideas para cumplir los siguientes objetivos:
"""1- leer tamaño de audio ejemplo:
      abrir whasat y enviar un mensaje a ('Pello')
      esta accion sera analizada por los espacios y la primera palabra"""

#Objetivos a cumplir con el codigo
"""1- combinacion de letras propias
   2- reconocer imagenes
   3- presionar letras propias
   4- abrir programa abierto
   5- accion de esperar
   6- comparar texto de imagenes
   7- leer lo que esta en la pantalla
   8- accion de retomar"""

#Objetivos avanzados:
"""1- capaz de enviar un mensaje
   2- capaz de poner alarma
   3- capaz de reiniciar el pc
   4- capaz de abrir navegador"""