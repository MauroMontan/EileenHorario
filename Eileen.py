from tkinter import *
from tkinter import messagebox
from time import strftime
import sqlite3
import os 
from alarm import selector
import random
import webbrowser
import subprocess


   
def salir():
    valor=messagebox.askquestion("salir","deseas salir de la aplicación?")

    if valor=="yes":
        root.destroy()



root=Tk()
configIcon=PhotoImage(file=os.path.abspath("statics/edit.png"))
ajustarIcon=PhotoImage(file=os.path.abspath("statics/cosecha.png"))
materiaIcon=PhotoImage(file=os.path.abspath("statics/escritura.png"))
saveIcon=PhotoImage(file=os.path.abspath("statics/disquete.png"))
searchIcon=PhotoImage(file=os.path.abspath("statics/lupa.png"))
refreshIcon=PhotoImage(file=os.path.abspath("statics/actualizar.png"))
quitIcon=PhotoImage(file=os.path.abspath("statics/cerrar.png"))
meetIcon=PhotoImage(file=os.path.abspath("statics/meet.png"))
teamsIcon=PhotoImage(file=os.path.abspath("statics/teams.png"))
zoomIcon=PhotoImage(file=os.path.abspath("statics/zoomV.png"))
confDIcon=PhotoImage(file=os.path.abspath("statics/confD.png"))
root.iconphoto(False,PhotoImage(file='statics/calendario.png'))
root.title("Eileen")
root.resizable(False,False)


nDias=IntVar()
GrupoVAR=StringVar()
nMaterias=IntVar()
nMateria=StringVar()
NombreMateria=StringVar()
horasLunes=StringVar()
horasMartes=StringVar()
horasMiercoles=StringVar()
horasJueves=StringVar()
horasViernes=StringVar()
horasSabado=StringVar()
horasDomingo=StringVar()


url_Lunes=StringVar()
url_Martes=StringVar()
url_Miercoles=StringVar()
url_Jueves=StringVar()
url_Viernes=StringVar()
url_Sabado=StringVar()
url_Domimgo=StringVar()






def escribir(ventana):
    try:
        if(nDias.get()>7):

            messagebox.showwarning(message="Oye! una semana no tiene {} días!".format(nDias.get()), title="ingresa otro valor")
        elif(nMaterias.get()>14):
            messagebox.showwarning(message="No creí que fuese posible ! {} están fuera de mi rango por ahora!".format(nMaterias.get()), title="ingresa otro valor")
        else:
            datosInFich=[str(nDias.get()),str(nMaterias.get())]
            configuraciones=open("config.mauro","w")
            for configs in datosInFich:
                configuraciones.write(configs)
                configuraciones.write("\n")
            
            configuraciones.close()
            ventana.destroy()
            root.destroy()
            try:
                subprocess.Popen("Eileen.exe")
            except:
                os.system("./Eileen")
    except:
        messagebox.showwarning(message="Los valores tienen que ser numéricos", title="ingresa valores numérico")
        pass



configvalues=[]

def leer():
    configuraciones=open("config.mauro","r")


    x=configuraciones.readlines()

    for i in range(2):
        c=x[i].replace("\n", "")
        configvalues.append(c)



    configuraciones.close()

leer()

NdiasValue=int(configvalues[0])
nMateriasValue=int(configvalues[1])

NdiasABS=int(configvalues[0])+3


def refresh():

    Tableframe.after(300,table)

def nuevaMateria_write(ventana):
    conexion=sqlite3.connect("Horario")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO HORARIO VALUES (NULL,'"+GrupoVAR.get()+
                    "','"+NombreMateria.get()+"','"+horasLunes.get()+"','"+horasMartes.get()+
                    "','"+horasMiercoles.get()+"','"+horasJueves.get()+
                    "','"+horasViernes.get()+"','"+horasSabado.get()+
                    "','"+horasDomingo.get()+"')")
    conexion.commit()
  
    Tableframe.after(100,table)


