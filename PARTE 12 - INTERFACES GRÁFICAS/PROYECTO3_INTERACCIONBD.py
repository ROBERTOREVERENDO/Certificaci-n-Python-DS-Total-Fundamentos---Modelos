from tkinter import *
import sqlite3


root = Tk()
root.iconbitmap("IMAGES\PYTHON.ico")
root.title("PROYECTO 3")

CONEXION = sqlite3.connect("PROYECTO3.db")
CURSOR = CONEXION.cursor()

# CURSOR.execute("""
#                CREATE TABLE PERSONA(
#                  ID integer PRIMARY KEY AUTOINCREMENT,
#                  Nombre varchar(50),
#                  Apelido varchar(50),
#                  Direccion varchar(100),
#                  Edad integer,
#                  EC char(1)
#                )
#                """)

CONEXION.commit()
CONEXION.close()

def GUARDAR():
    CONEXION = sqlite3.connect("PROYECTO3.db")
    CURSOR = CONEXION.cursor()   
    
    CURSOR.execute("INSERT INTO PERSONA VALUES(null , :NOMBRE , :APELLIDO , :DIRECC , :EDAD , :EC)",
                  {
                   "NOMBRE":E_NOMBRE.get(),
                   "APELLIDO":E_APELLIDO.get(),
                   "DIRECC":E_DIRECCION.get(),
                   "EDAD":E_EDAD.get(),
                   "EC":E_EC.get()
                  })
    
    CONEXION.commit()
    CONEXION.close()  
    
    E_NOMBRE.delete(0, END)
    E_APELLIDO.delete(0, END)
    E_DIRECCION.delete(0, END)
    E_EDAD.delete(0, END)
    E_EC.delete(0, END)
    

def MOSTRAR():
    CONEXION = sqlite3.connect("PROYECTO3.db")
    CURSOR = CONEXION.cursor()  
    
    CURSOR.execute("SELECT * FROM PERSONA")
    REGISTROS = CURSOR.fetchall()
    
    IMPRIMIR = ""
    
    for X in REGISTROS:
        IMPRIMIR = IMPRIMIR + str(X[0]) + "-" + str(X[1]) + " " +  str(X[2])  + "-" + str(X[4]) + "años" + "\n"
        
    CONSULTA = Label(root,text = IMPRIMIR)
    CONSULTA.grid(row=9,column=0,columnspan=2)
                  
    CONEXION.commit()
    CONEXION.close()  
    
def ELIMINAR():
    CONEXION = sqlite3.connect("PROYECTO3.db")
    CURSOR = CONEXION.cursor()      
    
    CURSOR.execute("DELETE FROM PERSONA WHERE ID = :IDN",
                  {
                   "IDN":E_ELIMINAR.get()
                  })
    
    E_ELIMINAR.delete(0, END)
    
    CONEXION.commit()
    CONEXION.close()  
    
    
def BOTON_MODIF():
    CONEXION = sqlite3.connect("PROYECTO3.db")
    CURSOR = CONEXION.cursor()  
    
    CURSOR.execute("""
                   UPDATE PERSONA 
                   SET Nombre = :NOMBRE,Apelido = :APELLIDO, Direccion = :DIRECC, Edad = :EDAD , EC = :EC
                   WHERE ID = :IDN
                   
                   """,
                   {
                   "NOMBRE":EDITAR_E_NOMBRE.get(),
                   "APELLIDO":EDITAR_E_APELLIDO.get(),
                   "DIRECC":EDITAR_E_DIRECCION.get(),
                   "EDAD":EDITAR_E_EDAD.get(),
                   "EC":EDITAR_E_EC.get(),
                   "IDN":E_EDITAR.get()
                   })
                  
    EDIT_root.destroy()
    E_EDITAR.delete(0,END)
    
    CONEXION.commit()
    CONEXION.close()  
    
    
    
