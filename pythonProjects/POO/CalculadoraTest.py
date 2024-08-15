import math
from tkinter import *
from tkinter import ttk


def darkTheme(*args):
    estilos.configure("mainframe.TFrame", background="gray15")

    style_label1.configure("Label1.TLabel", font=("Arial", 14), background="gray11", anchor="e", foreground="white")
    style_label2.configure("Label2.TLabel", font=("Arial", 35), background="gray11", anchor="e", foreground="white")

    style_buttonNumbers.configure("Button.TButton", font=("Arial", 12), background="gray11", relief="flat",
                                  foreground="white")
    style_buttonNumbers.map("Button.TButton", foreground=[("active", "white")], background=[("active", "#393d42")])

    style_buttonOperations.configure("ButtonOP.TButton", font=("Arial", 12), background="#171a4a", relief="flat",
                                     foreground="white")
    style_buttonOperations.map("ButtonOP.TButton", foreground=[("active", "white")],
                               background=[("active", "#2f2c79")])

    style_buttonBorrar.configure("ButtonBorrar.TButton", font=("Arial", 12), background="#722825", relief="flat",
                                 foreground="white")
    style_buttonBorrar.map("ButtonBorrar.TButton", foreground=[("active", "white")],
                           background=[("active", "#8b3e39")])

    style_buttonRemamnig.configure("ButtonRemanig.TButton", font=("Arial", 12), background="#171a4a", relief="flat",
                                   foreground="white")
    style_buttonRemamnig.map("ButtonRemanig.TButton", foreground=[("active", "white")],
                             background=[("active", "#2f2c79")])


def lightTheme(*args):
    estilos.configure("mainframe.TFrame", background="light gray")

    style_label1.configure("Label1.TLabel", font=("Arial", 14), background="White", anchor="e", foreground="black")
    style_label2.configure("Label2.TLabel", font=("Arial", 35), background="White", anchor="e", foreground="black")

    style_buttonNumbers.configure("Button.TButton", font=("Arial", 12), background="White", relief="flat",
                                  foreground="black")
    style_buttonNumbers.map("Button.TButton", foreground=[("active", "blue")], background=[("active", "light gray")])

    style_buttonOperations.configure("ButtonOP.TButton", font=("Arial", 12), background="#89A9DB", relief="flat",
                                     foreground="black")
    style_buttonOperations.map("ButtonOP.TButton", foreground=[("active", "white")], background=[("active", "#3747DB")])

    style_buttonBorrar.configure("ButtonBorrar.TButton", font=("Arial", 12), background="#DB949A", relief="flat",
                                 foreground="black")
    style_buttonBorrar.map("ButtonBorrar.TButton", foreground=[("active", "white")], background=[("active", "#DB3747")])

    style_buttonRemamnig.configure("ButtonRemanig.TButton", font=("Arial", 12), background="#89A9DB", relief="flat",
                                   foreground="black")
    style_buttonRemamnig.map("ButtonRemanig.TButton", foreground=[("active", "white")],
                             background=[("active", "#3747DB")])


def enterValues(key):
    if ("0" >= key <= "9" or key == "." or "(" or ")" or key == "*" or key == "+" or key == "-" or key == "/"
            or key == "*" or key == "+" or key == "-" or key == "/"):
        entrada2.set(entrada2.get() + key)

    if key == "=":
        entrada1.set(" ")
        entrada1.set(entrada1.get() + entrada2.get())

        operation = entrada1.get()
        operation = operation[:len(operation) - 1]

        result = eval(operation)
        entrada2.set(result)


def enterValuesKeyBoard(event):
    key = event.char

    if ("0" >= key <= "9" or key == "." or "(" or ")" or key == "*" or key == "+" or key == "-" or key == "/"
            or key == "*" or key == "+" or key == "-" or key == "/"):
        entrada2.set(entrada2.get() + key)

    if key == "=":
        entrada1.set(entrada1.get() + entrada2.get())

        operation = entrada1.get()
        operation = operation[:len(operation) - 1]

        result = eval(operation)
        entrada2.set(result)

    if key == "=":
        entrada1.set(entrada1.get() + entrada2.get())

        operation = entrada1.get()
        operation = operation[:len(operation) - 1]

        result = eval(operation)
        entrada2.set(result)


def squareRoot():
    entrada1.set(entrada2.get())
    result = math.sqrt(float(entrada2.get()))
    entrada2.set(result)


def delete():
    entrada2.set(entrada2.get()[:len(entrada2.get()) - 1])


def clear():
    entrada1.set(" ")
    entrada2.set(" ")


# Creamos la ventana de la calculadora
window = Tk()
window.title("Calculadora")
window.geometry("+500+80")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background="light gray")

# Creamos el frame principal donde va el contenido de la calculadora
mainframe = ttk.Frame(window, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(N + W + E + S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

# Estilos de los labels
style_label1 = ttk.Style()
style_label1.configure("Label1.TLabel", font=("Arial", 14), background="White", anchor="e")

style_label2 = ttk.Style()
style_label2.configure("Label2.TLabel", font=("Arial", 35), background="White", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W + E + S + N))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W + E + S + N))

# estilos para los botones
style_buttonNumbers = ttk.Style()
style_buttonNumbers.configure("Button.TButton", font=("Arial", 12), background="White", relief="flat")
style_buttonNumbers.map("Button.TButton", foreground=[("active", "blue")], background=[("active", "light gray")])

