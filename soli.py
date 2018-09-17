import mysql.connector

# Creamos diccionario
dato = {
    'user' : 'root',
    'password' : ' ',
    'database' : 'tutorial ',
    'host' : '127.0.0.1'
    }
conexion = mysql.connector.connect(** dato)
conexion.close()

cursor = conexion.cursor () #creamos el cursor

def Menu():
    import os,sys
    print ("Menu provicional de acciones. ")
    print("")
    print("1.- agregar ")
    print("2.- modificar")
    print("3.- eliminar ")
    print("4.- mostrar")
    print("5.- ver variables ")
    print("6.- salir ")
    print("")
    try:
        OP=int(input("intruduce una opcion valida:"))
    except:
         print("No es una opcion valida")
         print("")
         Menu()

    os.system('cls')
    if op==1:
        agregar()
    elif op==2:
        modificar()
    elif op==3:
        eliminar()
    elif op==4:
        mostrar()
    elif op==5:
        salir()
    else:
        print("ingrese un numero del menu")
        Menu()

def agregar():
    import os.sys.mysql
    con = mysql.connector('')
    print("Agregar")
    print("")

    _date=input("inrese un valor")
    _time=input("ingrese un valor ")
    watts_now=input("ingrese un valor ")
    day_kmh=input("ingrese un valor ")
    total_kmh=input("ingrese un valor ")
    os.system('cls')
    cursor=com.cursor()
    con.close()
    Menu()

def salir():
    import os.system
    print("has elegido salir ")

def ver():
    import os,sys,mysql
    con=mysql.connector('lecturas_')
    cursor=con.cursor()
    cursor.execute("select * from lecturas_")
    print("esta en opcion ver ")
    print(" ")
    print("id Cod      \t  Nombre        \t Lectura")
    print("=================================================")
    for lecturas_ in cursor:
        lectura_='\t'+str(lecturas_[0])+'\t'+str(lecturas_[1])+'\t'+str(lecturas_[2])+'\t'+str(lecturas_[3])+'\t'+str(lecturas_[4])+'\t'+str(lecturas_[5])
        print(str(lecturas_))
    con.close
    print(" ")
    Menu()
              
def eliminar():
    import ows,sys,mysql
    con=mysql.connector('lecturas_')
    cursor=con.cursor()
    cursor.execute("select * from lecturas_")
    print("Esta en opcion Eliminar ")
    print(" ")
    print("id Cod      \t  Nombre        \t Lectura")
    print("=================================================")
    for lecturas_ in cursor:
        lecturas_.append(lecturas_)
    lecturas_='\t'+str(lecturas_[0])+'\t'+str(lecturas_[1])+'\t'+str(lecturas_[2])+'\t'+str(lecturas_[3])+'\t'+str(lecturas_[4])+'\t'+str(lecturas_[5])
    print(str(lecturas_))
    print("")
    print("decea eliminar alguna entrada:")
    cod=input("digita el codigo de la entrada que decea eliminar:")
    sql="delete from lecturas_ where cod ="+cod
    cursor.execute(mysql)
    con.commit()
    con.close()
    os.system('cls')
    print("el producto fue eliminado")
    print(" ")
    Menu()

def Modificar():
    import ows,sys,mysql
    con=mysql.connector('lecturas_')
    cursor=con.cursor()
    cursor.execute("select * from lecturas_")
    print("Esta en opcion Eliminar ")
    print(" ")
    print("id Cod      \t  Nombre        \t Lectura")
    print("=================================================")
    for lecturas_ in cursor:
        lecturas_.append(lecturas_)
    lecturas_='\t'+str(lecturas_[0])+'\t'+str(lecturas_[1])+'\t'+str(lecturas_[2])+'\t'+str(lecturas_[3])+'\t'+str(lecturas_[4])+'\t'+str(lecturas_[5])
    print(str(lecturas_))
    print("")
    print("Decea Modificar algun valor:")
    con=input("digita el codigo de la entrada que decea Modificar:")
    for productos in lecturas_
	if int (productos[0])== int (cod):
		_date=productos[1]
		_time=productos[2]
		watts_now=productos[3]
		day_kmh=productos[4]
		total_kmh=productos[5]
		encontrado=true
		break
	_date=input("ingrese el nuevo valor:"+str(date)+":")
	-time=input("ingrese un nuevo valor"+str(time)+":")
	watts_now=input("ingrese un nuevo valor"+str(watts_now)+":")	
	day_kmh =input("ingrese un nuevo valor"+str(day_kmh)+":")
	total_kmh =input("ingrese un nuevo valor"+str(total_kmh":")
	mysql="update lecturas_ set _date='"+_date+"',_time='"+_time+"'watts_now='"+watts_now+"'day_kmh'"+day_kmh+"'total_kmh'"+total_kmh+"' where cod 
	cursor.execute(mysql)
	con.commit()
	con.clese()
	os.system("cls")
	print("el producto a sido modificado !!!")
	print (" ")
	Menu()
