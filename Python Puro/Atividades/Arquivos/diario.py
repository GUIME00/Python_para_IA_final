
# # Versão do professor

# import datetime
# def adicionar_entrada_diario():
#     data = input("Digite a data: ")
#     descricao = input("Digite a descrição da entrada do diário:\n ")
#     entrada = {
#         "data": data,
#                "descrição": descricao
#                }
#     with open("diario.txt","a",encoding="utf-8") as arquivo:
#         arquivo.write(str(entrada) + "\n")
#     print("Entrada adicionada.")
# adicionar_entrada_diario()



# # Versão 1.0 (eu que fiz)

# import time
# t = time.localtime(time.time())
# localtime = time.asctime(t)
# str = "D/H " + time.asctime(t)
# try:
#         print("Digite 0 se quiser encerrar.")
#         while True:
#             with open('Atividades/Arquivos/diario.txt',"a") as arquivo:
#                 nota = input("Anotação: ")
#                 if nota == '0':
#                     print("Saindo...")
#                     break
#                 else:
#                     f = arquivo
#                     print(str)
#                     f.write(f"\n{nota}\n{str}")
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")



# # Versão 2.0

# import os
# import time
# t = time.localtime(time.time())
# localtime = time.asctime(t)
# str = "D/H " + time.asctime(t)
# caminho = "Atividades/Arquivos/diario.txt"
# if os.path.exists(caminho):
#     print("A pasta existe.")
#     os.remove(caminho)
# else:
#     print("A pasta não existe.")
#     os.makedirs("Atividades/Arquivos",exist_ok=True)
# try: 
#     print("Digite 0 se quiser encerrar.")
#     while True:
#         with open(caminho, "a", encoding="utf-8") as arquivo:
#                 nota = input("Anotação: ")
#                 if nota == '0':
#                     print("Saindo...")
#                     break
#                 else:
#                     f = arquivo
#                     print(str)
#                     f.write(f"\nNota: {nota}\n{str}")
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")