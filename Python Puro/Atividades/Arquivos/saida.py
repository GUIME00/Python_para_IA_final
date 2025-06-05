# try:
#     print("Digite 0 se quiser encerrar.")
#     while True:
#         with open('Atividades/Arquivos/saida.txt',"a") as arquivo:
#             nota = input("Anotação: ")
#             if nota == '0':
#                 print("Saindo...")
#                 break
#             else:
#                 f = arquivo
#                 f.write(f"\n{nota}")
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")