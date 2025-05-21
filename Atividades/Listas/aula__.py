#Lista: Conceito
#São estruturas de dados mais versáteis e usadas em Python. Os valores contidos na listas são chamadas de itens.

# minha_lista = [0,10,20,30]
# print(minha_lista[0])
# print(minha_lista[1])
# print(minha_lista[2])
# print(minha_lista[3])

# resultado = print(minha_lista[1]) + print(minha_lista[3]) #Soma os elementos int/float da lista
# print(resultado)
# tamanho = len(minha_lista) #Mostra os elementos dentro da lista
# print(tamanho)

# #Append
# numeros = []
# numeros.append(1)
# numeros.append(2)
# numeros.append(3)
# numeros.append(4)
# numeros.append(5)
# print(numeros)

# #Append na Prática
# listaVazia = []
# while True:
#     item = input("Digite o item que deseja adicionar: ")
#     if item == 0:
#         print("Programa encerrado.")
#         print(f"Lista final: {listaVazia}")
#         break
#     else:
#         listaVazia.append(item)
#         print(listaVazia)

# quantidade = int(input("Quantos números deseja adicionar? "))
# listaNumeros = []
# contador = 0
# while contador < quantidade:
#     numero = int(input(f"Item número {contador + 1}. Digite o número que desejar: "))
#     listaNumeros.append(numero)
#     contador += 1
# print("Lista final:", listaNumeros)

# #Insert
# frutas = ["maçã", "banana", "laranja"]
# frutas.insert(1, "abacaxi")
# print(frutas)

# #Extend
# lista_1 = [1, 2]
# lista_2 = [3, 4, 5]
# lista_1.extend(lista_2)
# print(lista_1)

# #Remove
# lista = [10, 20, 30, 20, 40]
# lista.remove(20)
# print(lista)

# #Pop
# lista = [5, 10, 15, 20]
# lista.pop(3)
# lista.pop(0)
# print(lista)

# #Clear
# lista = ["strogonoff", "carne de panela", "batata", "suflê"]
# lista.clear()
# print(lista)

# #Index
# lista = ['a', 'b', 'c', 'd']
# print(lista.index('c'))

# #Count
# lista = [7, 1, 7, 3, 7, 5]
# print(lista.count(7))

# #Sort
# lista = [12, 4, 19, 1, 8]
# lista.sort()
# print(lista)
# lista.sort(reverse = True)
# print(lista)

# #Sort + Reverse
# lista = [1, 2, 3, 4, 5]
# lista.sort(reverse=True)
# print(lista)

# #Teste
# lista = [1, 2, 3, 4, 5]
# numero = int(input("Digite um número: "))
# while lista[0] != -1:
#     if numero == -1:
#         lista[0] = -1
#         print("Número inserido")
#         print(lista)
#         break
#     else:
#         print("Tente outro número.")

#Prática
# lista = [1, 2, 3, 4, 5]
# while True:
#     print("Lista atual:", lista)
#     indice = int(input("Digite o índice que deseja alterar (-1 para encerrar): "))
#     if indice == -1:
#         print("Encerrado.")
#         break
#     if 0 <= indice < len(lista):
#         novo_numero = int(input("Digite o número que deseja inserir: "))
#         lista[indice] = novo_numero
#     else:
#         print("Tente outro índice.")
# print("Lista atual:", lista)

# #Fatiar listas
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(letters[1:4]) # Tira o primeiro até o quarto índice
# print(letters[:3]) # Tira os três últimos índices
# print(letters[3:]) # Tira os três primeiros índices
# print(letters[::2]) # Tira os índices com passo 2
# print(letters[::-1]) #Inverte a ordem da lista

# #Prática

lista = []
while True:
    print("Lista atual",lista)
    escolha = input("Digite + para adicionar, - para remover ou 0 para sair: ")