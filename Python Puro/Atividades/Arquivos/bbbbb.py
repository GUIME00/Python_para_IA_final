# import os

# os.remove("dados2.txt")

# # Cria e remove a pasta 
# if os.path.exists("Atividades/Apagar"):
#     print("A pasta existe.")
#     os.rmdir("Atividades/Apagar")
# else:
#     print("A pasta não existe.")
#     os.mkdir("Atividades/Apagar")

# import json
# from datetime import datetime
# caminho = "Atividades/Arquivos/diario.txt"
# def adicionar_entrada():
#     # Solicita a descrição da entrada
#     descricao = input("Digite a descrição da entrada do diário: ")
 
#     # Pega a data atual
#     data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
#     # Cria um dicionário com a entrada
#     entrada = {
#                 "data": data_atual,
#                 "descricao": descricao
#                 }
 
#     # Abre o arquivo diario.txt e adiciona a entrada como JSON
#     with open(caminho, "a", encoding="utf-8") as arquivo:
#         arquivo.write(json.dumps(entrada) + "\n")
#     print("Entrada adicionada com sucesso!")

# adicionar_entrada()