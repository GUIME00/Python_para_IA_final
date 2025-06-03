# #Prática

# try:
#     with open("Atividades/Arquivos/nums.txt") as arquivo:
#         maior = 0
#         for num in arquivo:
#             numero = int(num)
#             if numero > maior:
#                 maior = numero
#         print("Maior número:", maior)
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
# except ValueError:
#     print("O arquivo com os dados deve ser de números inteiros.")

# # Utilizando a estrutura max()
# try:
#     with open('Atividades/Arquivos/nums.txt') as arquivo:
#         numeros = [int(num) for num in arquivo]
#         maior = max(numeros)
#         print("Maior número:", maior)
 
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
 
# except ValueError:
#     print("O arquivo com os dados deve ser de números inteiros.")

# # Utilizando a estrutura def() e max()
# def encontrar_maior():
#     try:
#         print("Maior número:", max(int(l) for l in open('Atividades/Arquivos/nums.txt')))
#     except FileNotFoundError:
#         print("Arquivo não encontrado.")
#     except ValueError:
#         print("O arquivo com os dados deve ser de números inteiros.")

# encontrar_maior()