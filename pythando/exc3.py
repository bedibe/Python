import json
import time

def salvar_em_json(dados, nome_arquivo_saida):
    try:
        start_time = time.time()  # Captura o tempo inicial
        with open(nome_arquivo_saida, "w") as json_file:
            json.dump(dados, json_file)
        end_time = time.time()  # Captura o tempo final
        print(f"Dados salvos com sucesso em '{nome_arquivo_saida}'")
        print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def ler_json(nome_arquivo_entrada):
    try:
        with open(nome_arquivo_entrada, "r") as json_file:
            dados = json.load(json_file)
        return dados
    except Exception as e:
        print(f"Erro ao ler os dados do arquivo de entrada: {e}")
        return None

# Arquivo de entrada e saída
arquivo_entrada = "dados.json"
arquivo_saida = "dados_saida.json"

# Lê os dados do arquivo de entrada
dados = ler_json(arquivo_entrada)

# Se os dados foram lidos com sucesso, salva-os no arquivo de saída
if dados:
    salvar_em_json(dados, arquivo_saida)