style_buttonOperations = ttk.Style()
style_buttonOperations.configure("ButtonOP.TButton", font=("Arial", 12), background="#89A9DB", relief="flat")
style_buttonOperations.map("ButtonOP.TButton", foreground=[("active", "white")], background=[("active", "#3747DB")])

style_buttonBorrar = ttk.Style()
style_buttonBorrar.configure("ButtonBorrar.TButton", font=("Arial", 12), background="#DB949A", relief="flat")
style_buttonBorrar.map("ButtonBorrar.TButton", foreground=[("active", "white")], background=[("active", "#DB3747")])

style_buttonRemamnig = ttk.Style()
style_buttonRemamnig.configure("ButtonRemanig.TButton", font=("Arial", 12), background="#89A9DB", relief="flat")
style_buttonRemamnig.map("ButtonRemanig.TButton", foreground=[("active", "white")], background=[("active", "#3747DB")])

# Creamos botones de la calculadora

button0 = ttk.Button(mainframe, text="0", style="Button.TButton", command=lambda: enterValues("0"))
button1 = ttk.Button(mainframe, text="1", style="Button.TButton", command=lambda: enterValues("1"))
button2 = ttk.Button(mainframe, text="2", style="Button.TButton", command=lambda: enterValues("2"))
button3 = ttk.Button(mainframe, text="3", style="Button.TButton", command=lambda: enterValues("3"))
button4 = ttk.Button(mainframe, text="4", style="Button.TButton", command=lambda: enterValues("4"))
button5 = ttk.Button(mainframe, text="5", style="Button.TButton", command=lambda: enterValues("5"))
button6 = ttk.Button(mainframe, text="6", style="Button.TButton", command=lambda: enterValues("6"))
button7 = ttk.Button(mainframe, text="7", style="Button.TButton", command=lambda: enterValues("7"))
button8 = ttk.Button(mainframe, text="8", style="Button.TButton", command=lambda: enterValues("8"))
button9 = ttk.Button(mainframe, text="9", style="Button.TButton", command=lambda: enterValues("9"))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="ButtonBorrar.TButton", command=lambda: delete())
button_borrar_todo = ttk.Button(mainframe, text="C", style="ButtonBorrar.TButton", command=lambda: clear())

button_parentesis1 = ttk.Button(mainframe, text="(", style="ButtonRemanig.TButton", command=lambda: enterValues("("))
button_parentesis2 = ttk.Button(mainframe, text=")", style="ButtonRemanig.TButton", command=lambda: enterValues(")"))
button_punto = ttk.Button(mainframe, text=".", style="Button.TButton", command=lambda: enterValues("."))

button_suma = ttk.Button(mainframe, text="+", style="ButtonOP.TButton", command=lambda: enterValues("+"))
button_resta = ttk.Button(mainframe, text="-", style="ButtonOP.TButton", command=lambda: enterValues("-"))
button_multiplicacion = ttk.Button(mainframe, text="*", style="ButtonOP.TButton", command=lambda: enterValues("*"))
button_division = ttk.Button(mainframe, text=chr(247), style="ButtonOP.TButton", command=lambda: enterValues("/"))
button_raiz = ttk.Button(mainframe, text=chr(8730), style="ButtonOP.TButton", command=lambda: squareRoot())

button_igual = ttk.Button(mainframe, text="=", style="ButtonOP.TButton", command=lambda: enterValues("="))

# Colocamos los botones en la pantalla
button_parentesis1.grid(column=0, row=3, sticky=(N + W + E + S))
button_parentesis2.grid(column=1, row=3, sticky=(N + W + E + S))
button_borrar_todo.grid(column=2, row=3, sticky=(N + W + E + S))
button_borrar.grid(column=3, row=3, sticky=(N + W + E + S))

button7.grid(column=0, row=4, sticky=(N + W + E + S))
button8.grid(column=1, row=4, sticky=(N + W + E + S))
button9.grid(column=2, row=4, sticky=(N + W + E + S))
button_division.grid(column=3, row=4, sticky=(N + W + E + S))

button4.grid(column=0, row=5, sticky=(N + W + E + S))
button5.grid(column=1, row=5, sticky=(N + W + E + S))
button6.grid(column=2, row=5, sticky=(N + W + E + S))
button_multiplicacion.grid(column=3, row=5, sticky=(N + W + E + S))

button1.grid(column=0, row=6, sticky=(N + W + E + S))
button2.grid(column=1, row=6, sticky=(N + W + E + S))
button3.grid(column=2, row=6, sticky=(N + W + E + S))
button_suma.grid(column=3, row=6, sticky=(N + W + E + S))

button0.grid(column=0, row=7, columnspan=2, sticky=(N + W + E + S))
button_punto.grid(column=2, row=7, sticky=(N + W + E + S))
button_resta.grid(column=3, row=7, sticky=(N + W + E + S))

button_igual.grid(column=0, row=8, columnspan=3, sticky=(N + W + E + S))
button_raiz.grid(column=3, row=8, sticky=(N + W + E + S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

window.bind("<KeyPress-o>", lambda e: darkTheme())
window.bind("<KeyPress-l>", lambda e: lightTheme())
window.bind("<Key>", enterValuesKeyBoard)
window.bind("<KeyPress-BackSpace>", lambda e: delete())
window.bind("<KeyPress-c>", lambda e: clear())
window.bind("<KeyPress-Return>", lambda e: enterValues("="))

# Iniciamos la calculadora
window.mainloop()
