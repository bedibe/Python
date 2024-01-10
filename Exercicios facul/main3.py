
# Cria uma lista para armazenar as respostas
respostas = []
# Faz 5 perguntas e armazena as respostas na lista
pergunta_a = input("Telefonou para a vítima? (S/N): ")
respostas.append(pergunta_a.upper())
pergunta_b = input("Esteve no local do crime? (S/N): ")
respostas.append(pergunta_b.upper())
pergunta_c = input("Mora perto da vítima? (S/N): ")
respostas.append(pergunta_c.upper())
pergunta_d = input("Devia para a vítima? (S/N): ")
respostas.append(pergunta_d.upper())
pergunta_e = input("Já trabalhou com a vítima? (S/N): ")
respostas.append(pergunta_e.upper())
# Conta o número de respostas positivas (S) na lista
respostas_positivas = respostas.count("S")
# Classifica a pessoa com base nas respostas
if respostas_positivas == 2:
    print("Suspeita")
elif respostas_positivas in (3, 4):
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassina")
else:
    print("Inocente")