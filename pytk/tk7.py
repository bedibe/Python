import tkinter as tk 

def ao_focar(event):
    if not entrada.get():
        entrada.insert(0, "Digite o seu nome aqui!")
        entrada.config(fg="gray") #altera a cor do texto de volta para cinza

janela = tk.Tk()
entrada = tk.Entry(width=40, bg="white", fg="gray")
entrada.pack()
entrada.insert(0, "Digite o seu nome aqui!")

entrada.bind("<FocusIn>", ao_focar)

entrada.bind("<FocusOut>", ao)

