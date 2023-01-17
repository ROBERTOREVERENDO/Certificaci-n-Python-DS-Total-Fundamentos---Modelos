from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")
root.geometry('400x500')

def HACER_CLICK():
    NUEVO_LABEL = Label(root, text= "NUEVO TEXTO AL CLICKEAR")
    NUEVO_LABEL.pack()

BOTON = Button(root, text="Clickear",command=HACER_CLICK)
BOTON.pack()

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()