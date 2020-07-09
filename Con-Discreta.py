from easygui import *
import sys
import matplotlib.pyplot as plt
import numpy as np



Titulo="Convolucion Discreta"
Opciones = ["Finita","Periodica","Circular"]
Mensage = "\t\t\t\tBIENVENIDOS \n\nEste Programa Realizara la convolucion Discreta\nen funciones Finitas y Periodicas"
Res = msgbox(Mensage,Titulo,ok_button="Continuemos")
if Res is None:
    sys.exit(0)
choice = choicebox("Seleccione el tipo de convolucion:",Titulo,Opciones)
if (choice  == Opciones[0]):#Finita
    Campos = ["Funcion 1:","Inicio 1:","Funcion 2:","Inicio 2:"]
    Respuesta = []
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencias",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)
    

    Secuencia_1 = Respuesta[0].split(",")
    Centro_1 = int(Respuesta[1])
    Secuencia_2 = Respuesta[2].split(",")
    Centro_2 = int(Respuesta[3])


    #Graficar cada una

    x1=[]
    x2=[]
    if Centro_1<0:
        for i in range(Centro_1,len(Secuencia_1)+Centro_1):
            x1.append(i)
    elif Centro_1 == 0:
        for i in range(0,len(Secuencia_1)):
            x1.append(i)

    if Centro_2<0:
        for i in range(Centro_2,len(Secuencia_2)+Centro_2):
            x2.append(i)
    elif Centro_2 == 0:
        for i in range(0,len(Secuencia_2)):
            x2.append(i)

    Secuencia_1_2=[]
    Secuencia_2_2=[]

    for elementos in Secuencia_1:
        Secuencia_1_2.append(float(eval(elementos)))
        
    for elementos in Secuencia_2:
        Secuencia_2_2.append(float(eval(elementos)))

    Con = plt.figure("Primeras")

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x1)

    plt.stem(x1,Secuencia_1_2)

    Conu = plt.figure("Segunda")
    ax = Conu.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x2)

    plt.stem(x2,Secuencia_2_2)

    plt.show()

    Solucion = {}
    for i in range(0,len(Secuencia_1)):
        Solucion[i]=[]
    for indice,elemento in enumerate(Secuencia_1):
        for i in range(indice):
            Solucion[indice].append(0)
            pass
        for elemnto2 in Secuencia_2:
            Solucion[indice].append(float(eval(elemento))*float(eval(elemnto2)))
            pass
        pass
    maximo = len(Solucion[indice])
    for i in range(indice):
        while len(Solucion[i])<maximo:
            Solucion[i].append(0)
            pass
        pass
    Solucion["Resultado"] = []
    for i in range(maximo ):
        suma = 0
        for e in range(indice+1):
            suma=suma + Solucion[e][i]       
            pass
        Solucion["Resultado"].append(suma)
        pass
    Centro_F = Centro_1 + Centro_2
    x=[]
    if Centro_F<0:
        for i in range(Centro_F,len(Solucion["Resultado"])+Centro_F):
            x.append(i)
    elif Centro_F == 0:
        for i in range(0,len(Solucion["Resultado"])):
            x.append(i)
        
    Cen =  Solucion["Resultado"][Centro_F*-1]

    msgbox("La Funcion resultante de la convolucion es: \n\n\n x(t) = {},\n con Inicio en {} el valor es {}".format(Solucion["Resultado"],Centro_F,Cen))
    Con = plt.figure()

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x)

    plt.stem(x,Solucion["Resultado"])
    plt.show()
    pass
