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