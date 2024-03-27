import csv

def salvar_em_csv(dados):
    try:
        with open('pessoas.csv', 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for pessoa in dados:
                escritor_csv.writerow(pessoa)
        print("Arquivo CSV 'pessoas.csv' foi criado com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar arquivo CSV: {e}")

# Exemplo de uso:
dados = [["João", 30], ["Maria", 25], ["José", 35]]
salvar_em_csv(dados)