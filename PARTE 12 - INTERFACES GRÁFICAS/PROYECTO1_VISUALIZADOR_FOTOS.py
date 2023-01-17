from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("IMAGES\PYTHON.ico")
root.title("PROYECTO 1")

NUMERO_IMAGEN = 0

IMAGEN1 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA.png"))
IMAGEN2 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA2.png"))
IMAGEN3 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA3.png"))
IMAGEN4 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA4.png"))
IMAGEN5 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA5.png"))
IMAGEN6 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA6.png"))
IMAGEN7 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA7.png"))
IMAGEN8 = ImageTk.PhotoImage(Image.open("IMAGES\LIMA8.png"))

LISTA_IMAGEN=[IMAGEN1,IMAGEN2,IMAGEN3,IMAGEN4,IMAGEN5,IMAGEN6,IMAGEN7,IMAGEN8]

IMAGEN_LABEL = Label(image=IMAGEN1)
IMAGEN_LABEL.grid(row=0, column=0,columnspan=2)

def HACIA_ADELANTE():
    global NUMERO_IMAGEN
    global IMAGEN_LABEL
    global BOTON_ADELANTE
    global BOTON_ATRAS
    
    IMAGEN_LABEL.grid_forget()
    IMAGEN_LABEL = Label(image=LISTA_IMAGEN[NUMERO_IMAGEN+1])
    NUMERO_IMAGEN += 1
    
    BOTON_ADELANTE = Button(root, text="->",command=HACIA_ADELANTE)
    BOTON_ATRAS = Button(root, text="<-",command=HACIA_ATRAS)
    
    if NUMERO_IMAGEN==7:
        BOTON_ADELANTE = Button(root, text="->",state=DISABLED)
        
    IMAGEN_LABEL.grid(row=0, column=0,columnspan=2)
    BOTON_ADELANTE.grid(row=1,column=1)
    BOTON_ATRAS.grid(row=1,column=0)

    
    
def HACIA_ATRAS():
    global NUMERO_IMAGEN
    global IMAGEN_LABEL
    global BOTON_ADELANTE
    global BOTON_ATRAS

    IMAGEN_LABEL.grid_forget()
    IMAGEN_LABEL = Label(image=LISTA_IMAGEN[NUMERO_IMAGEN-1])
    NUMERO_IMAGEN -= 1
    
    BOTON_ADELANTE = Button(root, text="->",command=HACIA_ADELANTE)
    BOTON_ATRAS = Button(root, text="<-",command=HACIA_ATRAS)
    
    if NUMERO_IMAGEN==0:
        BOTON_ATRAS = Button(root, text="<-",state=DISABLED)
    
    IMAGEN_LABEL.grid(row=0, column=0,columnspan=2)
    BOTON_ADELANTE.grid(row=1,column=1)
    BOTON_ATRAS.grid(row=1,column=0)
    

BOTON_ADELANTE = Button(root, text="->",command=HACIA_ADELANTE)
BOTON_ATRAS = Button(root, text="<-",command=HACIA_ATRAS,state=DISABLED)

BOTON_ADELANTE.grid(row=1,column=1)
BOTON_ATRAS.grid(row=1,column=0)

root.mainloop()