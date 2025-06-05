# arquivo = None
# try:
#     arquivo = open("exemplo.txt", "r")
#     conteudo = arquivo.read()

# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# except Exception as e:
#     print(f"Erro ao ler o arquivo: {e}")
# else:
#     print("Processamento do arquivo concluído com sucesso.")
# finally:
#     if arquivo:
#         arquivo.close()
#         print("Arquivo fechado.")

# conteudo = None
# try:
#     with open("Atividades/Arquivos/exemplo.txt") as novo_arquivo:
#         # conteudo = novo_arquivo.read()
#         # print(conteudo)
#             for linha in novo_arquivo:
#                  print(linha)
# except FileNotFoundError:
#     print("Arquivo não encontrado.")