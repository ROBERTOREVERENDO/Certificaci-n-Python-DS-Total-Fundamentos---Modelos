from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")

LABEL = Label(root, text="HOLA").grid(row=4,column=5)
LABEL2 = Label(root, text="CHAU").grid(row=1,column=1)
LABEL3 = Label(root, text="XYZ").grid(row=2,column=3)

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()