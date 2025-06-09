# import pandas as pd  # Importa a biblioteca pandas com o apelido pd

# # Cria um dicionário com dados de exemplo
# data = {
#     'Nome': ['Ana', 'Bruno', 'Carla', 'Diego'],  # Lista de nomes
#     'Idade': [23, 35, 29, 42],                   # Lista de idades
#     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte']  # Lista de cidades
# }

# # Transforma o dicionário em um DataFrame, que é uma tabela semelhante a uma planilha
# df = pd.DataFrame(data)

# # Exibe o DataFrame original no terminal
# print("DataFrame original:")
# print(df)

# # Filtra o DataFrame para mostrar apenas as pessoas com idade maior que 30
# # df['Idade'] > 30 cria uma série booleana (True/False)
# df_maiores_30 = df[df['Idade'] > 30]

# # Exibe as pessoas que têm mais de 30 anos
# print("\nPessoas com mais de 30 anos:")
# print(df_maiores_30)

# # Adiciona uma nova coluna ao DataFrame chamada 'Idade_em_meses'
# # Essa coluna é a idade multiplicada por 12 (conversão para meses)
# df['Idade_em_meses'] = df['Idade'] * 12

# # Exibe o DataFrame atualizado com a nova coluna
# print("\nDataFrame com idade em meses:")
# print(df)