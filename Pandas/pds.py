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

# import pandas as pd

# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)
# contagem_diretores = df_filmes['Director'].value_counts()
# print(f"\nOs 5 diretores mais frequentes sucessivamente: {contagem_diretores.head()}")

# duracao_filmes = df_filmes['Runtime'].value_counts()
# print(f"\nOs 10 filmes mais longos sucessivamente: {duracao_filmes.head(10)}")

# certificado_filmes = df_filmes['Certificate'].sort_values()
# print(f"\nOrdem alfabética da lista de filmes: {certificado_filmes.head()}")

# score_filmes = df_filmes['Meta_score'].sort_values()
# print(f"\nOrdem lista de filmes: {score_filmes.head()}")