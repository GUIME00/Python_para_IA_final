# #Atividade 2 de Dicionário

# def imprimir_agenda(agenda):
#     print("\nAgenda telefônica:")
#     for nome in agenda:
#         numeros = ', '.join(agenda[nome])
#         print(f"{nome}: {numeros}")
 
# def main():
#     agenda = {}
 
#     while True:
#         print("\nComandos: \n1=buscar \n2=adicionar \n3=sair")
#         comando = input("Digite o comando: ")
 
#         if comando == '1':
#             nome = input("Digite o nome para buscar: ")
#             if nome in agenda:
#                 print(f"Números de {nome}: {', '.join(agenda[nome])}")
#             else:
#                 print(f"{nome} não está na agenda.")
 
#         elif comando == '2':
#             nome = input("Digite o nome: ")
#             numero = input("Digite o número: ")
#             if nome in agenda:
#                 agenda[nome].append(numero)
#             else:
#                 agenda[nome] = [numero]
#             print(f"Número adicionado para {nome}.")
 
#         elif comando == '3':
#             imprimir_agenda(agenda)
#             print("Saindo...")
#             break
 
#         else:
#             print("Comando inválido! Tente novamente.")
 
# if __name__ == "__main__":
#     main()