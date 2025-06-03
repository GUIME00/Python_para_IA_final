# #Atividade 4 de Dicionário com Try e Except

# arquivo = None
# try:
#     arquivo = open("dados.txt", "r")
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
#         print(arquivo)
#         print(conteudo)