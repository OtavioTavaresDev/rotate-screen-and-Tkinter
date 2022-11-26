from tkinter import *
from tkinter import ttk
import rotatescreen
screen = rotatescreen.get_primary_display()

grau = 0
def girar_positivo():
    global grau, screen
    grau += 90
    screen.rotate_to(grau)

def girar_negativo():
    global grau, screen
    if grau == 0:
        pass
    else:
        grau -= 90
        screen.rotate_to(grau)

def girar_normal():
    global grau, screen
    grau = 0
    screen.rotate_to(grau)

janela = Tk()
ttk.Label(janela, text="Girar a Tela").grid(column=3, row=0)
ttk.Button(janela, command=girar_positivo, text="Girar +90º").grid(column=5, row=1)
ttk.Button(janela, command=girar_normal, text="Voltar para 0º").grid(column=3, row=1)
ttk.Button(janela, command=girar_negativo, text="Girar -90º").grid(column=1, row=1)

janela.mainloop()
