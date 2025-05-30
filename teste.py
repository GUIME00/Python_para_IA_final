# #Teste 1
# numero = int(input("Digite o número: "))
# contador = 0
# elemento = ""
# coluna = 0
# while contador < numero:
#     while coluna < numero:
#         elemento += "letra"
#         coluna += 1
#     print(elemento)
#     contador += 1

# #Teste 2
# numero = int(input("Digite o número: "))
# contador = 0
# while contador < numero:
#     elemento = ""
#     coluna = 0
#     while coluna < numero:
#         if (coluna + contador) % 2 == 0:
#             elemento += "0"
#         else:
#             elemento += "1"
#         coluna += 1
#     print(elemento)
#     contador += 1

# #Teste 3
# def cumprimentar(nome):
#     print(f"Olá {nome}")
# def cumprimentar_vezes(nome, vezes):
#     while vezes > 0:
#         cumprimentar(nome)
#         vezes -= 1
# cumprimentar_vezes("Guime", 5)

# #Teste 4
# def resultado():
#     resultado = 25 + 25
#     return resultado
# def calculo(x):
#     soma = x + resultado()
#     print(soma)
# calculo (77)

# Teste 5 # Somando listas
# def lista_soma(str1,str2,str3):
#     resultado = []
#     for i in range (len(str1)):
#         soma = str1[i] + str2[i] + str3[i]
#         resultado.append(soma)
#     return resultado
    
# lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 22]
# lista2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# lista3 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(lista_soma(lista1,lista2,lista3))

# Teste de nada
# def mais_caracteres(txt):
#     frase = "O rato roeu a roupa do rei de Roma."
#     print(frase.count(all))
#     return max(frase)
# print(mais_caracteres())

# resposta = input("Deseja continuar? (s/n): ")
# if resposta.lower() == 's':
#     print("Continuando...")
# else:
#     print("Parando.")

# sudoku = [
#     [9, 0, 0, 0, 8, 0, 3, 0, 0],
#     [0, 0, 0, 2, 5, 0, 7, 0, 0],
#     [0, 2, 0, 3, 0, 0, 0, 0, 4],
#     [0, 9, 4, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 3, 0, 5, 6, 0],
#     [7, 0, 5, 0, 6, 0, 4, 0, 0],
#     [0, 0, 7, 8, 0, 3, 9, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 3],
#     [3, 0, 0, 0, 0, 0, 0, 0, 2]
#     ]

# for i in range(9):
#     for j in range(9):
#         if sudoku[i][j] == 0:
#             print("_", end=" ")
#         else:
#             print(sudoku[i][j], end=" ")
#         if (j + 1) % 3 == 0 and j < 8:
#             print("|", end=" ")
#     print()
#     if (i + 1) % 3 == 0 and i < 8:
#         print("-" * 21)

# Teste Jogo da Velha

# def jogueOjogo(mesa: list, x: int, y: int, caracter: str):
#     if 0 <= x < 3 and 0 <= y < 3:
#         if mesa[x][y] == " ":
#             mesa[x][y] = caracter
#         else:
#             print("A posição já está ocupada.")
#     else:
#         print("Coordenadas inválidas.")
# jogo_da_velha = [
#                 [" "," "," "],
#                 [" "," "," "],
#                 [" "," "," "]
#                 ]
# jogueOjogo(jogo_da_velha, 0, 0, "O")
# jogueOjogo(jogo_da_velha, 1, 1, "X")
# jogueOjogo(jogo_da_velha, 2, 2, "X")
# jogueOjogo(jogo_da_velha, 0, 1, " ")
# jogueOjogo(jogo_da_velha, 1, 0, " ")
# jogueOjogo(jogo_da_velha, 1, 2, "O")
# jogueOjogo(jogo_da_velha, 2, 1, "O")
# jogueOjogo(jogo_da_velha, 0, 2, "X")
# jogueOjogo(jogo_da_velha, 2, 0, "X")

# for linha in jogo_da_velha:
#     print("|".join(linha))

# lista = {"Julia": "99999-9999", "Bruna": "98999-9999", "Amanda": "98799-9999", "Guilherme": "98769-9999", "Holandda": "98765-9999", "Pedro": "98765-4999"}
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