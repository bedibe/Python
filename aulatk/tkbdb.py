import tkinter as tk
def sair():
    janela.quit()
janela = tk.Tk()
janela.geometry('320x150')
menubar = tk.Menu(janela)
janela.config(menu= menubar)

menu_arquivo = tk.Menu(menubar, tearoff=0)
menu_arquivo.add_command(label='Abrir')
menu_arquivo.add_command(label='Fechar')
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Sair', command=sair)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_ajuda = tk. Menu(menubar, tearoff=0)
menu_ajuda.add_command(label='Bem-vindo')
menu_ajuda.add_command(label='Sobre')
menubar.add_cascade(label='Ajuda', menu=menu_ajuda)

janela.mainloop()