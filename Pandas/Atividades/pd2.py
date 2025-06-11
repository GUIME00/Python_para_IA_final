# import pandas as pd

# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)

# titulos_filmes = df_filmes[['Series_Title','Released_Year','Director']] # 1.
# print(titulos_filmes.head())

# selecao_especifica = df_filmes.iloc[10:16,0:4] # 2.
# print("\nLinha 10 e 15 com a coluna 0 e 3.")
# print(selecao_especifica)

# df_temp = df_filmes.set_index('IMDB_Rating') # 3.
# top_5_rank = df_temp.loc[1:5, ['Series_Title','Gross']]
# print("\nFilmes que estão dentro do Top 5 no Rank com Receita: ")
# print(df_temp[['Series_Title','Gross']].head())

# df_filmes['Released_Year'] = pd.to_numeric(df_filmes['Released_Year'], errors='coerce') # 4.
# filmes_pos_2016 = df_filmes[df_filmes['Released_Year'] >= 2016][['Series_Title', 'Released_Year']]
# print("\nFilmes lançados desde 2016:")
# print(filmes_pos_2016)