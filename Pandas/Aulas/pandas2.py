import pandas as pd

url_filmes = "IMDB-Movie-Data.csv" # "Construir" o caminho para o arquivo
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com succeso!")

# # .head() # "Topo"

# print(f"Primeiras 5 linhas de DataFrame de filmes:\n{df_filmes.head()}")

# # .tail() "Base"

# print(f"\nÚltimas 5 linhas de DataFrame de filmes:\n{df_filmes.tail()}")

# # .info()

# print(f"\nInformações sobre o DataFrame: {df_filmes.info()}")

# # .shape()

# print(f"\nO DataFrame de filmes têm:\n{df_filmes.shape[0]} linhas e {df_filmes.shape[1]} colunas.")

# # .describe()
# # gera estatística descritiva do DataFrame

# print("\nEstatística descritiva do DataFrame:")
# print(df_filmes.describe())

# # .index()
# # traz informações sobre índices das linhas

# print("\nInformações do índice:")
# print(df_filmes.index)

# # Selecionando a coluna 'Title'
# titulos_filmes = df_filmes['Series_Title']
# print("Primeiros 5 títulos.")
# print(titulos_filmes.head())

# # Selecionando múltiplas colunas
# filmes_selecionados = df_filmes[['Series_Title','Genre','IMDB_Rating']]
# print(f"\nDataFrame com título, Gênero e Nota.")
# print(filmes_selecionados.head())

# # Selecionando a primeira linha
# # Iloc é usado para selecionar linhas por índice numérico
# primeira_linha = df_filmes.iloc[200]
# print(f"\nPrimeira linha selecionada.")
# print(primeira_linha)

# # Selecionando as 3 primeiras linhas
# tres_linhas = df_filmes.iloc[0:3]
# print('\nTrês primeiros filmes (DataFrame):')
# print(tres_linhas)

# # Selecionando linhas e colunas específicas
# selecao_especifica = df_filmes.iloc[[0,3],[5,6]]
# print("\n Printando uma seleção específica. \nLinha 0 e 3 com a coluna 5 e 6.")
# print(selecao_especifica)

# # Selecionando Dados com .loc
# # Localiza os dados pelos rótulos
# df_filmes_idx = df_filmes.set_index('Series_Title')
# print('\n Definimos o índice agora como Series Titles.')
# print(df_filmes_idx.head())

# poderoso = df_filmes_idx.loc['The Godfather']
# print("\nDados do filme: The Godfather: ")
# print(poderoso)

# # Filtrar os Dados baseados em condições (Boolean indexing0)
# df_filmes_bem_avaliados = df_filmes[df_filmes['IMDB_Rating'] >= 8.5]
# print("\n Filmes com nota >= 8.5 (Primeiras linhas).")
# print(df_filmes_bem_avaliados['Series_Title'].head()) # Aparece só o título dos filmes

# # Filmes que têm gênero 'Action'
# filmes_acao = df_filmes[df_filmes['Genre'].str.contains('Action', na=False)]
# print(" \n Filmes que contém o gênero 'Action'")
# print(filmes_acao[['Series_Title', 'Genre']].head())