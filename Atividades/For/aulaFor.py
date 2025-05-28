# forforforforforforforforforforforforforforforforforforforforforforforforforforforforforfor

# lista = ["Maria", "Madalena", "Pedro", "Paulo", "Alex"]
# for nome in lista:
#     if len(nome) > 2:
#         print(f"O {nome} tem mais de 2 caracteres.")
#     else:
#         print(f"O {nome} tem menos de 2 caracteres.")

# caractere = syntax #caractere tem a mesma função de syntax
# string = input("Digite uma palavra: ")
# for syntax in string:
#     print(f"*{string}")

# Prática
# txt = input("Digite uma palavra: ")
# for caractere in txt:
#     print(caractere, end="*")

# txt = input("Digite uma palavra: ")
# for caractere in txt:
#     print(caractere + "*")


# Range no for

# Conta de 0 até 99
# for i in range(100):
#     print(i)
# Conta de 10 até 99
# for i in range(10, 100):
#     print(i)
# Vai contar de 0 até 10, mas de 2 em 2 (0, 2, 4, 6, 8)
# for j in range(0, 10, 2):
#     print(j)

# n = int(input("Digite um número: "))
# if n < 0:
#     n = (n*-1)
# for i in range(-n, n):
#     print(i)

# Prática

# #Vertical

# n = int(input("Digite um número positivo: "))
# if n > 0:
#     for i in range(-n, n +1):
#         if i != 0:
#             print(i)
# else:
#     print("O número deve ser positivo.")

# #Horizontal

# n = int(input("Digite um número positivo: "))
# if n > 0:
#     for i in range(-n, n +1):
#         if i != 0:
#             print(i, end=" ")
# else:
#     print("O número deve ser positivo.")


# #Criando uma lista partindo do Range

# num = list(range(3, 15))
# print(num)

# num = list(range(3, 15))
# print(num[7])

# num = list(range(3, 15))
# print(num)
# for i in num:
#     print(i)

# .count(): conta quantas vezes uma string ou inteiro há dentro de um conjunto de dados. 

# minha_string = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeiras?"
# print(minha_string.count("a"))

# minha_lista = [1,2,3,4,4,4,6,6,8,9,9]
# print(minha_lista.count(9))

# Replace

# minhaString = "Olá, Oi, Oi, Amigos"
# novaString = minhaString.replace("Amigos", "Friends")
# print(novaString)

# minhaString = "Oi, Oi, Oi, Amigos"
# novaString = minhaString.replace("Oi", "Olá")
# print(novaString)

# Prática
# frase = "O rato roeu a roupa do rei de roma."
# def mais_caracteres(txt):
    
#     maior_caractere = ""
#     maior_contagem = 0

#     for caractere in txt:
#         contagem = txt.count(caractere)
#         if contagem > maior_contagem:
#             maior_contagem = contagem
#             maior_caractere = caractere
#     return maior_caractere
# print(mais_caracteres(frase.replace(" ","")))


# Lower
# A estrutura .lower() é um método de string que serve para converter todos os caracteres de uma string para letras minúsculas.
# texto = "Python É Legal"
# texto_minusculo = texto.lower()
# print(texto_minusculo)


# lista_bidimensional = [
#     [0,1,2,3],
#     [5,6,8,9],
#     [1,8,2,3],
#     [4,5,6,7]
#     ]                   # x, y # x = linha e y = coluna
# print(lista_bidimensional[2][2])
# print(lista_bidimensional[2][0])
# print(lista_bidimensional[0][2])
# print(lista_bidimensional[0][3])
# print(lista_bidimensional[3][3])
# print(lista_bidimensional[0]) # Imprime a linha inteira
# print(lista_bidimensional[1]) # Imprime a linha inteira
# print(lista_bidimensional[2]) # Imprime a linha inteira
# print(lista_bidimensional[3]) # Imprime a linha inteira

# Prática

# def conta_elementos_match(minha_matriz: list, elemento: int): 
#     contador = 0
#     for linha in minha_matriz:
#         for item in linha:
#             if item == elemento:
#                 contador += 1
#     return contador
# tabela = [
#     [0,1,2,3],
#     [5,6,8,9],
#     [2,8,4,0],
#     [4,5,2,7]
#     ]
# resultado = conta_elementos_match(tabela,2)
# print(f"O número 2 aparece {resultado} vezes na tabela.")