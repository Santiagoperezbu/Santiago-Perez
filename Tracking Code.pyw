import tkinter as tk
from tkinter import messagebox
    
def cerrar():
    ventana.withdraw()
 
def Datos_subidos():
    ventana1=tk.Tk()
    ventana1.title("Datos Subidos")
    ventana1.geometry("250x200")
    ventana1.configure(background="white")
    d=tk.Label(ventana1,text="!Datos Subidos¡",bg="white",fg="green",font=(50))
    d.pack(padx=20,pady=20)
    boton1=tk.Button(ventana1,text="Seguir",fg="blue",command=ventana1.destroy)
    boton1.pack(side=tk.TOP)
    d=tk.Label(ventana1,text="",bg="white",fg="black",font=(10))
    d.pack(padx=5,pady=5)
    boton2=tk.Button(ventana1,text="Cerrar",fg="red",command=cerrar)
    boton2.pack(side=tk.TOP)

def escribir_datos():
    nt=NomA.get()+'.txt'
    cap=open(nt,"w")
    cap.write("INICIAMOS")
    cap.close()
    cap = open(nt,'r')
    linea=cap.readlines()
    cap.close()
    cap=open(nt,"w")
    for i in linea:
        cap.write("[Tipo de pez: "+ Tipo_pez.get()+']')
        cap.write("[NUM.LOTE: "+ N_Lote.get()+']')
        cap.write("[Se le aplico antioxidante: "+ Cal.get()+']')
        cap.write("[Empacado por: "+ Nom_emp.get()+']')
        cap.write("[Se pesco en el puerto: "+ Puerto.get()+']')
        cap.write("[Se pesco a las :"+HE.get()+']')
        cap.write("[Salio de la empacadora a las: "+ HS.get()+']')
        cap.write("[Mar o Rio en el que se pesco: "+ MoR.get()+']')
        cap.write("[Mapa de coordenadas de puertos pesqueros de el Golfo de California: https://drive.google.com/open?id=1Zgtl8_twUt7kjva_cFR0wGMfa4Edriru&usp=sharing"+']')
        Datos_subidos()
    cap.close()
        
    def codigoqr(a,b):
        import qrcode
        from PIL import Image 
        cadena = open(a,'r')
        nombre=cadena.readlines()
        cadena.close()
        imagen = qrcode.make(nombre)
        nombre_imagen = ( b + '.png')
        archivo_imagen = open(nombre_imagen,'wb')
        imagen.save(archivo_imagen)
        archivo_imagen.close()
        ruta_imagen = './'+nombre_imagen
        Image.open(ruta_imagen).show()
    codigoqr(nt,NomA.get())


ventana=tk.Tk()
ventana.title("TRACKING FISH")
ventana.geometry("800x1200")
ventana.configure(background="white")
ventana.iconbitmap("Logo_HG1.ico")



image=tk.PhotoImage(file="Logo_HG1.gif")
image=image.subsample(4,3)
label=tk.Label(ventana,image=image,bg="white")
label.place(x=0,y=0,relwidth=1.0,relheight=1.0)
label.pack(fill=tk.Y,side=tk.LEFT)

e1=tk.Label(ventana,text="-TRACKING FISH-",bg="white",fg="black",font=(50))
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)

e1=tk.Label(ventana,text="Ingresa el tipo de pez: ",bg="white",fg="blue",font=(35))
e1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
Tipo_pez=tk.Entry(ventana)
Tipo_pez.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Ingresa numero de lote: ",bg="white",fg="blue",font=(35))
e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
N_Lote=tk.Entry(ventana)
N_Lote.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

eG=tk.Label(ventana,text="Ingresa el nombre del archivo: ",bg="white",fg="blue",font=(35))
eG.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
NomA=tk.Entry(ventana)
NomA.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)


e23=tk.Label(ventana,text="Se le agrego acido lipoico insaturado antioxidante: ",bg="white",fg="blue",font=(35))
e23.pack(padx=5,pady=5,ipadx=5,ipady=5)
Cal=tk.Entry(ventana)
Cal.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e3=tk.Label(ventana,text="Ingresa el nombre de la empacadora: ",bg="white",fg="blue",font=(35))
e3.pack(padx=5,pady=5,ipadx=5,ipady=5)
Nom_emp=tk.Entry(ventana)
Nom_emp.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e4=tk.Label(ventana,text="Ingresa el nombre del puerto: ",bg="white",fg="blue",font=(35))
e4.pack(padx=5,pady=5,ipadx=5,ipady=5)
Puerto=tk.Entry(ventana)
Puerto.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e4=tk.Label(ventana,text="Ingresa la hora de entra del pez a la empacadora: ",bg="white",fg="blue",font=(35))
e4.pack(padx=5,pady=5,ipadx=5,ipady=5)
HE=tk.Entry(ventana)
HE.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e5=tk.Label(ventana,text="Ingresa la hora de salida del pez a la empacadora: ",bg="white",fg="blue",font=(35))
e5.pack(padx=5,pady=5,ipadx=5,ipady=5)
HS=tk.Entry(ventana)
HS.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e6=tk.Label(ventana,text="Ingrese el mar o rio donde se pezco: ",bg="white",fg="blue",font=(35))
e6.pack(padx=5,pady=5,ipadx=5,ipady=5)
MoR=tk.Entry(ventana)
MoR.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

boton=tk.Button(ventana,text="Subir Datos",fg="blue",command=escribir_datos)
boton.pack(side=tk.TOP)