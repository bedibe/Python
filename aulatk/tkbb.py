import tkinter as tk
# Função a ser chamada quando o botão for clicado
def clicado():
    label.config(text="Botão clicado!")
#Cria uma janela
janela = tk.Tk()
janela.title("Exemplo Tkinter")
#Cria um rótulo
label = tk.Label(janela, text="Olá, Tkinter!")
label.pack()
#Cria um botão
botao= tk.Button(janela, text="Clique em Mim", command=clicado)
botao.pack()
#inicia o loop principal da aplicação
janela.mainloop()