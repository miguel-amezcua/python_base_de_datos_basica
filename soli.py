#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os
import sys
import time

def Menu():
     print ("Menu provicional de acciones. ")
     print("")
     print("1.- agregar ")
     print("2.- modificar")
     print("3.- eliminar ")
     print("4.- mostrar")
     print("5.- salir ")
     print("")
     try:
         op=int(input("intruduce una opcion valida:"))
     except:
         print("No es una opcion valida")
         print("")
         Menu()

     os.system('cls')
     if op==1:
         Agregar()
     elif op==2:
         Modificar()
     elif op==3:
         Eliminar()
     elif op==4:
         Mostrar()
     elif op==5:
         Salir()
     else:
         print("ingrese un numero del menu")
         Menu()

def Mostrar():
    conn = sqlite3.connect(r"C:\Users\practicas3.jalisco\Desktop\db2\mynewdb.db")
    cursor = conn.cursor()
    print ("esto indica que nos conectamos""\n") 
    a=cursor.execute("select id_lecturas, __date, _time, watts_now, day_kmh, total_kmh FROM lecturas__")
    print(" ")
    print("\tid Cod \t  fecha  \t Hora    watts \t lect/dia  total_kmh ")
    print("\t==============================================================")
    for lecturas_ in cursor:
        #print("esto indica que a mediados estoy bien ")
        lecturas_='\t'+str(lecturas_[0])+'\t'+str(lecturas_[1])+'\t'+str(lecturas_[2])+'\t'+str(lecturas_[3])+'   \t '+str(lecturas_[4])+'\t\t'+str(lecturas_[5])
        print (str(lecturas_))
    conn.commit()
    cursor.close()
    conn.close()
    print ("\n")
   
    time.sleep(7)
    os.system('clear')
    Menu()

def Agregar():
    conn = sqlite3.connect(r"C:\Users\practicas3.jalisco\Desktop\db2\mynewdb.db")
    cursor = conn.cursor()
    print("Opcion Agregar")
    print("\n")
    __date=input("Ingrese un valor para fecha: ")
    _time=input("Ingrese un valor para hora: ")
    watts_now=int(input("Ingrese un valor: "))
    day_kmh=int(input("Ingrese un valor consumo: "))
    total_kmh=int(input("Ingrese un valor total medido: "))
    sentencia = "insert into lecturas__(__date, _time, watts_now, day_kmh, total_kmh)values(?,?,?,?,?)"
    cursor.execute(sentencia, [__date, _time, watts_now, day_kmh, total_kmh])
    print ("Datos guardados correctamente")

    os.system('cls')
    conn.commit()
    cursor.close()
    conn.close()
    
    print ("\n")
    time.sleep(3)
    os.system('clear')
    Menu()
    
def Eliminar():
    conn = sqlite3.connect(r"C:\Users\practicas3.jalisco\Desktop\db2\mynewdb.db")
    cursor = conn.cursor()
    cursor.execute("select * from lecturas__")
    print("Esta en opcion Eliminar ")
    print(" ")
    print("\tid Cod \t  fecha  \t Hora    watts \t lect/dia  total_kmh ")
    print("\t==============================================================")
    for lecturas_ in cursor:
        #print("esto indica que a mediados estoy bien ")
        lecturas_='\t'+str(lecturas_[0])+'\t'+str(lecturas_[1])+'\t'+str(lecturas_[2])+'\t'+str(lecturas_[3])+'   \t '+str(lecturas_[4])+'\t\t'+str(lecturas_[5])
        print (str(lecturas_))
    print("")
    print("Decea eliminar alguna entrada:")
    cod=input("digita el codigo de la entrada que decea eliminar:")
    sentencia="delete from lecturas__ where id_lecturas = ?; "
    cursor.execute(sentencia, [cod])
    print ("la entrafa fue eliminada ")
    conn.commit()
    cursor.close()
    conn.close()
    print ("\n")
    time.sleep(2)
    os.system('clear')
    Menu()

def Modificar():
    info=[]
    conn = sqlite3.connect(r"C:\Users\practicas3.jalisco\Desktop\db2\mynewdb.db")
    cursor = conn.cursor()
    cursor.execute("select * from lecturas__")
    print("Esta en opcion Eliminar ")
    print(" ")
    print("\tid Cod \t  fecha  \t Hora    watts \t lect/dia  total_kmh ")
    print("\t==============================================================")
    for lecturas__ in cursor:
        info.append(lecturas__)
        #print("esto indica que a mediados estoy bien ")
        lecturas__='\t'+str(lecturas__[0])+'\t'+str(lecturas__[1])+'\t'+str(lecturas__[2])+'\t'+str(lecturas__[3])+'   \t '+str(lecturas__[4])+'\t\t'+str(lecturas__[5])
        print (str(lecturas__))
    print("")
    print("Decea Modificar algun valor:")
    cod=input("digita el codigo de la entrada que decea Modificar:")
    for lecturas__ in info:
        if int(lecturas__[0])== int (cod):
                __date=lecturas__[1]
                _time=lecturas__[2]
                watts_now=lecturas__[3]
                day_kmh=lecturas__[4]
                total_kmh=lecturas__[5]
                encontrado=True
        break
    __date=input("ingrese el nuevo valor:")
    _time=input("ingrese un nuevo valor:")
    watts_now=input("ingrese un nuevo valor:")
    day_kmh =input("ingrese un nuevo valor:")
    total_kmh =input("ingrese un nuevo valor:")
    sentencia="update lecturas__ set __date='"+__date+"',_time='"+_time+"',watts_now='"+watts_now+"',day_kmh='"+day_kmh+"',total_kmh='"+total_kmh+"' where id_lecturas =?"
    cursor.execute(sentencia, [cod])
    print ("el producto fue modificado")
    conn.commit()
    cursor.close()
    conn.close()
    print ("\n")
    time.sleep(2)
    os.system('clear')
    Menu()

def Salir():
    print("has elegido salir ") 
     
Menu()

