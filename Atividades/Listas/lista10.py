# #Atividade 10 de Lista

# def lista_compras():
#     compras = []
#     while True:
#         item = input("Digite um item, 'remover' para excluir ou 'sair' para encerrar: ")
#         if item == "sair":
#             print("Finalizando.")
#             break
#         elif item == "remover":
#             if compras:
#                 nome_remover = input("Digite o nome do item que deseja remover: ")
#                 if nome_remover in compras:
#                     compras.remove(nome_remover)
#                     print(f"Item '{nome_remover}' removido.")
#                 else:
#                     print(f"Item '{nome_remover}' não se encontra na lista.")
#             else: print("Lista vazia.")
#         else:
#             compras.append(item)
#             print(f"Item '{item}' adicionado.")
#     compras_ordenada = sorted(compras)
#     i = 0
#     print("Lista:")
#     while i < len(compras_ordenada):
#         print(compras_ordenada[i])
#         i += 1
