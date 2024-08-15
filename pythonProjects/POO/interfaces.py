import tkinter
from tkinter import *

window = Tk()
window.title("Ventana de pruebas")
window.geometry("960x540")
window.resizable(False, False)
window.config(bg="royalBlue")

titlePage = tkinter.Label(window, text="Welcome to Genius Help", font=("Open Sans", 26))
titlePage.config(bg="royalBlue", fg="white")
titlePage.place(x=420.3, y=41)


def exit():
    window.destroy()


exitButton = tkinter.Button(window, text="Exit", height=1, width=4, command=exit, borderwidth=5, )
exitButton.config(bg="red", fg="white", font=("Arial", 12))
exitButton.place(x=850, y=450)

window.mainloop()
