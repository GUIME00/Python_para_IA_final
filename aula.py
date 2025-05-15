# #Estruturas lógicas: Operadores de atribuição
# #Usados para atribuir valores para as variáveis
# valor = 10
# print(valor)
# valor += 5
# print(valor)
# valor *= 7
# print(valor)
# valor -= 33
# print(valor)
# valor /= 8
# print(valor)
# valor **= 2
# print(valor)
# valor %= 9
# print(valor)

# #Estruturas lógicas: Operadores de comparação
# n1 = 10
# n2 = 20
# n3 = 30
# n4 = 40
# print(n1 > n2 and n2 < n3) #Tem uma condição para ser False
# print(n1 < n2 and n2 > n3) #Tem uma condição para ser False
# print(n1 != n2 or n3 == n4) #Tem uma condição para ser True
# print(n1 == n2 or n3 != n4) #Tem uma condição para ser True

# if n1 != n2 and n3 != n4:
#     print("Verdadeiro!")
# else:
#     print("Falso!")

# numero = int(input("Entre com um número: "))
# if numero < 0:
#     print("Esse número é negativo.")
# if numero > 0:
#     print("Esse número é positivo.")
# if numero == 0:
#     print("O número é 0.")

# #Estruturas lógicas: Estrutura condicional: IF, ELSE, ELIF:

# senha_correta = "python123"
# for tentativas in range(3, 0, -1):
#     senha = input("Digite a senha: ")
#     if senha == senha_correta:
#         print("Acesso concedido!")
#         break
#     elif tentativas > 1:
#         print(f"Senha incorreta. Tentativas restantes: {tentativas - 1}")
#     else:
#         print("Acesso bloqueado! Tentativas esgotadas.")


# num_ = int(input("Digite uma número inteiro: "))
# if num_ == 1984:
#     print("Orwell")
# else:
#     print("Erroooooouuuuu!!!")