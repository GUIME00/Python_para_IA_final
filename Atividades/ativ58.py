# #Atividade 58
string = input("Digite o que quiser: ")
largura = 30
espacos = largura - 2 - len(string)
esquerda = espacos // 2
direita = espacos - esquerda
print("*" * largura)
print("*" + " " * esquerda + string + " " * direita + "*")
print("*" * largura)