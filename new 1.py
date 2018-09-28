#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

from  tkinter import *
from  tkinter import messagebox


raiz= Tk()

def infoAdicional():
    messagebox.showinfo("medidor de energia portatil","Hecho para ejecutar en raspberry")

def avisolicencia():
    messagebox.showwarning("Licencia", "CIATEQ, Miguel Angel Amezcua Ponce")

def salirAplicacion():
    valor=messagebox.askquestion("salir","decea salir de la palicacion???")
    if valor =="yes":
            raiz.destroy()
            
def cerrardocumento():
    valor=messagebox.askretrycancel("Reintentar","no es posible conectar con la base de datos ")
    if valor =="false":
            conn = sqlite3.connect(r"C:\Users\practicas3.jalisco\Desktop\db2\mynewdb.db")

                           
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=50, height=50)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como ")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir" ,command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="copiar")
archivoEdicion.add_command(label="cortar")
archivoEdicion.add_command(label="pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="base de datos", command=cerrardocumento) 

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command (label="Licencia", command=avisolicencia)
archivoAyuda.add_command (label="Acerca de ...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

miframe=Frame(raiz, bg='green', width=800, height=800)
miframe.pack()

golpeanpc=PhotoImage(file="computadora.gif")
Label(miframe, image=golpeanpc).grid(rowspan=5, column= 4)

cuadronombre=Entry(miframe)
cuadronombre.grid(row=0, column=1, padx=10,pady=10)
cuadronombre.config(fg="blue", justify="right")

cuadropass=Entry(miframe)
cuadropass.grid(row=1, column=1, padx=10,pady=10)
cuadropass.config(show="*", fg="red", )

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=2, column=1, padx=10,pady=10)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=3, column=1, padx=10,pady=10)

cuadrotel=Entry(miframe)
cuadrotel.grid(row=4, column=1, padx=10,pady=10)

nombrelabel=Label(miframe, text="Nombre:")
nombrelabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passlabel=Label(miframe, text="Password:")
passlabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidolabel=Label(miframe, text="Apellido:")
apellidolabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miframe, text="Direccion:")
direccionlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

telefonolabel=Label(miframe, text="Telefono:")
telefonolabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()
