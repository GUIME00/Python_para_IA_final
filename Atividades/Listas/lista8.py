# #Atividade 8 de Lista

# import re

# def cadastrar_senhas():
#     senhas = []
#     while len(senhas) < 5:
#         senha = input(f"Digite a {len(senhas)+1}ª senha: ")
#         if len(senha) >= 8 and re.search("[0-9]",senha) != None:
#             senhas.append(senha)
#         else:
#             print("Senha inserida inválida. A senha deve conter pelo menos um número e 8 caracteres.")
#     print("Senhas válidas")
#     i = 0
#     while i < len(senhas):
#         print(senhas[i])
#         i += 1
# cadastrar_senhas()



# def senhas():
#     senhas_cinco = []
#     while len(senhas_cinco) < 5:
#         senha = input(f"Digite a {len(senhas_cinco)+1}ª senha: ")        
#         if len(senha) < 8:
#             print("Senha inválida. A senha deve ter 8 ou mais caracteres.")
#         elif not any(char.isdigit() for char in senha):
#             print("A senha deve conter pelo menos um número.")
#         else:
#             senhas_cinco.append(senha)
#             print("Senha cadastrada.")
#     print("\nSenhas válidas cadastradas:")
#     for i, s in enumerate(senhas_cinco, 1):
#         print(f"{i}:{s}")
# senhas()