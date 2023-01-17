from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")
root.geometry("500x500")

TEXTO = Text(root, width=50, height=10, font=("Calibri",15))
TEXTO.pack()

FRAME = Frame(root)
FRAME.pack()

def BLANQUEAR():
    TEXTO.delete(1.0,"end")

def COPIAR():
    LABEL = Label(root, text = TEXTO.get(1.0,"end"))
    TEXTO.delete(1.0,"end")
    LABEL.pack()


BOTON_BLANQUEAR = Button(FRAME, text="BLANQUEAR CAJA", command=BLANQUEAR)
BOTON_BLANQUEAR.grid(row=0,column=0,padx=50,pady=20)
BOTON_COPIAR = Button(FRAME, text="COPIAR CAJA", command=COPIAR)
BOTON_COPIAR.grid(row=0,column=1,padx=50,pady=20)

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()