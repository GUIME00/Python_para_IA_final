# #Atividade 4 de Dicionário

# # Sem input()

# def add_filme(database: list, nome: str, diretor:str, ano: int, duracao: int):
#     filme = {
#             "nome": nome,
#             "diretor": diretor,
#             "ano": ano,
#             "duração": duracao
#             }
#     database.append(filme)
# meu_banco_de_filmes = []
# add_filme(meu_banco_de_filmes,"Onde os Fracos Não Têm Vez", "Cormac McCarthy", 2007, 122)
# add_filme(meu_banco_de_filmes,"Uma Babá Quase Perfeita", "Chris Columbus", 1993, 126)
# print(f"Info:{meu_banco_de_filmes}")

# # Com input()

# def add_filme(database: list, nome: str, diretor:str, ano: int, duracao: int):
#     filme = {
#             "nome": nome,
#             "diretor": diretor,
#             "ano": ano,
#             "duração": duracao
#             }
#     database.append(filme)
# meu_banco_de_filmes = []
# nome = input("Digite o nome do filme: ")
# diretor = input("Digite o nome do diretor deste filme: ")
# ano = int(input("Digite o ano em que este filme lançou: "))
# duracao = int(input("Digite o tempo de duração deste filme em minutos: "))
# add_filme(meu_banco_de_filmes,nome, diretor, ano, duracao)
# print(f"Info:{meu_banco_de_filmes}")

# # Versão Ultra Mega Blaster Master

# def add_filme(database: list, nome: str, diretor:str, ano: int, duracao: int):
#     filme = {
#             "nome": nome,
#             "diretor": diretor,
#             "ano": ano,
#             "duração": duracao
#             }
#     database.append(filme)
# meu_banco_de_filmes = []
# while True:
#     nome = input("Digite o nome do filme: ")
#     diretor = input("Digite o nome do diretor deste filme: ")
#     ano = int(input("Digite o ano em que este filme lançou: "))
#     duracao = int(input("Digite o tempo de duração deste filme em minutos: "))
#     if ano <= 0:
#         print("Este valor não é válido.")
#     else:
#         print(f"O filme: {nome}, lançou em {ano}.")
#     if duracao <= 0:
#         print("Este valor não é válido tente outro.")
#     else:
#         formula = duracao / 60
#         print(f"O filme têm o tempo de duração igual a: {formula} horas.")
#     add_filme(meu_banco_de_filmes,nome, diretor, ano, duracao)
#     print(f"Informações:{meu_banco_de_filmes}")
#     break

# #Versão do professor

# banco_filmes = []

# def add_filme(database, nome, diretor, ano, duracao):
#     filme = {
#             "nome": nome,
#             "diretor": diretor,
#             "ano": ano,
#             "duração": duracao
#             }
#     database.append(filme)
#     print(banco_filmes)

# while True:
#     nome = input("Digite o nome do filme: ")
#     diretor = input("Digite o nome do diretor deste filme: ")
#     ano = int(input("Digite o ano em que este filme lançou: "))
#     duracao = int(input("Digite o tempo de duração deste filme em minutos: "))
#     add_filme(banco_filmes, nome, diretor, ano, duracao)