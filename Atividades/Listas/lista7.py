# #Atividade 7 de Lista
lista_de_produtos = ['Alvejante', 'Deterjente', 'Sabonete', 'Sabão em barra', 'Sabão em pó', 'Esponja']
def produtosLista(lista_de_produtos):
    while True:
        produto = input("Digite o produto que está procurando ou digite Sair para encerrar: ")
        if produto in lista_de_produtos:
            print("Produto encontrado.")
            produtosLista(lista_de_produtos)
        elif produto == 'Sair':
            ("Encerrando programa.")
            break
        else:
            print("Produto está fora do catálogo.")
            produtosLista(lista_de_produtos)
produtosLista(lista_de_produtos)