elif (choice  == Opciones[1]):#Periodica
    Campos = ["Funcion(periodica) 1:","Inicio 1:","Funcion 2:","Inicio 2:"]
    Respuesta = []
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencias",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)

    Secuencia_1 = Respuesta[0].split(",")
    Centro_1 = int(Respuesta[1])
    Secuencia_2 = Respuesta[2].split(",")
    Centro_2 = int(Respuesta[3])
    

        #Graficar cada una
    Secuencia_1_2=[]
    Secuencia_2_2=[]

    for elementos in Secuencia_1:
        Secuencia_1_2.append(float(eval(elementos)))
        
    for elementos in Secuencia_2:
        Secuencia_2_2.append(float(eval(elementos)))


    Sec1=Secuencia_1_2         
    for elemento in range(0,len(Secuencia_1_2)):
        Sec1.append(Secuencia_1_2[elemento])

    x1=[]
    x2=[]
    if Centro_1<0:
        for i in range(Centro_1,len(Sec1)+Centro_1):
            x1.append(i)
    elif Centro_1 == 0:
        for i in range(0,len(Sec1)):
            x1.append(i)

    if Centro_2<0:
        for i in range(Centro_2,len(Secuencia_2)+Centro_2):
            x2.append(i)
    elif Centro_2 == 0:
        for i in range(0,len(Secuencia_2)):
            x2.append(i)

    

    Con = plt.figure("Primeras")

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x1)

    plt.stem(x1,Sec1)

    Conu = plt.figure("Segunda")
    ax = Conu.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x2)

    plt.stem(x2,Secuencia_2_2)

    plt.show()



    Solucion = {}
    for i in range(0,len(Secuencia_1)):
        Solucion[i]=[]
    for indice,elemento in enumerate(Secuencia_1):
        for i in range(indice):
            Solucion[indice].append(0)
            pass
        for elemnto2 in Secuencia_2:
            Solucion[indice].append(float(eval(elemento))*float(eval(elemnto2)))
            pass
        pass
    maximo = len(Solucion[indice])
    for i in range(indice):
        while len(Solucion[i])<maximo:
            Solucion[i].append(0)
            pass
        pass
    Solucion["SResultado"] = []
    for i in range(maximo ):
        suma = 0
        for e in range(indice+1):
            suma=suma + Solucion[e][i]       
            pass
        Solucion["SResultado"].append(suma)
        pass
    long_periodica = len(Secuencia_1) 
    Semi = {}
    if (len(Solucion["SResultado"])%long_periodica == 0):
        num_ite = len(Solucion["SResultado"])/long_periodica
        i=0
        for nu in range(num_ite):
            
            Semi[nu] = []
            for e in Solucion["SResultado"]:
                Semi[nu].append(Solucion["SResultado"][i])
                if(i>0 and (i+1)%long_periodica ==0):
                    i= i+1
                    break
                i = i+1
                pass
            pass
    else:
        faltantes = long_periodica - len(Solucion["SResultado"])%long_periodica
        fin=(len(Solucion["SResultado"])+faltantes)
        while len(Solucion["SResultado"])<fin:
            Solucion["SResultado"].append(0)
            pass
        num_ite = len(Solucion["SResultado"])/long_periodica
        i=0
        for nu in range(num_ite):
            Semi[nu] = []
            for e in Solucion["SResultado"]:
                Semi[nu].append(Solucion["SResultado"][i])
                if(i>0 and (i+1)%long_periodica ==0):
                    i= i+1
                    break
                i = i+1
                pass
            pass
        pass    
    Solucion["Resultado"] = []
    for i in range(long_periodica):
        suma = 0
        for e in range(num_ite):
            suma=suma + Semi[e][i]       
            pass
        Solucion["Resultado"].append(suma)
        pass
    Centro_F = Centro_1 + Centro_2 
    print ("La Funcion resultante de la convolucion es:{}".format(Solucion["SResultado"]))
    print (Semi)
    print ("La Funcion resultante de la convolucion es:{}".format(Solucion["Resultado"]))
    print (Centro_F)
    
    Res = []
    for i in range(0,2):
        for elementos  in Solucion["Resultado"]:
            Res.append(elementos)       
    
    x=[]
    if Centro_F<0:
        if((Centro_F*-1)>long_periodica):
            Centro_F= Centro_F+long_periodica
        else:
            pass
        for i in range(Centro_F,len(Res)+Centro_F):
            x.append(i)
    elif Centro_F == 0:
        for i in range(0,len(Res)):
            x.append(i)

    Cen =  Solucion["Resultado"][Centro_F*-1]

    msgbox("La Funcion resultante de la convolucion es: \n\n\n x(t) = ...{}... , con Inicio en {} Valor = {}".format(Solucion["Resultado"],Centro_F,Cen))
    Con = plt.figure()

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x)

    plt.stem(x,Res)
    plt.show()
