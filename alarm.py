import sqlite3
from time import strftime
from tkinter import *
import datetime
import os
import random

infoo="""

        HOLA, si estas viendo esto seguramente tienes el codigo fuente de esta alarma, 
        pues tienes que saber no funciona sin dos archivos de bases de datos ni las importaciones 
        de los widgets, estos vienen ya en el repositorio.(carpeta).
        Espero que este programa te sea util!



"""

#esta funcion almacena la hora actual
x = datetime.datetime.now()



#estas instrucciones recaudan los horarios de la base de datos
conexion=sqlite3.connect("Horario")

cursor=conexion.cursor()
cursor.execute("SELECT HORARIO_LUNES FROM HORARIO")
materiasHorasLunes =cursor.fetchall()

cursor2=conexion.cursor()
cursor2.execute("SELECT HORARIO_MARTES FROM HORARIO")
materiasHorasMartes=cursor2.fetchall()

cursor3=conexion.cursor()
cursor3.execute("SELECT HORARIO_MIERCOLES FROM HORARIO")
materiasHorasMiercoles=cursor3.fetchall()

cursor4=conexion.cursor()
cursor4.execute("SELECT HORARIO_JUEVES FROM HORARIO")
materiasHorasJueves=cursor4.fetchall()

cursor5=conexion.cursor()
cursor5.execute("SELECT HORARIO_VIERNES FROM HORARIO")
materiasHorasViernes=cursor5.fetchall()

cursor6=conexion.cursor()
cursor6.execute("SELECT HORARIO_SABADO FROM HORARIO")
materiasHorasSabado=cursor6.fetchall()

cursor7=conexion.cursor()
cursor7.execute("SELECT HORARIO_DOMINGO FROM HORARIO")
materiasHorasDomingo=cursor7.fetchall()

conexion.commit()

#vaciando las tuplas en listas
LunesHoras=[]
MartesHoras=[]
MiercolesHoras=[]
JuevesHoras=[]
ViernesHoras=[]
SabadoHoras=[]
DomingoHoras=[]

for materia in materiasHorasLunes:
    LunesHoras.append(materia)

for materia in materiasHorasMartes:
    MartesHoras.append(materia)

for materia in materiasHorasMiercoles:
    MiercolesHoras.append(materia)

for materia in materiasHorasJueves:
    JuevesHoras.append(materia)

for materia in materiasHorasViernes:
    ViernesHoras.append(materia)

for materia in materiasHorasSabado:
    SabadoHoras.append(materia)

for materia in materiasHorasDomingo:
    DomingoHoras.append(materia)


#conviertiendo cada elemento en un string
arrLunes=[]
arrMartes=[]
arrMiercoles=[]
arrJueves=[]
arrViernes=[]
arrSabado=[]
arrDomingo=[]


for intervalo in LunesHoras:
    arrLunes.append(intervalo[0])

for intervalo in MartesHoras:
    arrMartes.append(intervalo[0])

for intervalo in MiercolesHoras:
    arrMiercoles.append(intervalo[0])

for intervalo in JuevesHoras:
    arrJueves.append(intervalo[0])

for intervalo in ViernesHoras:
    arrViernes.append(intervalo[0])

for intervalo in SabadoHoras:
    arrSabado.append(intervalo[0])

for intervalo in DomingoHoras:
    arrDomingo.append(intervalo[0])

#convirtiendo el formato de horas a formatos de entero 


#aqui se guarda el formato de entero
intervalosNumerosLunes=[]
intervalosNumerosMartes=[]
intervalosNumerosMiercoles=[]
intervalosNumerosJueves=[]
intervalosNumerosViernes=[]
intervalosNumerosSabado=[]
intervalosNumerosDomingo=[]

#generacion de intervalo

#lunes
primerIntervaloLunes=[]
segundoIntervaloLunes=[]

#Martes
primerIntervaloMartes=[]
segundoIntervaloMartes=[]
#Miercoles
primerIntervaloMiercoles=[]
segundoIntervaloMiercoles=[]
#jueves
primerIntervaloJueves=[]
segundoIntervaloJueves=[]
#Viernes
primerIntervaloViernes=[]
segundoIntervaloViernes=[]
#Sabado
primerIntervaloSabado=[]
segundoIntervaloSabado=[]
#Sabado
primerIntervaloDomingo=[]
segundoIntervaloDomingo=[]


