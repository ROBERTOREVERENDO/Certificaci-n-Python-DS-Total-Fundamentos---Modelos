from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")
root.geometry('500x600')

LABEL1 = Label(root,text="Nombre:")
LABEL1.grid(row=0,column=0,sticky='w')

LABEL2 = Label(root,text="Apellido:")
LABEL2.grid(row=1,column=0,sticky='w')

LABEL3 = Label(root,text="Edad:")
LABEL3.grid(row=2,column=0,sticky='w')


ENTRY1 = Entry(root)
ENTRY1.grid(row=0,column=1,sticky='w')

ENTRY2 = Entry(root)
ENTRY2.grid(row=1,column=1,sticky='w')

ENTRY3 = Entry(root)
ENTRY3.grid(row=2,column=1,sticky='w')


def SALUDAR():
    TEXTO = "Hola, soy " + ENTRY1.get() + " " + ENTRY2.get() + "\ntengo " + ENTRY3.get() + " años"
    LABEL4 = Label(root, text=TEXTO)
    LABEL4.grid(row=4,column=0,sticky='w',columnspan = 2)


BOTON = Button(root, text="Saludar" , command =SALUDAR, width = 24)
BOTON.grid(row=3,column=0,sticky='w',columnspan = 2)

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()