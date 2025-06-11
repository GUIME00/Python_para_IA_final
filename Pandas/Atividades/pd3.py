# import pandas as pd

# df_filmes = pd.read_csv("IMDB-Movie-Data.csv")

# df_filmes['Rating_Metascore_Diff'] = df_filmes['IMDB_Rating'] - (df_filmes['Meta_score'] / 10) # 1.
# print(df_filmes.head())

# filmes_selecionados = df_filmes[['Series_Title','IMDB_Rating','Rating_Metascore_Diff']] # 2.
# print(filmes_selecionados.head())

# df_filmes['Description'] = df_filmes.drop('Overview') # 3.
# print(df_filmes.head())

# df_filmes['Numero_Votos'] = df_filmes['No_of_Votes'] # 4.
# print(df_filmes['Numero_Votos'] == df_filmes['No_of_Votes'])