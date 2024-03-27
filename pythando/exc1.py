from dataclasses import dataclass
from typing import List

@dataclass
class Pessoa:
    nome: str
    idade: int

def salvar_pessoas(lista_pessoas: List[Pessoa], nome_arquivo: str = "pessoa.txt"):
    try:
        with open(nome_arquivo, "w") as arquivo:
            for pessoa in lista_pessoas:
                arquivo.write(f"{pessoa.nome},{pessoa.idade}\n")
        print(f"Os dados das pessoas foram salvos em '{nome_arquivo}' com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    pessoas = [
        Pessoa(nome="bernardo", idade=20),
        Pessoa(nome="nicolas", idade=18),
        Pessoa(nome="Maria", idade=52)
    ]
    salvar_pessoas(pessoas)