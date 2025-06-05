# #Atividade 7 de For

# mesa = [
#     ["","",""],
#     ["","",""],
#     ["","",""]
#     ]
# contador = 0 # Contador do número de jogadas feitas
# print(F"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!")
 
# def jogue_o_jogo(mesa,linha,coluna,caracter): # função que atualiza o tabuleiro
#     mesa[linha][coluna] = caracter
#     exibe_resultado()
#     if contador % 2 != 0:
#         jogador = "1 (x)"
#     else:
#         jogador = "2 (O)"
       
#     print(f"Tempo {contador} - Ótimo jogada, agora é a vez do jogador {jogador}")
#     print("")
 
# def exibe_resultado(): # mostra a atul situção do jogo da velha
#     for linhas in mesa:
#         for items in linhas:
#             if items == "":
#                 print("_ ",end="")
#             print(items,end=" ")
 
#         print(" ")
   
# while True: # pergunta a posição e o caractere ao usuário
#     linha = int(input("Qual a linha: "))
#     coluna = int(input("Qual a coluna: "))
#     caracter = input("Qual o caracter: ")
#     jogue_o_jogo(mesa,linha, coluna, caracter)
#     contador += 1
#     if contador == 9:
#         exibe_resultado()
#         break