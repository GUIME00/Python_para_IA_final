# #Atividade 5 de Função
# #Método "diferente":
# def quadradoString(string, tamanho):
#     i = 0
#     while i < tamanho:
#         j = 0
#         linha = ''
#         pos = i
#         while j < tamanho:
#             linha += string[pos]
#             pos += 1
#             if pos == len(string):
#                 pos = 0
#             j += 1
#         print(linha)
#         i += 1
# quadradoString("Bigato", 5)

# #Método correto:
# def repetir(palavra, numero): #Definir a função 
#     stringTotal = (palavra * numero) #Variável que multiplica a string pelo inteiro
#     linha = 0 #Variável de controle
#     while linha < numero:
#         coluna = 0 #Variável de controle 2
#         letras = " " #Variável de controle 3
#         while coluna < numero:
#             posicao = linha * numero + coluna #"Layout" da saída
#             letras += stringTotal[posicao] #"Layout" da saída 2
#             coluna += 1 
#         print(letras)
#         linha += 1
# repetir("Estalactite", 4) 