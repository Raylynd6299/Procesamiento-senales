from easygui import *
import sys
import matplotlib.pyplot as plt
import numpy as np
import  pyaudio  
import  wave
from scipy.io import wavfile

#Definimos paramentros
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
duracion=5
archivo = "grabacion.wav"

def Senal_cast(Senal):
    SenalF = Senal.split(",")
    Final = []
    for elemento in SenalF:
        Final.append(float(eval(elemento)))
    return Final
def Amplificacion(Senal,amp):
    Amplificacion = []
    for elem  in Senal:
        Amplificacion.append(elem * amp)
    return Amplificacion
def Reflejar(Senal,Centro):
    Senal.reverse()
    Centro = len (Senal)-Centro+1
    return Senal,Centro
def Desplazamientos(Senal,Centro,DesP):
    if DesP >=0:# cento a la derecha
        Centro = Centro + DesP
        while Centro > len(Senal):
            Senal.append(0)    
        
    else:# centro a la izquierda
        Centro = Centro +  DesP
        if (Centro<0):
            for i in range(0,abs(Centro)+1):
                Senal.insert(0,0)
            Centro=1
    return Senal,Centro
def Interpolacion(Senal,Centro,Inter):  
    Final=[]
    for elemento in Senal:
        for i in range(0,Inter):
            Final.append(elemento)
           
    Centro = ((Centro-1) * (Inter))+1
    return Final,Centro
def Diezmacion(Senal,Centro,DesP):
    Diesma=[]
    for r in range(Centro-1,0,-(DesP)):
        Diesma.append(Senal[r])
    Diesma.reverse()
    #print("Izquierda : {}".format(Diesma))
    if(len(Diesma)>0):
        Diesma.pop()
    #print("Izquierda : {}".format(Diesma))
    Centro2 = len(Diesma)+1
    for i  in range(Centro-1,len(Senal),DesP):
        Diesma.append(Senal[i])
    return Diesma,Centro2
def Graficar (Senal,Centro,Titulo):
    #Parte negativa de la recta
    X = []
    for i in range(0,Centro):
        X.append(i*-1)
    X.reverse()
    for p in range(1,len(Senal)-Centro+1):
        X.append(p)

    Con = plt.figure(Titulo)

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(X)

    plt.stem(X,Senal)
    plt.show()
