from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")

LABEL = Label(root, text="HOLA")
LABEL.pack(side='left')

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()
