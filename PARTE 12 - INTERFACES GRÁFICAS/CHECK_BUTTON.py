from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")
root.geometry('400x300')

PEDIDO = StringVar()
GASEOSA =  StringVar()
AJI = StringVar()
PARALLEVAR =  StringVar()

CHECK1 = Checkbutton(root,text="¿Agrandar pedido?",variable=PEDIDO, onvalue= "Pedido: Grande", offvalue= "Pedido: Regular")
CHECK2 = Checkbutton(root,text="¿Agrandar gaseosa?",variable=GASEOSA, onvalue= "Gaseosa: Grande", offvalue= "Gaseosa: Regular")
CHECK3 = Checkbutton(root,text="¿Con ají?",variable=AJI, onvalue= "Con ají", offvalue= "Sin ají")
CHECK4 = Checkbutton(root,text="¿Para llevar?",variable=PARALLEVAR, onvalue= "Para llevar", offvalue= "Para comer aquí")

CHECK1.deselect()
CHECK2.deselect()
CHECK3.deselect()
CHECK4.deselect()

CHECK1.pack(anchor="w")
CHECK2.pack(anchor="w")
CHECK3.pack(anchor="w")
CHECK4.pack(anchor="w")

def MOSTRAR():
    LABEL.config(text= PEDIDO.get() + "\n" + GASEOSA.get() + "\n" + AJI.get() + "\n" + PARALLEVAR.get())

BOTON = Button(root, text="Generar pedido",command=MOSTRAR).pack(anchor="w")
LABEL = Label(root,text="")
LABEL.pack(anchor="w")

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()