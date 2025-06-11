import pandas as pd

df_filmes = pd.read_csv("IMDB-Movie-Data.csv")
print(df_filmes.isna().sum())
df_sem_nan_colunas = df_filmes.dropna(axis=1)