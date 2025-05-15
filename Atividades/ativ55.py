# #Atividade 55
palavra = input("Digite a primeira palavra: ")
palavra_ = input("Digite a segunda palavra: ")
if len(palavra) > len(palavra_):
    print(palavra)
elif len(palavra) < len(palavra_):
    print(palavra_)
else:
    print("As palavras tem o mesmo tamanho.")