for i in range(14):
    #no olvides que se cambia el arrDIA
    intervalosNumerosLunes.append(arrLunes[i].replace(":","").replace("-",""))
    intervalosNumerosMartes.append(arrMartes[i].replace(":","").replace("-",""))
    intervalosNumerosMiercoles.append(arrMiercoles[i].replace(":","").replace("-",""))
    intervalosNumerosJueves.append(arrJueves[i].replace(":","").replace("-",""))
    intervalosNumerosViernes.append(arrViernes[i].replace(":","").replace("-",""))
    intervalosNumerosSabado.append(arrSabado[i].replace(":","").replace("-",""))
    intervalosNumerosDomingo.append(arrDomingo[i].replace(":","").replace("-",""))

    #aqui se corta el string y se genera el intervalo de tiempo min & max 

    #lunes
    primerIntervaloLunes.append(intervalosNumerosLunes[i][0:4])
    segundoIntervaloLunes.append(intervalosNumerosLunes[i][4:10])

    #Martes
    primerIntervaloMartes.append(intervalosNumerosMartes[i][0:4])
    segundoIntervaloMartes.append(intervalosNumerosMartes[i][4:10])
    
    #Miercoles
    primerIntervaloMiercoles.append(intervalosNumerosMiercoles[i][0:4])
    segundoIntervaloMiercoles.append(intervalosNumerosMiercoles[i][4:10])

    #Jueves
    primerIntervaloJueves.append(intervalosNumerosJueves[i][0:4])
    segundoIntervaloJueves.append(intervalosNumerosJueves[i][4:10]) 

    #Viernes
    primerIntervaloViernes.append(intervalosNumerosViernes[i][0:4])
    segundoIntervaloViernes.append(intervalosNumerosViernes[i][4:10])

    #Sabado
    primerIntervaloSabado.append(intervalosNumerosSabado[i][0:4])
    segundoIntervaloSabado.append(intervalosNumerosSabado[i][4:10])

    #Domingo
    primerIntervaloDomingo.append(intervalosNumerosDomingo[i][0:4])
    segundoIntervaloDomingo.append(intervalosNumerosDomingo[i][4:10])


#aqui se retiran los strings vacios para poder convertir a enteros



#Lunes 
N1=[]
P1=[]

for string in primerIntervaloLunes:
    if(string !=""):
        P1.append(int(string))

for string in segundoIntervaloLunes:
    if(string !=""):
        N1.append(int(string))


#Martes
N2=[]
P2=[]

for string in primerIntervaloMartes:
    if(string !=""):
        P2.append(int(string))

for string in segundoIntervaloMartes:
    if(string !=""):
        N2.append(int(string))

#Miercoles
N3=[]
P3=[]

for string in primerIntervaloMiercoles:
    if(string !=""):
        P3.append(int(string))

for string in segundoIntervaloMiercoles:
    if(string !=""):
        N3.append(int(string))

#Jueves
N4=[]
P4=[]

for string in primerIntervaloJueves:
    if(string !=""):
        P4.append(int(string))

for string in segundoIntervaloJueves:
    if(string !=""):
        N4.append(int(string))


#Viernes
N5=[]
P5=[]

for string in primerIntervaloViernes:
    if(string !=""):
        P5.append(int(string))

for string in segundoIntervaloViernes:
    if(string !=""):
        N5.append(int(string))

#Sabado
N6=[]
P6=[]

for string in primerIntervaloSabado:
    if(string !=""):
        P6.append(int(string))

for string in segundoIntervaloSabado:
    if(string !=""):
        N6.append(int(string))

#Sabado
N7=[]
P7=[]

for string in primerIntervaloDomingo:
    if(string !=""):
        P7.append(int(string))

for string in segundoIntervaloDomingo:
    if(string !=""):
        N7.append(int(string))


#la variable hora nos da la hora del momento actual en el formato "0000"

hora=strftime('%H%M')
#se convierte la hora de texto a entero para poder evaluar los intervalos
hora=int(hora)


# esto filtra el dia en que son las clases y las horas a las que tocan !!! 
#tambien se encarga de asignar el url de cada clase 

