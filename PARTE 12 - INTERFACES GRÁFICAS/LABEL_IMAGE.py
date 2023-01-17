from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")

IMAGEN = ImageTk.PhotoImage(Image.open("IMAGES/LIMA.jpg"))
LABEL_IMAGEN = Label(image=IMAGEN)
LABEL_IMAGEN.pack()

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()