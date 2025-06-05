# #Atividade 1 de Dicionário

# Meu código

# lista = {}
  
# while True:
#     comando = input("\nComandos: \n1 - busca \n2 - adiciona \n3 - sair \nDigite aqui: ")
#     if comando == '2':
#         nome = input("Digite o nome que deseja adicionar na lista telefônica: ")
#         telefone = input("Digite o telefone deste contato: ")
#         lista[nome] = telefone
#         print(f"{nome} adicionado a sua lista telefônica.")
#     elif comando == '1':
#         busca = input("Digite o nome de quem está procurando: ")
#         if busca in lista:
#             print(f"{busca} encontrado(a).")
#             print(lista[busca])
#         else:
#             print("Nome não foi encontrado. Digite 1 para adicionar um contato novo. :-)")
#     elif comando == '3':
#         print("Saindo...")
#         break
#     else:
#         print("Comando não identificado.")

# Código do professor

# def lista_telefonica():
#     agenda = {}  
 
#     while True:
#         comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
 
#         if comando == "1":
#             nome = input("nome: ")
#             if nome in agenda:
#                 print("número:", agenda[nome])
#             else:
#                 print("nenhum número")
 
#         elif comando == "2":
#             nome = input("nome: ")
#             numero = input("número: ")
#             agenda[nome] = numero
#             print("ok!")
#         elif comando == "3":
#             print("saindo...")
#             print(agenda)
#             break
#         else:
#             print("Comando inválido. Tente novamente.")          
# lista_telefonica()