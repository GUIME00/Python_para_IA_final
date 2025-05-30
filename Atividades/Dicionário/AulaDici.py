# meu_dicionario = {}
# meu_dicionario["apina"] = "macaco"
# meu_dicionario["nome"] = "Guilherme"

# print(meu_dicionario)
# print(meu_dicionario["nome"])

# palavra = input("Digite uma palavra: ")
# if palavra in meu_dicionario:
#     print("Tradução:", meu_dicionario[palavra])
# else:
#     print("Palavra não encontrada.")

# resultado = {}
# resultado["Julia"] = 5
# resultado["Holanda"] = 10

# soma = resultado["Julia"] + resultado["Holanda"]
# print(soma)

# dicionario = {}

# dicionario["apina"] = "Macaco" 
# dicionario["banana"] = "Amarelo" 
# dicionario["cembalo"] = "Cravo"

# for chave in dicionario:
#     print("Chave",chave)
#     print("valor",dicionario[chave])

# lista_palavras = [
#                 "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#                 "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#                 "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
#                 ]

# def contagens(minha_lista):
#     palavras = {} # "chave":"valor"
#     for palavra in minha_lista:
#         if palavra not in palavras:
#             palavras[palavra] = 0
#         palavras[palavra] += 1
#     return palavras
# print(contagens(lista_palavras))

# Prática

# Método 1
# def histogram(str):
#     contagem = {}
#     for letra in str:    
#         if letra in contagem:
#             contagem[letra] += 1
#         else:
#             contagem[letra] = 1
#     for letra in sorted(contagem):
#         print(f"{letra}{'*' * contagem[letra]}")
# histogram('juliaholandda')

# Método 2
# def histogram(txt: str1):
#     contagem = {}
#     for letra in txt:
#         if letra in contagem:
#             contagem[letra] += 1
#         else:
#             contagem[letra] = 1
#     for letra in contagem:
#         print(letra + ": " + "*" * contagem[letra])
# histogram('guilherme brasil pereira')

# Comando del

# staff = {"Alan":"Professor","Emily":"Aluna","David":"Professor"}
# print(staff)

# del staff["Alan"]
# print(staff)

# Comando .pop()

# deletado = staff.pop("Emily")
# print(deletado)

# Estruturar dados com Dicionário
# pessoa1 = {"nome": "Peppa","Altura": 175,"Peso": 105,"idade":14}
# pessoa2 = {"nome": "Lilo","Altura": 100,"Peso": 30,"idade":8}
# pessoa3 = {"nome": "Ariel","Altura": 180,"Peso": 65,"idade":18}

# pessoal = [pessoa1, pessoa2, pessoa3]

# for pessoa in pessoal:
#     print(f"Nome: {pessoa["nome"]}")
#     print(f"Altura: {pessoa["Altura"]}")
#     print(f"Peso: {pessoa["Peso"]}")
#     print(f"Idade: {pessoa["idade"]}")
#     print(" ")

# altura_de_nos_todos = 0

# for pessoa in pessoal:
#     altura_de_nos_todos += pessoa["Altura"]

# print(altura_de_nos_todos)