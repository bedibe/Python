import tkinter as tk

def exibir_nome():
    nome_digitado = entry.get()
    texto_inserido.delete(1.0, tk.END)  # Limpa qualquer texto anterior
    texto_inserido.insert(tk.END, nome_digitado)

# Criar a janela
janela = tk.Tk()
janela.title("Widget de Entrada")

# Criar o widget de entrada
entry = tk.Entry(janela, width=40)
entry.insert(0, "Digite o seu nome!")
entry.pack(pady=10)

# Botão para exibir o texto inserido
btn_exibir = tk.Button(janela, text="Exibir Nome", command=exibir_nome)
btn_exibir.pack(pady=5)

# Criar o widget para exibir o texto inserido
texto_inserido = tk.Text(janela, width=40, height=10, bg="white", fg="black")
texto_inserido.pack(pady=10)

# Executar o loop principal da janela
janela.mainloop()