elif (choice  == Opciones[2]):#Circular
    Campos = ["Funcion(periodica) 1:","Inicio 1:","Funcion(periodica) 2:","Inicio 2:"]
    Respuesta = []
    Respuesta = multenterbox("Ingrese las secuencias para realizar la operacion:","Secuencias",Campos)

    if Respuesta is None:
        msgbox("Los Campos no fueron llenados","Error")
        sys.exit(0)

    Secuencia_1 = Respuesta[0].split(",")
    Centro_1 = int(Respuesta[1])
    Secuencia_2 = Respuesta[2].split(",")
    Centro_2 = int(Respuesta[3])

        #Graficar cada una
    Secuencia_1_2=[]
    Secuencia_2_2=[]

    for elementos in Secuencia_1:
        Secuencia_1_2.append(float(eval(elementos)))
        
    for elementos in Secuencia_2:
        Secuencia_2_2.append(float(eval(elementos)))

    Sec1=Secuencia_1_2         
    for elemento in range(0,len(Secuencia_1_2)):
        Sec1.append(Secuencia_1_2[elemento])

    Sec2=Secuencia_2_2         
    for elemento in range(0,len(Secuencia_2_2)):
        Sec2.append(Secuencia_2_2[elemento])


    x1=[]
    x2=[]
    if Centro_1<0:
        for i in range(Centro_1,len(Sec1)+Centro_1):
            x1.append(i)
    elif Centro_1 == 0:
        for i in range(0,len(Sec1)):
            x1.append(i)

    if Centro_2<0:
        for i in range(Centro_2,len(Sec2)+Centro_2):
            x2.append(i)
    elif Centro_2 == 0:
        for i in range(0,len(Sec2)):
            x2.append(i)

    

    Con = plt.figure("Primeras")

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x1)

    plt.stem(x1,Sec1)

    Conu = plt.figure("Segunda")
    ax = Conu.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x2)

    plt.stem(x2,Sec2)

    plt.show()


    Solucion = {}
    for i in range(0,len(Secuencia_1)):
        Solucion[i]=[]
    for indice,elemento in enumerate(Secuencia_1):
        for i in range(indice):
            Solucion[indice].append(0)
            pass
        for elemnto2 in Secuencia_2:
            Solucion[indice].append(float(eval(elemento))*float(eval(elemnto2)))
            pass
        pass
    maximo = len(Solucion[indice])
    for i in range(indice):
        while len(Solucion[i])<maximo:
            Solucion[i].append(0)
            pass
        pass
    Solucion["SResultado"] = []
    for i in range(maximo ):
        suma = 0
        for e in range(indice+1):
            suma=suma + Solucion[e][i]       
            pass
        Solucion["SResultado"].append(suma)
        pass
    if (len(Secuencia_2)>=(len(Secuencia_1))):
        long_periodica = len(Secuencia_2)
        pass
    else:
        long_periodica = len(Secuencia_1)
        pass
    Semi = {}
    if (len(Solucion["SResultado"])%long_periodica == 0):
        num_ite = len(Solucion["SResultado"])/long_periodica
        i=0
        for nu in range(num_ite):
            
            Semi[nu] = []
            for e in Solucion["SResultado"]:
                Semi[nu].append(Solucion["SResultado"][i])
                if(i>0 and (i+1)%long_periodica ==0):
                    i= i+1
                    break
                i = i+1
                pass
            pass
    else:
        faltantes = long_periodica - len(Solucion["SResultado"])%long_periodica
        fin=(len(Solucion["SResultado"])+faltantes)
        while len(Solucion["SResultado"])<fin:
            Solucion["SResultado"].append(0)
            pass
        num_ite = len(Solucion["SResultado"])/long_periodica
        i=0
        for nu in range(num_ite):
            Semi[nu] = []
            for e in Solucion["SResultado"]:
                Semi[nu].append(Solucion["SResultado"][i])
                if(i>0 and (i+1)%long_periodica ==0):
                    i= i+1
                    break
                i = i+1
                pass
            pass
        pass    
    Solucion["Resultado"] = []
    for i in range(long_periodica):
        suma = 0
        for e in range(num_ite):
            suma=suma + Semi[e][i]       
            pass
        Solucion["Resultado"].append(suma)
        pass
    Centro_F = Centro_1 + Centro_2 
    print(Secuencia_1)
    print(Centro_1)
    print(Secuencia_2)
    print(Centro_2)
    print ("La Funcion resultante de la convolucion es:{}".format(Solucion["SResultado"]))
    print (Semi)
    print ("La Funcion resultante de la convolucion es:{}".format(Solucion["Resultado"]))  

    Res = []
    for i in range(0,2):
        for elementos  in Solucion["Resultado"]:
            Res.append(elementos)   

    x=[]
    if Centro_F<0:
        if((Centro_F*-1)>long_periodica):
            Centro_F= Centro_F+long_periodica
        else:
            pass
        for i in range(Centro_F,len(Res)+Centro_F):
            x.append(i)
    elif Centro_F == 0:
        for i in range(0,len(Res)):
            x.append(i)
        
    Cen =  Solucion["Resultado"][Centro_F*-1]
    msgbox("La Funcion resultante de la convolucion es periodica: \n\n\n x(t) = ...{}..., con Inicio en {} con el Valor: {}".format(Solucion["Resultado"],Centro_F,Cen))
    Con = plt.figure()

    ax = Con.add_subplot(1,1,1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks(x)

    plt.stem(x,Res)
    plt.show()
    pass