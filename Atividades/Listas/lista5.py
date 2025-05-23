# #Atividade 5 de Lista
# lista = []
# def mostrarLista():
#     print("\nLista atual:", lista)
# while True:
#     print("\nMENU DE TAREFAS")
#     print("0.Sair.")
#     print("1.Adicionar tarefa.")
#     print("2.Remover tarefa.")
#     print("3.Mostrar.")
#     escolha = input("Digite uma opção: ")
#     if escolha == '1':
#         item = input("Digite o item que deseja adicionar a lista: ")
#         lista.append(item)
#         mostrarLista()
#     elif escolha == '2':
#         item = input("Digite o item a ser removido: ")
#         if item in lista:
#             lista.remove(item)
#         else:
#             print("O item não se encontra na lista.")
#             mostrarLista()
#     elif escolha == '3':
#         mostrarLista()
#     elif escolha == '0':
#         print("Programa encerrado. Até a próxima.")
#         break
#     else:
#         print("Opção inválida. Tente um valor válido.")