def actualizar(window,top):
    conexion=sqlite3.connect("Horario")
    cursor=conexion.cursor()
    cursor.execute("""UPDATE HORARIO SET GRUPO='{}' , NOMBRE_DE_LA_MATERIA='{}' , 
                        HORARIO_LUNES='{}' , HORARIO_MARTES='{}' , HORARIO_MIERCOLES='{}' , 
                        HORARIO_JUEVES='{}' , HORARIO_VIERNES='{}' , HORARIO_SABADO='{}' , HORARIO_DOMINGO='{}' WHERE NUMERO_DE_MATERIA='{}' """.format(GrupoVAR.get(),NombreMateria.get(),horasLunes.get(),horasMartes.get(),horasMiercoles.get(),horasJueves.get(),horasViernes.get(),horasSabado.get(),horasDomingo.get(),nMateria.get()))
    conexion.commit()
    
    urlsconnect=sqlite3.connect("Urls")
    UrlsCursor=urlsconnect.cursor()
    UrlsCursor.execute("""UPDATE URLS SET URL_LUNES='{}' , URL_MARTES='{}' , URL_MIERCOLES='{}' , 
                        URL_JUEVES='{}' , URL_VIERNES='{}' , URL_SABADO='{}' , URL_DOMINGO='{}' WHERE N_URL='{}' """.format(url_Lunes.get(),url_Martes.get(),url_Miercoles.get(),url_Jueves.get(),url_Viernes.get(),url_Sabado.get(),url_Domimgo.get(),nMateria.get()))
    
    urlsconnect.commit()
    
    
    messagebox.showinfo("busqueda","se cambio los datos de la materia con exito!\n si no seguiras editando cierra la ventana")
    top.destroy()
    window.after(300,nuevaMateria_view)
    Tableframe.after(300,table)


def BuscarPorNumero(newpos,lfMateria,lfHorario,lfUrls,panelFrame,indice,cerrar,lunesUrlEntry,m,mier,j,v,s,d):

    
        
    conexion=sqlite3.connect("Horario")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM HORARIO WHERE NUMERO_DE_MATERIA="+nMateria.get())
    materias=cursor.fetchall()

    urlsconnect=sqlite3.connect("Urls")
    UrlCursor=urlsconnect.cursor()
    UrlCursor.execute("SELECT * FROM URLS WHERE N_URL="+nMateria.get())
    urls=UrlCursor.fetchall()

    for materia in materias:
        nMateria.set(materia[0])
        NombreMateria.set(materia[2])
        GrupoVAR.set(materia[1])
        horasLunes.set(materia[3])
        horasMartes.set(materia[4])
        horasMiercoles.set(materia[5])
        horasJueves.set(materia[6])
        horasViernes.set(materia[7])
        horasSabado.set(materia[8])
        horasDomingo.set(materia[9])
    try:
        for url in urls:
            url_Lunes.set(url[1])
            url_Martes.set(url[2])
            url_Miercoles.set(url[3])
            url_Jueves.set(url[4])
            url_Viernes.set(url[5])
            url_Sabado.set(url[6])
            url_Domimgo.set(url[7])
    except:
        print("f")
    

    urlsconnect.commit()
    conexion.commit()
    if(horasLunes.get()==""):
        lunesUrlEntry.config(state="disabled")
    if(horasMartes.get()==""):
        m.config(state="disabled")
    if(horasMiercoles.get()==""):
        mier.config(state="disabled")
    if(horasJueves.get()==""):
        j.config(state="disabled")
    if(horasViernes.get()==""):
        v.config(state="disabled")
    if(horasSabado.get()==""):
        s.config(state="disabled")
    if(horasDomingo.get()==""):
        d.config(state="disabled")


    
    indice.config(state="disabled")
    lfHorario.grid(row=1,column=0,padx=20,pady=10)
    lfUrls.grid(row=1,column=1,padx=20,pady=10)
    lfMateria.grid(row=0,column=0,padx=20,pady=10)
    newpos.grid(row=18,column=1,padx=20,pady=10)
    cerrar.grid(row=18,column=0,padx=10,pady=3)
    panelFrame.destroy()
    

