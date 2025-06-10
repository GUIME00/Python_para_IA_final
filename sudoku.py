# import copy

# tabuleiro_inicial = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
#     ]

# tabuleiro = copy.deepcopy(tabuleiro_inicial)


# def exibir_tabuleiro(tab):
#     print("\nTabuleiro Atual:")
#     for i, linha in enumerate(tab):
#         if i % 3 == 0 and i != 0:
#             print("-" * 21)
#         for j, val in enumerate(linha):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")
#             print(val if val != 0 else ".", end=" ")
#         print()
#     print()

# def entrada_valida(valor):
#     return valor.isdigit() and 1 <= int(valor) <= 9

# def posicao_valida(x, y):
#     return 0 <= x <= 8 and 0 <= y <= 8

# def verificar_regra(tab, x, y, num):
#     # Verifica linha
#     if num in tab[x]:
#         return False
#     # Verifica coluna
#     for i in range(9):
#         if tab[i][y] == num:
#             return False
#     # Verifica subgrade 3x3
#     sub_x = (x // 3) * 3
#     sub_y = (y // 3) * 3
#     for i in range(3):
#         for j in range(3):
#             if tab[sub_x + i][sub_y + j] == num:
#                 return False
#     return True

# def atualizar_tabuleiro(tab, x, y, num):
#     tab[x][y] = num

# def verificar_conclusao(tab):
#     for i in range(9):
#         for j in range(9):
#             if tab[i][j] == 0 or not verificar_regra(tab, i, j, tab[i][j]):
#                 return False
#     return True

# def jogar_sudoku():
#     exibir_tabuleiro(tabuleiro)

#     while True:
#         try:
#             x = int(input("Digite a linha (0-8): "))
#             y = int(input("Digite a coluna (0-8): "))
#             if not posicao_valida(x, y):
#                 print("Posição inválida. Tente novamente.")
#                 continue
#             if tabuleiro_inicial[x][y] != 0:
#                 print("Essa posição já está preenchida e não pode ser alterada.")
#                 continue
#             num = int(input("Digite um número de 1 a 9: "))
#             if not entrada_valida(str(num)):
#                 print("Número inválido. Digite de 1 a 9.")
#                 continue
#             if verificar_regra(tabuleiro, x, y, num):
#                 atualizar_tabuleiro(tabuleiro, x, y, num)
#                 exibir_tabuleiro(tabuleiro)
#                 if verificar_conclusao(tabuleiro):
#                     print("Parabéns! Você completou o Sudoku!")
#                     break
#             else:
#                 print("Movimento inválido! Viola as regras do Sudoku.")
#         except ValueError:
#             print("Entrada inválida. Por favor, digite números válidos.")

# jogar_sudoku()