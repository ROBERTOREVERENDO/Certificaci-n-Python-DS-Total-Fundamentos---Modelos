from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")

LABEL1 = Label(root, text="LABEL1").grid(row=0,column=0)
LABEL2 = Label(root, text="LABEL2").grid(row=0,column=1)
ENTRY = Entry(root).grid(row=1,column=0)
BOTON1 = Button(root,text="BOTON1").grid(row=1,column=1)
LABEL3 = Label(root, text="LABEL3").grid(row=1,column=2)

BOTON2 = Button(root,text="BOTON1--------------------------------").grid(row=2,column=0,columnspan=3)
BOTON3 = Button(root,text="BOTON3",height = 3, width = 10).grid(row=1,column=3,rowspan=2)
root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()