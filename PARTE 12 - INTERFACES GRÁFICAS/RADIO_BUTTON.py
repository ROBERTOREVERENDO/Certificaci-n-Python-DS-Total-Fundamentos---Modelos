from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")

LISTA_TUPLAS = [
    #("TEXTO DE LA OPCION","VARIABLE QUE GENERA")
    ("OPCION 1","ESCOGISTE LA OPCIÓN 1"),
    ("OPCION 2","ESCOGISTE LA OPCIÓN 2"),
    ("OPCION 3","ESCOGISTE LA OPCIÓN 3"),
    ("OPCION 4","ESCOGISTE LA OPCIÓN 4"),
    ("OPCION 5","ESCOGISTE LA OPCIÓN 5")
]

VARIABLE = StringVar()
VARIABLE.set("OPCION 2")

for NOMBRE_OPCION,OPCION_ESCOGIDA in LISTA_TUPLAS:
    Radiobutton(root, text = NOMBRE_OPCION , variable = VARIABLE, value = OPCION_ESCOGIDA).pack()
    
    
def HACERCLICK():
    LABEL = Label(root,text=VARIABLE.get()).pack()
    
BOTON = Button(root, text="CLICKEAR",command=HACERCLICK).pack()
    
    

root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()