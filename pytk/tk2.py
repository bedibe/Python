import tkinter as tk
janela=tk.Tk()
label = tk.Label(
    text="Brincando com Tkinter",
    fg="#E6E6FA",
    bg="#FF1493",
    width=40,
    height=40
)
botao = tk.Button(
    text="Botão",
    width=25,
    height=5,
    bg="black",
    fg="yellow"
)
entry= tk.Entry(fg="yellow", bg="blue", width=50)
label.pack()
botao.pack()
janela.mainloop()