def initConfigMenuWindow():
        
    configMenu=Toplevel()
    configMenu.config(bg=color.white,width=300,height=500)
    configMenu.title("configuraciones")
    frame=Frame(configMenu,bg=color.white)
    frame.pack()
    label=Label(frame,bg=color.white,text="cuantas materias llevas?",anchor="w",fg="black")
    label.grid(row=0,column=0,padx=20,pady=10)

    

    nMaterias_E=Entry(frame,bg="lightblue",justify=CENTER,fg="black",textvariable=nMaterias)
    nMaterias_E.grid(row=0,column=1,padx=20,pady=10)

    label=Label(frame,bg=color.white ,text="cuantos dias a la semana vas a la escuela?",anchor="w",fg="black")
    label.grid(row=1,column=0,padx=20,pady=10)
    nDias_E=Entry(frame,bg="lightblue",justify=CENTER,textvariable=nDias,fg="black")
    nDias_E.grid(row=1,column=1,padx=20,pady=10)

    nMaterias_E.delete(0,END)
    nDias_E.delete(0,END)
    guardar=Button(configMenu,image=saveIcon,bg=color.white, command=lambda:escribir(configMenu))
    guardar.pack()

def nuevaMateria_view():
    
        
        
    configMenu=Toplevel()
    configMenu.config(bg="lightblue",width=300,height=500)
    configMenu.resizable(False,False)
    configMenu.title("añadir nueva materia")
    frame=Frame(configMenu,bg=color.white)
    frame.pack()

    lf1=LabelFrame(frame,bg="white",fg="green",bd=3,text="Datos de la materia")
    lf1.grid(row=0,column=0,padx=20,pady=10)
    lf1.grid_forget()
    nombreMateria=Label(lf1,bg=color.white,text="Nombre de la materia",anchor="w",fg="black")
    nombreMateria.grid(row=0,column=0,padx=20,pady=10)
    nombreMateria_E=Entry(lf1,bg="lightgreen",justify=CENTER,width=27,textvariable=NombreMateria,font="calibri 11", fg="black")
    nombreMateria_E.grid(row=0,column=1,padx=20,pady=10)
    nombreMateria_E.delete(0,END)
    gruplabel=Label(lf1,bg=color.white,text="Grupo",anchor="w",fg="black")
    gruplabel.grid(row=1,column=0,padx=20,pady=10)
    grupo=Entry(lf1,width=27,bg="lightblue",bd=0,textvariable=GrupoVAR,justify=CENTER,font="calibri 11",fg="black")
    grupo.grid(row=1,column=1,padx=20,pady=10)
    grupo.delete(0,END)


    lf=LabelFrame(frame,bg="white",fg="green",bd=5,text="buscar materia")
    lf.grid(row=0,column=1,padx=20,pady=10)

    IndiceDeMateria=Label(lf,bg=color.white,text="cual es el indice de la materia\n que quiere cambiar?",anchor="w",fg="black")
    IndiceDeMateria.grid(row=0,column=0,padx=20,pady=10)

    indice=Entry(lf,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=nMateria)
    indice.grid(row=1,column=0,padx=20,pady=10)
    indice.delete(0,END)
    lf3=LabelFrame(frame,bg="white",fg="green",text="Enlaces de Reunión")
    lf3.grid(row=1,column=1,padx=20,pady=10)
    lf3.grid_forget()

    urlLunes=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Lunes)
    urlLunes.grid(row=2,column=2,padx=20,pady=10)
    urlLunes.delete(0,END)
    
    urlMartes=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Martes)
    urlMartes.grid(row=3,column=2,padx=20,pady=10)
    urlMartes.delete(0,END)
    urlMiercoles=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Miercoles)
    urlMiercoles.grid(row=4,column=2,padx=20,pady=10)
    urlMiercoles.delete(0,END)
    urlJueves=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Jueves)
    urlJueves.grid(row=5,column=2,padx=20,pady=10)
    urlJueves.delete(0,END)
    urlViernes=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Viernes)
    urlViernes.grid(row=6,column=2,padx=20,pady=10)
    urlViernes.delete(0,END)
    urlSabado=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Sabado)
    urlSabado.grid(row=7,column=2,padx=20,pady=10)
    urlSabado.delete(0,END)
    urlDomingo=Entry(lf3,bg="lightblue",justify=CENTER,width=27,font="calibri 11", fg="black",textvariable=url_Domimgo)
    urlDomingo.grid(row=8,column=2,padx=20,pady=10)
    urlDomingo.delete(0,END)
    if(NdiasValue==6):
        urlDomingo.grid_forget()
    elif(NdiasValue==5):
        urlDomingo.grid_forget()
        urlSabado.grid_forget()
    elif(NdiasValue==4):
        urlDomingo.grid_forget()
        urlSabado.grid_forget()
        urlViernes.grid_forget()      
    elif(NdiasValue==3):
        urlDomingo.grid_forget()
        urlSabado.grid_forget()
        urlViernes.grid_forget()
        urlJueves.grid_forget()
    elif(NdiasValue==2):
        urlDomingo.grid_forget()
        urlSabado.grid_forget()
        urlViernes.grid_forget()
        urlJueves.grid_forget()
        urlMiercoles.grid_forget()
    elif(NdiasValue==1):
        urlDomingo.grid_forget()
        urlSabado.grid_forget()
        urlViernes.grid_forget()
        urlJueves.grid_forget()
        urlMiercoles.grid_forget()
        urlLunes.grid_forget()
    else:
        pass


    lf2=LabelFrame(frame,bg="white",fg="green",text="Horarios de la Materia")
    lf2.grid(row=1,column=0,padx=20,pady=10)
    lf2.grid_forget()

    HlText=["Lunes","Martes","Miércoles","Jueves","Viernes","Sabado","Domingo"]
    
    L=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasLunes,justify=CENTER,font="calibri 11",fg="black")
    M=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasMartes,justify=CENTER,font="calibri 11",fg="black")
    Mier=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasMiercoles,justify=CENTER,font="calibri 11",fg="black")
    J=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasJueves,justify=CENTER,font="calibri 11",fg="black")
    V=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasViernes,justify=CENTER,font="calibri 11",fg="black")
    S=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasSabado,justify=CENTER,font="calibri 11",fg="black")
    D=Entry(lf2,width=27,bg="lightblue",bd=0,textvariable=horasDomingo,justify=CENTER,font="calibri 11",fg="black")

    WidgetsVars=[L,M,Mier,J,V,S,D]

    
   
    for i in range(NdiasValue):
        
        label=Label(lf2,text=HlText[i],width=27,bg="white",bd=1,fg="black")
        label.grid(row=i+2,column=0,pady=7,padx=6)
        WidgetsVars[i].grid(row=i+2,column=1,padx=2,pady=5,ipady=6)
        WidgetsVars[i].delete(0,END)

    

 
   
    actu=Button(frame,image=saveIcon,bg=color.white,command=lambda:actualizar(frame,configMenu))

    cerrar1=Button(frame,image=quitIcon,bg=color.white,command=lambda:configMenu.destroy())

    panelFrame=Frame(frame,bg="white")
    panelFrame.grid(row=1,column=1,padx=20,pady=10)
    cerrar=Button(panelFrame,image=quitIcon,bg=color.white,command=lambda:configMenu.destroy())
    cerrar.grid(row=0,column=0,padx=10,pady=3)

    buscar=Button(panelFrame,image=searchIcon,bg=color.white,command=lambda:BuscarPorNumero(actu,lf1,lf2,lf3,panelFrame,indice,cerrar1,urlLunes,urlMartes,urlMiercoles,urlJueves,urlViernes,urlSabado,urlDomingo))
    buscar.grid(row=0,column=2,padx=10,pady=3)
    

