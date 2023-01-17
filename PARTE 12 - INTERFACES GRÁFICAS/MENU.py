from tkinter import *

root = Tk()
root.title("PRIMER INTERFAZ GRÁFICA")
root.geometry('400x300')

MENU = Menu(root)
root.config(menu=MENU)

def NEW_FILE():
    LABEL1 = Label(root, text="Acabas de apretar el Menu -> File -> New File").pack()
    
def OPEN():
    LABEL2 = Label(root, text="Acabas de apretar el Menu -> File -> Open").pack()
    
def QUIT():
    LABEL3 = Label(root, text="Acabas de apretar el Menu -> File -> Quit").pack()
    
def UNDO():
    LABEL4 = Label(root, text="Acabas de apretar el Menu -> Edit -> Undo").pack()
    
def CUT():
    LABEL5 = Label(root, text="Acabas de apretar el Menu -> Edit -> Cut").pack()
        
def COPY():
    LABEL6 = Label(root, text="Acabas de apretar el Menu -> Edit -> Copy").pack()

#------------------------------------MENU FILE------------------------------------
FILEMENU = Menu(MENU,tearoff=0)

MENU.add_cascade(label="File",menu=FILEMENU)

FILEMENU.add_command(label="New File", command = NEW_FILE)
FILEMENU.add_separator()
FILEMENU.add_command(label="Open", command = OPEN)
FILEMENU.add_command(label="Quit", command = QUIT)


#------------------------------------MENU EDIT------------------------------------
EDITMENU = Menu(MENU,tearoff=0)

MENU.add_cascade(label="Edit",menu=EDITMENU)

EDITMENU.add_command(label="Undo", command = UNDO)
EDITMENU.add_separator()
EDITMENU.add_command(label="Cut", command = CUT)
EDITMENU.add_command(label="Copy", command = COPY)


#------------------------------------MENU HELP------------------------------------
HELPMENU = Menu(MENU,tearoff=0)

MENU.add_cascade(label="Help",menu=HELPMENU)

HELPMENU.add_command(label="Tutorial")
HELPMENU.add_separator()
HELPMENU.add_command(label="About Spyder")




root.config(cursor="cross")
root.config(bg='gray')
root.config(bd=25)
root.config(relief='sunken')

root.resizable(1,1) #(ANCHO,ALTO)

root.mainloop()