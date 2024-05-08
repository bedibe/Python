import tkinter as tk 
janela= tk.Tk()
label = tk.Label(text="Nome")
entry = tk.Entry()
label.pack()
entry.pack()
entry.insert(0, "Bernardo")
janela.mainloop()