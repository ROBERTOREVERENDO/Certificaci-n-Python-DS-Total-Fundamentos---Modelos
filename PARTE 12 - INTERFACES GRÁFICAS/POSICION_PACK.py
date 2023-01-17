from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")

LABEL1 = Label(root, text="LABEL1").pack()
LABEL2 = Label(root, text="LABEL2").pack()
ENTRY = Entry(root).pack()
BOTON1 = Button(root,text="BOTON1").pack()

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()