class lightThemeColors:
    white="white"
    horaLibreColor="lightblue"

color=lightThemeColors()



Tableframe=Frame(root,bg=color.white)
Tableframe.pack()
def table():
    try:
        conexion=sqlite3.connect("Horario")
        
        nombre=conexion.execute("SELECT * from HORARIO").fetchall()

        lista_tags = []

        for i in nombre:
            lista_tags.append(i)
        
        try:

            materia1=lista_tags[0]
            materia2=lista_tags[1]
            materia3=lista_tags[2]
            materia4=lista_tags[3]
            materia5=lista_tags[4]
            materia6=lista_tags[5]
            materia7=lista_tags[6]
            materia8=lista_tags[7]
            materia9=lista_tags[8]
            materia10=lista_tags[9]
            materia11=lista_tags[10]
            materia12=lista_tags[11]
            materia13=lista_tags[12]
            materia14=lista_tags[13]
        
        
            conexion.commit()
            conexion.close()
        except:
            messagebox.showerror("error fatal","ya te lo chingaste :( ")
            pass

        try:
            maxLimit=[len(materia1[2]),len(materia1[2]),
            len(materia1[2]),len(materia2[2]),len(materia3[2]),
            len(materia4[2]),len(materia5[2]),len(materia6[2]),
            len(materia7[2]),len(materia8[2]),len(materia9[2]),
            len(materia10[2]),len(materia11[2]),len(materia12[2]),
            len(materia13[2]),len(materia14[2])]

            maxLimintlenght=max(maxLimit)

            diasNombres=["Indice","Grupo","Materia","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
            cc=[3,8,maxLimintlenght,10,10,10,10,10,10,10]
     
            colores=["#C39BD3","#7FB3D5","#76D7C4","#F5B041","#F4D03F","#52BE80","#5DADE2","#F5B7B1","#D1F2EB","#EC7063"]
            fgcolores=["#C39BD3","#7FB3D5","#76D7C4","#CD6155","#D4AC0D","#52BE80","#2E86C1","#EC7063","#CD6155","#EC7063"]
            for i in range(NdiasABS):
                label=Label(Tableframe,text=diasNombres[i],width=8,height=2,bg=color.white,bd=0,activebackground="#d2f6c5",fg=fgcolores[i],highlightcolor= "red",font="comicSans 15")
                label.grid(row=2,column=i,padx=5,pady=5)


            for i in range(NdiasABS):
             
                if(materia1[i]==""):
                    button1=Button(Tableframe,text=materia1[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button1.grid(row=3,column=i,padx=5,pady=5)
                else:
                    button1=Button(Tableframe,text=materia1[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button1.grid(row=3,column=i,padx=5,pady=5)

                if(nMateriasValue<1):
                    button1.grid_forget()
            for i in range(NdiasABS):
                if(materia2[i]==""):
                    button2=Button(Tableframe,text=materia2[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button2.grid(row=4,column=i,padx=5,pady=5)
                else:
                    button2=Button(Tableframe,text=materia2[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button2.grid(row=4,column=i,padx=5,pady=5)

                if(nMateriasValue<2):
                    button2.destroy()
            for i in range(NdiasABS):
                if(materia3[i]==""):
                    button3=Button(Tableframe,text=materia3[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button3.grid(row=5,column=i,padx=5,pady=5)
                else:
                    button3=Button(Tableframe,text=materia3[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button3.grid(row=5,column=i,padx=5,pady=5)
                if(nMateriasValue<3):
                    button3.destroy()
            for i in range(NdiasABS):
                if(materia4[i]==""):
                    button4=Button(Tableframe,text=materia4[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button4.grid(row=6,column=i,padx=5,pady=5)
                else:
                    button4=Button(Tableframe,text=materia4[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button4.grid(row=6,column=i,padx=5,pady=5)

                if(nMateriasValue<4):
                    button4.destroy()
            for i in range(NdiasABS):
                if(materia5[i]==""):
                    button5=Button(Tableframe,text=materia5[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button5.grid(row=7,column=i,padx=5,pady=5)
                else:
                    button5=Button(Tableframe,text=materia5[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button5.grid(row=7,column=i,padx=5,pady=5)
                if(nMateriasValue<5):
                    button5.destroy()
            for i in range(NdiasABS):
                if(materia6[i]==""):
                    button6=Button(Tableframe,text=materia6[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button6.grid(row=8,column=i,padx=5,pady=5)
                else:
                    button6=Button(Tableframe,text=materia6[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button6.grid(row=8,column=i,padx=5,pady=5)

                if(nMateriasValue<6):
                    button6.destroy()
            
            for i in range(NdiasABS):
                if(materia7[i]==""):
                    button7=Button(Tableframe,text=materia7[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button7.grid(row=9,column=i,padx=5,pady=5)
                else:
                    button7=Button(Tableframe,text=materia7[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button7.grid(row=9,column=i,padx=5,pady=5)
                if(nMateriasValue<7):
                    button7.grid_forget()
            
            for i in range(NdiasABS):
                if(materia8[i]==""):
                    button8=Button(Tableframe,text=materia8[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button8.grid(row=10,column=i,padx=5,pady=5)
                else:
                    button8=Button(Tableframe,text=materia8[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button8.grid(row=10,column=i,padx=5,pady=5)

                if(nMateriasValue<8):
                    button8.destroy()
            
            for i in range(NdiasABS):
                if(materia9[i]==""):
                    button9=Button(Tableframe,text=materia9[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button9.grid(row=11,column=i,padx=5,pady=5)
                else:
                    button9=Button(Tableframe,text=materia9[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button9.grid(row=11,column=i,padx=5,pady=5)
                if(nMateriasValue<9):
                    button9.destroy()
            
            for i in range(NdiasABS):
                if(materia10[i]==""):
                    button10=Button(Tableframe,text=materia10[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button10.grid(row=12,column=i,padx=5,pady=5)
                else:
                    button10=Button(Tableframe,text=materia10[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button10.grid(row=12,column=i,padx=5,pady=5)

                if(nMateriasValue<10):
                    button10.destroy()
            for i in range(NdiasABS):
                if(materia11[i]==""):
                    button11=Button(Tableframe,text=materia11[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button11.grid(row=13,column=i,padx=5,pady=5)
                else:
                    button11=Button(Tableframe,text=materia11[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button11.grid(row=13,column=i,padx=5,pady=5)

                if(nMateriasValue<11):
                    button11.destroy()
            
            for i in range(NdiasABS):
                if(materia12[i]==""):
                    button12=Button(Tableframe,text=materia12[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button12.grid(row=14,column=i,padx=5,pady=5)
                else:
                    button12=Button(Tableframe,text=materia12[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button12.grid(row=14,column=i,padx=5,pady=5)

                if(nMateriasValue<12):
                    button12.destroy()
            for i in range(NdiasABS):
                if(materia13[i]==""):
                    button13=Button(Tableframe,text=materia13[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button13.grid(row=15,column=i,padx=5,pady=5)
                else:
                    button13=Button(Tableframe,text=materia13[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button13.grid(row=15,column=i,padx=5,pady=5)

                if(nMateriasValue<13):
                    button13.destroy()
         

            for i in range(NdiasABS):
                if(materia14[i]==""):
                    button14=Button(Tableframe,text=materia14[i],width=cc[i],height=1,bg="#95A5A6",bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button14.grid(row=16,column=i,padx=5,pady=5)
                else:
                    button14=Button(Tableframe,text=materia14[i],width=cc[i],height=1,bg=colores[i],bd=0,activebackground="#d2f6c5",fg="black",highlightcolor= "red")
                    button14.grid(row=16,column=i,padx=5,pady=5)
                if(nMateriasValue<14):
                    button14.destroy()
         
       
        except:
            pass
  
    except:
        pass

table()



def fichHelp():
    try:
        subprocess.Popen("notepad READ.me")
    except:
        os.system("kate READ.me")

#barra de ajustes
navBar=Menu(root,bg=color.white)
root.config(menu=navBar,width=300,height=300,bg=color.white)

configMenu=Menu(navBar,tearoff=0,bg=color.white)
configMenu.add_command(label="configurar tabla",command=initConfigMenuWindow)
configMenu.add_command(label="refrescar",command=refresh)
configMenu.add_command(label="salir",command=salir)

crearMateria=Menu(navBar,tearoff=0,bg=color.white)
crearMateria.add_command(label="editar Materia",command=nuevaMateria_view)

infoMenu=Menu(navBar,tearoff=0,bg=color.white)
infoMenu.add_command(label="información",command=fichHelp)

navBar.add_cascade(label="configuraciones",menu=configMenu)
navBar.add_cascade(label="configurar materias",menu=crearMateria)
navBar.add_cascade(label="información",menu=infoMenu)



bottomframe = Frame(root)
bottomframe.pack( side = RIGHT )
bottomframe.config(bg="white")

nma = Button(bottomframe,image=configIcon, bg=color.white,fg=color.white,command=nuevaMateria_view)
nma.pack( padx=10,pady=7,side =BOTTOM)

B = Frame(root)
B.pack( side =RIGHT)
B.config(bg="white")

blackbutton = Button(B,image=ajustarIcon, bg=color.white,fg=color.white,command=initConfigMenuWindow)
blackbutton.pack( padx=10,pady=7,side =LEFT)

Url=StringVar()
def time():

    hora=strftime('%H:%M:%S')
    Hourbtn.config(text ="Hora actual  "+hora) 
    Hourbtn.after(1000, time) 
    


NFrame= Frame(root)
NFrame.pack( side =LEFT)
NFrame.config(bg="white")


laaabel=StringVar()

labelNMateriasPerDay=Label(NFrame,text="",textvariable=laaabel, bg="white", fg="black",font="comicSans 12")


labelNMateriasPerDay.pack(padx=30,pady=7,side =RIGHT)



hourFrame= Frame(root)
hourFrame.pack( side =LEFT)
hourFrame.config(bg="white")

Hourbtn =Label(hourFrame,text="", bg="white",fg="black",font="comicSans 12")
Hourbtn.pack( padx=5,pady=7,side =RIGHT)



Urlf= Frame(root)
Urlf.pack( side =LEFT)
Urlf.config(bg="white")

UrlEntry=Entry(Urlf,width=23,bg="lightblue",fg="black",bd=1,textvariable=Url,font="calibri 11")
UrlEntry.pack( padx=30,pady=7,side =LEFT)
UrlEntry.delete(0,END)




selector(laaabel,Url,UrlEntry)

def rrr():
    root.destroy()
    try:
        subprocess.Popen("Eileen.exe")
    except:
        os.system("./Eileen")


def request():
    

    valor=messagebox.askquestion("Que puntual !","quieres ingresar a la reunión?")

    if valor=="yes":
         webbrowser.open(Url.get(), new=2, autoraise=True)




buttonRRR=Button(Urlf,image=refreshIcon,command=rrr,bg="white")
buttonRRR.pack(padx=5,pady=7,side =LEFT)

buttonRequest=Button(Urlf,image=refreshIcon,command=request,bg="white")
buttonRequest.pack(padx=5,pady=7,side =LEFT)

stringcaseUpper=Url.get()

vUpper=stringcaseUpper.upper()



def meetType():
    if(Url.get()==""):
        Url.set("sin url asignado")


    if("ZOOM" in vUpper):
       buttonRequest.config(image=zoomIcon)
    elif("MEET" in vUpper):
        buttonRequest.config(image=meetIcon)
    elif("TEAMS" in vUpper):
        buttonRequest.config(image=teamsIcon)
    else:
        buttonRequest.config(image=confDIcon)



meetType()
time()
root.mainloop()
