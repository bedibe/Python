import tkinter as tk
janela = tk.Tk()
for i in range(3):
    janela.columnconfigure(i, weight=1, minsize=75)
    janela.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=janela,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Linha {i}\nColuna {j}")
        label.pack()
janela.mainloop()