# #Atividade 6 de Dicionário com Try e Except



# # Código utilizando a estutura KeyError
# # Dicionário com alguns dados
# pessoas = {
#     "Alice": 25,
#     "Bruno": 30,
#     "Carla": 22
# }

# # Função para buscar idade por nome
# def buscar_idade(nome):
#     try:
#         idade = pessoas[nome]
#         print(f"{nome} tem {idade} anos.")
#     except KeyError:
#         print(f"Erro: '{nome}' não está no dicionário.")

# # Testando a função
# buscar_idade("Bruno")    # Deve funcionar
# buscar_idade("Daniela")  # Deve disparar o KeyError e entrar no except

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome



# # Código utilizando a estrutura AttributeError
# # Criando um objeto do tipo Pessoa
# pessoa = Pessoa("Lucas")

# # Tentando acessar um atributo que não existe
# try:
#     print(pessoa.idade)
# except AttributeError:
#     print("Erro: O atributo 'idade' não existe no objeto 'Pessoa'.")



# #Código utilizzando a estrutura StopIteration
# # Criando um iterador manualmente a partir de uma lista
# numeros = iter([10, 20, 30])

# while True:
#     try:
#         numero = next(numeros)
#         print(f"Próximo número: {numero}")
#     except StopIteration:
#         print("Fim da iteração.")
#         break