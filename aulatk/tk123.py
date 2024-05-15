import tkinter as tk
janela = tk.Tk()
frame = tk.Frame(master=janela, width=210, height=210)
frame.pack()
label1 = tk.Label(master=frame, text="Estou na posição (0, 0)", bg="red")
label1.place(x=0, y=0)
label2 = tk.Label(master=frame, text="Estou na posição (75, 75)", bg="blue")
label2.place(x=75, y=75)
janela.mainloop()