# def frutas():
#     dicionario = {}
#     try:
#         with open('Atividades/Arquivos/frutas.csv') as Arquivo:
#             for linha in Arquivo:
#                 linha = linha.strip()
#                 if linha:
#                     dados = linha.split(";")
#                     dicionario[dados[0]] = float(dados[1])
#     except ValueError:
#         print("Erro: erro ao converter o preço para float. ")
#     except FileNotFoundError:
#         print("Erro: arquivo não encontrado")
#     return dicionario
# print(frutas())