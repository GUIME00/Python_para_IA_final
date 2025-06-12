# import pandas as pd
 
# # Carregar os dados
# df_filmes = pd.read_csv("IMDB-Movie-Data.csv")
 
# #Contar quantos filmes cada diretor dirigiu
# diretores_freq = df_filmes['Director'].value_counts().head(5)
# print("Diretores com mais filmes:")
# print(diretores_freq)
 
# # Ordenar os filmes pelo runtime e descrescente
# df_filmes['Runtime'] = df_filmes['Runtime'].str.replace(' min','')
# df_filmes['Runtime'] = pd.to_numeric(df_filmes['Runtime'], errors='coerce')
# filmes_mais_longos = df_filmes.sort_values(by='Runtime', ascending=False).head(10)
# print("\nTop 10 filmes mais longos:")
# print(filmes_mais_longos[['Series_Title', 'Runtime']])
 
# #Ordenar por 'Certificate' (ordem alfabética) e depois por 'Meta_score's
# df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')
# filmes_ordenados = df_filmes.sort_values(by=['Certificate', 'Meta_score'], ascending=[True, False])
# print("\nFilmes ordenados por Certificate e Meta_score:")
# print(filmes_ordenados[['Series_Title', 'Certificate', 'Meta_score']].head(5))
 
# #Agrupamento por 'Certificate'
# agrupado = df_filmes.groupby('Certificate').agg({
#     'Runtime': 'mean',
#     'Meta_score': 'mean',
#     'Series_Title': 'count'  # contar número de filmes
# }).rename(columns={'Title': 'Total_filmes'})
 
# print("\nEstatísticas por Certificate:")
# print(agrupado)