from tkinter import *
import math


root = Tk()
root.iconbitmap("IMAGES\PYTHON.ico")
root.title("PROYECTO 2")

def ESCRIBIR(CARACTER):
    global TEXTO
    global OPERACION
    
    OPERACION = OPERACION + str(CARACTER)
    
    TEXTO = Text(root, height = 2, width = 40)
    TEXTO.grid(row=0,column=0, columnspan=4)
    
    TEXTO.delete(1.0,"end")
    TEXTO.insert(1.0,OPERACION)
    
def BORRAR():
    TEXTO.delete(1.0,"end")
    OPERACION = ""
    
def RESOLVER():
    global TEXTO
    global OPERACION
    
    try:
        SOLUCION = eval(str(OPERACION))
        TEXTO.delete(1.0,"end")
        OPERACION = ""
        TEXTO.insert(1.0,SOLUCION)
    except:
        OPERACION = ""
        TEXTO.delete(1.0,"end")
        TEXTO.insert(1.0,"Syntax ERROR")       
    

TEXTO = Text(root, height = 2, width = 40).grid(row=0,column=0, columnspan=4)
BOTON_BORRAR = Button(root, text="BORRAR",height = 2, width = 10,command = BORRAR).grid(row=0,column=4)

OPERACION = ""

BOTON_7 = Button(root, text="7" ,height = 2, width = 10,command=lambda: ESCRIBIR("7")).grid(row=1,column=0)
BOTON_8 = Button(root, text="8" ,height = 2, width = 10,command=lambda: ESCRIBIR("8")).grid(row=1,column=1)
BOTON_9 = Button(root, text="9" ,height = 2, width = 10,command=lambda: ESCRIBIR("9")).grid(row=1,column=2)
BOTON_MAS = Button(root, text="+" ,height = 2, width = 10,command=lambda: ESCRIBIR("+")).grid(row=1,column=3)
BOTON_P1 = Button(root, text="(" ,height = 2, width = 10,command=lambda: ESCRIBIR("(")).grid(row=1,column=4)

BOTON_4 = Button(root, text="4" ,height = 2, width = 10,command=lambda: ESCRIBIR("4")).grid(row=2,column=0)
BOTON_5 = Button(root, text="5" ,height = 2, width = 10,command=lambda: ESCRIBIR("5")).grid(row=2,column=1)
BOTON_6 = Button(root, text="6" ,height = 2, width = 10,command=lambda: ESCRIBIR("6")).grid(row=2,column=2)
BOTON_MENOS = Button(root, text="-" ,height = 2, width = 10,command=lambda: ESCRIBIR("-")).grid(row=2,column=3)
BOTON_P2 = Button(root, text=")" ,height = 2, width = 10,command=lambda: ESCRIBIR(")")).grid(row=2,column=4)

BOTON_1 = Button(root, text="1" ,height = 2, width = 10,command=lambda: ESCRIBIR("1")).grid(row=3,column=0)
BOTON_2 = Button(root, text="2" ,height = 2, width = 10,command=lambda: ESCRIBIR("2")).grid(row=3,column=1)
BOTON_3 = Button(root, text="3" ,height = 2, width = 10,command=lambda: ESCRIBIR("3")).grid(row=3,column=2)
BOTON_POR = Button(root, text="*" ,height = 2, width = 10,command=lambda: ESCRIBIR("*")).grid(row=3,column=3)
BOTON_POT = Button(root, text="**" ,height = 2, width = 10,command=lambda: ESCRIBIR("**")).grid(row=3,column=4)

BOTON_0 = Button(root, text="0" ,height = 2, width = 10,command=lambda: ESCRIBIR("0")).grid(row=4,column=0)
BOTON_PUNTO = Button(root, text="." ,height = 2, width = 10,command=lambda: ESCRIBIR(".")).grid(row=4,column=1)
BOTON_IGUAL = Button(root, text="=" ,height = 2, width = 10,command = RESOLVER).grid(row=4,column=2)
BOTON_ENTRE = Button(root, text="/" ,height = 2, width = 10,command=lambda: ESCRIBIR("/")).grid(row=4,column=3)
BOTON_RAIZ = Button(root, text="Raíz" ,height = 2, width = 10,command=lambda: ESCRIBIR("math.sqrt(")).grid(row=4,column=4)

root.mainloop()