def Grabar_audio():#
    #Definimos paramentros
    FORMAT=pyaudio.paInt16
    CHANNELS=2
    RATE=44100
    CHUNK=1024
    duracion=5
    archivo = "grabacion.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,channels=CHANNELS,rate = RATE,input=True,frames_per_buffer=CHUNK)

    print("Grabando...")
    frames = []

    for i in range(0,int(RATE/CHUNK*duracion)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("Grabacion terminada")
    #print(frames)
    #Terminamos grabacion
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #Creamos/guardamos el archivo
    waveFile = wave.open(archivo,'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    #CODIGO NUEVO :V
    raw_input(">>")
    wf = wave.open(archivo, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate = RATE, output = True)
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.close()
    p.terminate() 
def Convertir_Audio():
    fs, data = wavfile.read('./grabacion.wav')
    Senal=[]
    for i in range(20,600):
        Senal.append(data[i][0])
    #print(Senal)
    #print(fs)
    #print(data)
    #print(type(data))
    return Senal
Titulo="Convolucion Discreta"
Opciones = ["Amplificacion","Reflejo","Desplazamiento","Interpolacion","Diezmacion"]
Mensage = "\t\t\t\tBIENVENIDOS \n\nEste Programa Realizara las operaciones basicas a una Senal de entrada"
Res = msgbox(Mensage,Titulo,ok_button="Continuemos")
if Res is None:
    sys.exit(0)
choice = choicebox("Seleccione el tipo de convolucion:",Titulo,Opciones)
if choice is None:
    sys.exit(0)
#Titulo2="tipo de Senal"
#Opciones2 = ["Ingresada por Texto","Ingresada por audio"]
#choice2 = choicebox("Seleccione el tipo de Senal:",Titulo2,Opciones2)
if(choice == Opciones[0]):#Amplificacion
    #if( choice2 == Opciones2[0]):
    Campos = ["Senal: ","Centro: ","Amplificanda por: "]
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencia",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)
#
    Senal = Senal_cast(Respuesta[0])
    Centro = int(Respuesta[1])
    amp = float(Respuesta[2])
    #elif (choice2 == Opciones2[1]):#audio
    #    Campos = ["Amplificanda por: "]
    # #   Respuesta = multenterbox("Ingrese el valor a amplificar,El audio se grabara (5seg) despues de dar aceptar","Secuencia Audio",Campos)
    #    amp = float(Respuesta[0])
    #    Grabar_audio()
    #    Senal = Convertir_Audio()
    #    Centro=1



    Graficar(Senal,Centro,"Original")
        
    Amp = Amplificacion(Senal,amp)

    #print(Senal)
    #print(Centro)
    #print(amp)
    #print(Amp)
    #print("Centro es {}: ES {}".format(Centro,Amp[Centro-1]))
 
    #if(choice2 == Opciones2[1]):
    #    msgbox("La Funcion resultante es: \n\n\n x(t) = {}".format(Amp))
    #    msgbox("con Inicio en {} con el Valor: {}".format(Centro,Amp[Centro-1]))
    #else:
    msgbox("La Funcion resultante es: \n\n\n x(t) = {}, con Inicio en {} con el Valor: {}".format(Amp,Centro,Amp[Centro-1]))
    

    Graficar(Amp,Centro,"Final")
elif (choice == Opciones[1]):#Reflejo
    #if( choice2 == Opciones2[0]):
    Campos = ["Senal: ","Centro:"]
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencia",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)

    Senal = Senal_cast(Respuesta[0])
    Centro = int(Respuesta[1])
    #elif (choice2 == Opciones2[1]):#audio
    #    msgbox("El audio se grabara (5seg) despues de dar aceptar","Secuencia Audio")
    #    
    #    Grabar_audio()
    #    Senal = Convertir_Audio()
    #    Centro=1

    Graficar(Senal,int(Centro),"Original")

    #print(Senal)
    #print(Centro)

    Senal,Centro = Reflejar(Senal,Centro)
    
    #print(Senal)
    #print(Centro)
    #print("Centro es {}: ES {}".format(Centro,Senal[int(Centro)-1]))  
    #if(choice2 == Opciones2[1]):
    #    msgbox("La Funcion resultante es: \n\n\n x(t) = {}".format(Senal))
    #    msgbox("con Inicio en {} con el Valor: {}".format(Centro,Senal[Centro-1]))
    #else:
    msgbox("La Funcion resultante es: \n\n\n x(t) = {}, con Inicio en {} con el Valor: {}".format(Senal,Centro,Senal[Centro-1]))


    Graficar(Senal,Centro,"Final")
elif (choice == Opciones[2]):#Dezplazamiento

    #if( choice2 == Opciones2[0]):
    Campos = ["Senal: ","Centro:","Desplazamiento"]
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencia",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)

    Senal = Senal_cast(Respuesta[0])
    Centro = int(Respuesta[1])
    DesP = int(Respuesta[2])
    #elif (choice2 == Opciones2[1]):#audio
    #    Campos = ["Desplazamiento"]
    #    
    #    Respuesta = multenterbox("Ingrese el valor a Desplazar,El audio se grabara (5seg) despues de dar aceptar","Secuencia Audio",Campos)
    #    
    #    Grabar_audio()
    #    Senal = Convertir_Audio()
    #    Centro=1
    #    DesP = int(Respuesta[0])
    Graficar(Senal,Centro,"Original")

    #print(Senal)
    #print(Centro)
    print("Desp: {}".format(DesP))
    Senal,Centro=Desplazamientos(Senal,Centro,DesP)

    #print(Senal)
    #print(Centro)
    #if(choice2 == Opciones2[1]):
    # #   msgbox("La Funcion resultante es: \n\n\n x(t) = {}".format(Senal))
    #    msgbox("con Inicio en {} con el Valor: {}".format(Centro,Senal[Centro-1]))
    #else:
    msgbox("La Funcion resultante es: \n\n\n x(t) = {}, con Inicio en {} con el Valor: {}".format(Senal,Centro,Senal[Centro-1]))

    Graficar(Senal,Centro,"Final")
elif (choice == Opciones[3]):#Interpolacion

    #if( choice2 == Opciones2[0]):
    Campos = ["Senal: ","Centro:","Interpolativo (n/ ): "]
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencia",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)
    Senal = Senal_cast(Respuesta[0])
    Centro = int(Respuesta[1])
    Inter = int(Respuesta[2])
    #elif (choice2 == Opciones2[1]):#audio
    #    Campos = ["Interpolativo (n/ ): "]
    #    
    #    Respuesta = multenterbox("Ingrese el valor a Interpolar,El audio se grabara (5seg) despues de dar aceptar","Secuencia Audio",Campos)
    #    
     #   Grabar_audio()
    #    Senal = Convertir_Audio()
    #    Centro=1
    #    Inter = int(Respuesta[0])

    Graficar(Senal,Centro,"Original")

    #print(Senal)
    #print(Centro)

    Final,Centro = Interpolacion(Senal,Centro,Inter)
    
    #print(Final)
    #print(Centro)
    #if(choice2 == Opciones2[1]):
    #    msgbox("La Funcion resultante es: \n\n\n x(t) = {}".format(Final))
    #    msgbox("con Inicio en {} con el Valor: {}".format(Centro,Final[Centro-1]))
   # else:
    msgbox("La Funcion resultante es: \n\n\n x(t) = {}, con Inicio en {} con el Valor: {}".format(Final,Centro,Final[Centro-1]))

    Graficar(Final,Centro,"Final")
elif (choice == Opciones[4]):#Diezmacion

    #if( choice2 == Opciones2[0]):
    Campos = ["Senal: ","Centro:","Diezamtivo: "]
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencia",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)
    Senal = Senal_cast(Respuesta[0])
    Centro = int(Respuesta[1])
    DesP = int(Respuesta[2])
    #elif (choice2 == Opciones2[1]):#audio
    #    Campos = ["Diezamtivo: "]
    #    
    #    Respuesta = multenterbox("Ingrese el valor a Diezmar,El audio se grabara (5seg) despues de dar aceptar","Secuencia Audio",Campos)
    #    
    #    Grabar_audio()
    #    Senal = Convertir_Audio()
    #    Centro=1
    #    DesP = int(Respuesta[0])

    
    Graficar(Senal,Centro,"Original")

    Diesma,Centro2 = Diezmacion(Senal,Centro,DesP)
    #print(Senal)
    #print(Centro)
    #print(Diesma)
    #print(Centro2)#Este es el Centro despues de la diezmacion


    #if(choice2 == Opciones2[1]):
    #    msgbox("La Funcion resultante es: \n\n\n x(t) = {}".format(Diesma))
   #     msgbox("con Inicio en {} con el Valor: {}".format(Centro2,Diesma[Centro2-1]))
   # else:
    msgbox("La Funcion resultante es: \n\n\n x(t) = {}, con Inicio en {} con el Valor: {}".format(Diesma,Centro2,Diesma[Centro2-1]))

    Graficar(Diesma,Centro2,"Final")

    