def selector(label,entry,display):

    conexion=sqlite3.connect("Urls")

    cursor=conexion.cursor()
    cursor.execute("SELECT URL_LUNES FROM URLS")
    urlsLunes=cursor.fetchall()

    cursorMartes=conexion.cursor()
    cursorMartes.execute("SELECT URL_MARTES FROM URLS")
    urlsMartes=cursorMartes.fetchall()

    cursorMiercoles=conexion.cursor()
    cursorMiercoles.execute("SELECT URL_MIERCOLES FROM URLS")
    urlsMiercoles=cursorMiercoles.fetchall()

    cursorJueves=conexion.cursor()
    cursorJueves.execute("SELECT URL_JUEVES FROM URLS")
    urlsJueves=cursorJueves.fetchall()

    cursorViernes=conexion.cursor()
    cursorViernes.execute("SELECT URL_VIERNES FROM URLS")
    urlsViernes=cursorViernes.fetchall()

    cursorSabado=conexion.cursor()
    cursorSabado.execute("SELECT URL_SABADO FROM URLS")
    urlsSabado=cursorSabado.fetchall()

    cursorDomingo=conexion.cursor()
    cursorDomingo.execute("SELECT URL_DOMINGO FROM URLS")
    urlsDomingo=cursorDomingo.fetchall()


    conexion.commit()



    LunesUrls=[]
    ListLunes=[]

    MartesUrls=[]
    ListMartes=[]

    MiercolesUrls=[]
    ListMiercoles=[]

    JuevesUrls=[]
    ListJueves=[]

    ViernesUrls=[]
    ListViernes=[]

    SabadoUrls=[]
    ListSabado=[]

    DomingoUrls=[]
    ListDomingo=[]

    #Lunes
    for i in urlsLunes:
        LunesUrls.append(i)

    for intervalo in LunesUrls:
        ListLunes.append(intervalo[0])
    #Martes
    for i in urlsMartes:
        MartesUrls.append(i)

    for intervalo in MartesUrls:
        ListMartes.append(intervalo[0])
    #Miercoles
    for i in urlsMiercoles:
        MiercolesUrls.append(i)

    for intervalo in MiercolesUrls:
        ListMiercoles.append(intervalo[0])
    #Jueves
    for i in urlsJueves:
        JuevesUrls.append(i)

    for intervalo in JuevesUrls:
        ListJueves.append(intervalo[0])
    
    #Viernes
    for i in urlsViernes:
        ViernesUrls.append(i)

    for intervalo in ViernesUrls:
        ListViernes.append(intervalo[0])
    #Sabado
    for i in urlsSabado:
        SabadoUrls.append(i)

    for intervalo in SabadoUrls:
        ListSabado.append(intervalo[0])
    #Domingo
    for i in urlsDomingo:
        DomingoUrls.append(i)

    for intervalo in DomingoUrls:
        ListDomingo.append(intervalo[0])

    #AQUI SE RETIRAN ESPACION EN BLANCO ya que los espacios en blanco generan un lugar mas en el arreglo
    #por lo tanto el Numero de urls por dia tie que ser igual al numero de intervalos
    #ejemplo len(P)=5 por lo tanto len(listaMartes)=5 


    listaLunes=[]
    for string in ListLunes:
        if(string !=""):
            listaLunes.append(string)


    listaMartes=[]
    for string in ListMartes:
        if(string !=""):
            listaMartes.append(string)
    
    listaMiercoles=[]
    for string in ListMiercoles:
        if(string !=""):
            listaMiercoles.append(string)
    
    listaJueves=[]
    for string in ListJueves:
        if(string !=""):
            listaJueves.append(string)
    
    listaViernes=[]
    for string in ListViernes:
        if(string !=""):
            listaViernes.append(string)
    
    listaSabado=[]
    for string in ListSabado:
        if(string !=""):
            listaSabado.append(string)
    
    listaDomingo=[]
    for string in ListDomingo:
        if(string !=""):
            listaDomingo.append(string)



    #Lunes
    if (x.strftime("%a")=="Mon"):
        
        if(len(N1)==0):
            entry.set("sin clases hoy")
            label.set("toma un descanso!")
        else:
            label.set("hoy solo tienes "+str(len(N1))+ " clases !")

        for i in range(len(P1)):
            if(P1[i]<=hora<N1[i]):
                display.delete(0,END)
                display.insert(0,listaLunes[i])
       
    #Martes
    elif (x.strftime("%a")=="Tue"):
        if(len(N2)==0):
            entry.set("sin clases hoy")
            label.set("toma un descanso!")
        else:
            label.set("hoy solo tienes "+str(len(N1))+ " clases !")
        for i in range(len(P2)):

            if(P2[i]<=hora<N2[i]):
                display.delete(0,END)
                display.insert(0,listaMartes[i])
            
      
                  
   
    #Miercoles
    elif (x.strftime("%a")=="Wed"):
        if(len(N3)==0):
            entry.set("sin clases hoy")
            label.set("toma un descanso!")
        else:
            label.set("hola! hoy solo tienes "+str(len(N3))+ " clases !")
       
        for i in range(len(P3)):
            if(P3[i]<=hora<N3[i]):
                display.delete(0,END)
                display.insert(0,listaMiercoles[i])

    #Jueves
    elif (x.strftime("%a")=="Thu"):
        if(len(N4)==0):
            entry.set("sin clases hoy")
            label.set("toma un descanso!")
        else:
            label.set("hola! hoy solo tienes "+str(len(N4))+ " clases !")
        for i in range(len(P4)):
            if(P4[i]<=hora<N4[i]):
                display.delete(0,END)
                display.insert(0,listaJueves[i])
               
   

    #Viernes
    elif (x.strftime("%a")=="Fri"):
        if(len(N5)==0):
            entry.set("no hay clase para esta hora")
            label.set("toma un descanso!")
        else:
            label.set("hola! hoy solo tienes "+str(len(N5))+ " clases !")
        for i in range(len(P5)):
            if(P5[i]<=hora<N5[i]):
                display.delete(0,END)
                display.insert(0,listaViernes[i])
 
 

    #Sabado
    elif (x.strftime("%a")=="Sat"):
        if(len(N6)==0):
            entry.set("sin clases hoy")
            label.set("toma un descanso!")
        else:
            label.set("hola! hoy solo tienes "+str(len(N6))+ " clases !")
     
        for i in range(len(P6)):
            if(P6[i]<=hora<N6[i]):
                display.delete(0,END)
                display.insert(0,listaSabado[i])
    #Domingo
    elif (x.strftime("%a")=="Sun"):
        if(len(N7)==0):
            label.set("toma un descanso!")
        else:
            label.set("hola! hoy solo tienes "+str(len(N7))+ " clases !")
        for i in range(len(P7)):   
            if(P7[i]<=hora<N7[i]):
                display.delete(0,END)
                display.insert(0,listaDomingo[i])


