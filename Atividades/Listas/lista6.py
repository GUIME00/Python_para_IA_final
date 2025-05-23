# #Atividade 6 de Lista
# def eliminar_duplicados():
#     numeros = [] #lista vazia que comportará todos os números inseridos pelo usuário
#     while len(numeros) < 10: #limitar até 10 tentativas
#         num = int(input(f"Digite o {len(numeros)+1}° número: "))
#         numeros.append(num) #adiciona o número inserido pelo usuário dentro da lista numeros
#     unicos = [] #lista vazia que vai comportar uma unidade de um mesmo número sem repetir
#     i = 0 #variável de controle
#     while i < len(numeros):
#         if numeros[i] not in unicos:
#             unicos.append(numeros[i])
#         i += 1 #adiciona uma "tentativa"
#     print("Números únicos:", unicos) #saída dos números únicos
#     print("Todos os números inseridos pelo usuário:", numeros) #saída dos números inseridos pelo usuário
# eliminar_duplicados()