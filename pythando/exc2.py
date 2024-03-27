import json

def salvar_em_json(dados):
    try:
        with open("dados.json", "w") as json_file:
            json.dump(dados, json_file)
        print("Dados salvos com sucesso em 'dados.json'")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Exemplo de uso:
dados = {
    "nome": "bdb",
    "idade": 20,
    "cidade": "Rio de Janeiro"
}

salvar_em_json(dados)
