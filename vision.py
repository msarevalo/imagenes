import io
import os

from google.cloud import vision
from google.cloud.vision import types

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

raiz=Tk()

def desarrolla():
    messagebox.showinfo("Desarrolladores", "Manuel Santiago Arévalo Corredor\nMaria Alejandra Rojas Florez")

def salir():
    valor=messagebox.askokcancel("Salir", "¿Estas seguro que deseas salir de la aplicacion?")
    if valor:
        raiz.destroy()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir Archivo", filetypes=(("Imagenes", "*.jpg"), ("Imagenes", "*.png"), ("Imagenes", "*.jpeg")))
    print (fichero)

    client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
    	os.path.dirname (__file__),
    	'leon.jpg')
    with io.open (file_name,'rb') as image_file:
    	content = image_file.read()

    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print ("labels: ")

    texto=""
    for label in labels:
    	#print (label.description)
        texto=texto+label.description+"\n\n"

    messagebox.showinfo("Info Imagen", texto)


raiz.title("Analisis de Imagenes")
#raiz.geometry("500x500")
raiz.config(bg="#858585")
raiz.resizable(0,0)

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Abrir", command=abrefichero)
archivoMenu.add_command(label="Salir", command=salir)

acercaMenu=Menu(barraMenu, tearoff=0)
acercaMenu.add_command(label="Desarrolladores", command=desarrolla)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Acerca", menu=acercaMenu)


miFrame=Frame()
miFrame.pack(fill="both", expand="true")
miFrame.config(bg="#858585")
miFrame.config(width="300", height="150")

miLabel=Label(miFrame, text="Por favor ingresa\nuna imagen", bg="#858585", font=("Times News Roman",14), fg="white").place(x="75", y="10")

Button(raiz, text="Abrir Archivo", command=abrefichero).place(x="110", y="75")
Button(raiz, text="Salir", command=salir).place(x="130", y="110")


raiz.mainloop()

#from google.cloud import vision
#from google.cloud.vision import types

#client = vision.ImageAnnotatorClient()

#file_name = os.path.join(
	#os.path.dirname (__file__),
	#'leon.jpg')
#with io.open (file_name,'rb') as image_file:
	#content = image_file.read()

#image = types.Image(content=content)
#response = client.label_detection(image=image)
#labels = response.label_annotations
#print ("labels: ")

#for label in labels:
	#print (label.description)