def EDITAR():
    CONEXION = sqlite3.connect("PROYECTO3.db")
    CURSOR = CONEXION.cursor() 
        
    global EDITAR_E_NOMBRE
    global EDITAR_E_APELLIDO
    global EDITAR_E_DIRECCION
    global EDITAR_E_EDAD
    global EDITAR_E_EC
    global EDIT_root
    
    CURSOR.execute("SELECT * FROM PERSONA WHERE ID = :IDN",
                  {
                    "IDN":E_EDITAR.get()
                  })
    REGISTRO_EDITAR = CURSOR.fetchone()
    
    
    EDIT_root = Tk()
    EDIT_root.iconbitmap("IMAGES\PYTHON.ico")
    EDIT_root.title("MODIFICAR REGISTRO")  
    
    EDITAR_NOMBRE = Label(EDIT_root, text="NOMBRE:").grid(row=0,column=0,sticky="w")
    EDITAR_APELLIDO = Label(EDIT_root, text="APELLIDO:").grid(row=1,column=0,sticky="w")
    EDITAR_DIRECCION = Label(EDIT_root, text="DIRECCION:").grid(row=2,column=0,sticky="w")
    EDITAR_EDAD = Label(EDIT_root, text="EDAD:").grid(row=3,column=0,sticky="w")
    EDITAR_EC = Label(EDIT_root, text="ESTADO CIVIL:").grid(row=4,column=0,sticky="w")

    EDITAR_E_NOMBRE = Entry(EDIT_root,width=40)
    EDITAR_E_NOMBRE.grid(row=0, column = 1)
    EDITAR_E_NOMBRE.insert(0,REGISTRO_EDITAR[1])

    EDITAR_E_APELLIDO = Entry(EDIT_root,width=40)
    EDITAR_E_APELLIDO.grid(row=1, column = 1)
    EDITAR_E_APELLIDO.insert(0,REGISTRO_EDITAR[2])
    
    EDITAR_E_DIRECCION = Entry(EDIT_root,width=40)
    EDITAR_E_DIRECCION.grid(row=2, column = 1)
    EDITAR_E_DIRECCION.insert(0,REGISTRO_EDITAR[3])

    EDITAR_E_EDAD = Entry(EDIT_root,width=40)
    EDITAR_E_EDAD.grid(row=3, column = 1)
    EDITAR_E_EDAD.insert(0,REGISTRO_EDITAR[4])

    EDITAR_E_EC = Entry(EDIT_root,width=40)
    EDITAR_E_EC.grid(row=4, column = 1)
    EDITAR_E_EC.insert(0,REGISTRO_EDITAR[5])
    
    EDITAR2 = Button(EDIT_root,text="GUARDAR MODIFICACIONES",width=35,command = BOTON_MODIF).grid(row=5,column =1,columnspan=2)
    
    
    
    EDIT_root.mainloop()
    
    CONEXION.commit()
    CONEXION.close()  
    
    
    
    
    
    
NOMBRE = Label(root, text="NOMBRE:").grid(row=0,column=0,sticky="w")
APELLIDO = Label(root, text="APELLIDO:").grid(row=1,column=0,sticky="w")
DIRECCION = Label(root, text="DIRECCION:").grid(row=2,column=0,sticky="w")
EDAD = Label(root, text="EDAD:").grid(row=3,column=0,sticky="w")
EC = Label(root, text="ESTADO CIVIL:").grid(row=4,column=0,sticky="w")

E_NOMBRE = Entry(root,width=40)
E_NOMBRE.grid(row=0, column = 1)

E_APELLIDO = Entry(root,width=40)
E_APELLIDO.grid(row=1, column = 1)

E_DIRECCION = Entry(root,width=40)
E_DIRECCION.grid(row=2, column = 1)

E_EDAD = Entry(root,width=40)
E_EDAD.grid(row=3, column = 1)

E_EC = Entry(root,width=40)
E_EC.grid(row=4, column = 1)

GUARDAR = Button(root,text="GUARDAR REGISTRO",width=35,command = GUARDAR).grid(row=5,column =0, columnspan=2)
MOSTRAR = Button(root,text="MOSTRAR REGISTROS",width=35, command = MOSTRAR).grid(row=6,column =0, columnspan=2)

E_EDITAR = Entry(root,width=20)
E_EDITAR.grid(row=7, column = 0)

E_ELIMINAR = Entry(root,width=20)
E_ELIMINAR.grid(row=8, column = 0)

EDITAR = Button(root,text="EDITAR REGISTRO",width=35,command = EDITAR).grid(row=7,column =1)
ELIMINAR = Button(root,text="ELIMINAR REGISTRO",width=35, command = ELIMINAR).grid(row=8,column =1)

CONSULTA = Label(root).grid(row=9,column=0,columnspan=2)

root.mainloop()