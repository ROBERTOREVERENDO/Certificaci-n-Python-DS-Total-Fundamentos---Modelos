from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")
root.resizable(1,1) #(ANCHO,ALTO)

FRAME = Frame(root , height=400 , width=400)
FRAME.pack(fill='both' , expand=1)
FRAME.config(bg='gray')

root.config(cursor="cross")
root.config(bd=25)
root.config(relief='sunken')

root.mainloop()

