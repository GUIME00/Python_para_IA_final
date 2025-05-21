# #Atividade 51
# import re
# while True:
#     senha = input("Digite uma senha com 8 caracteres: ")
#     maiuscula = re.search("[A-Z]",senha)
#     minuscula = re.search("[a-z]",senha)
#     numero = re.search("[0-9]",senha)
#     if len(senha) < 8:
#         print("A senha precisa ter 8 caracteres.")
#     elif maiuscula == None:
#         print("A senha deve conter pelo menos uma letra maiúscula.")
#     elif minuscula == None:
#         print("A senha deve conter uma letra minúscula.")
#     elif numero == None:
#         print("A senha deve conter um número.")
#     else:
#         print("Senha criada com sucesso.")
#         break