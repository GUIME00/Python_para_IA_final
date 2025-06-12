# import pandas as pd

# df_filmes = pd.read_csv("IMDB-Movie-Data.csv")

# print("Valores ausentes por coluna:") # 1.
# print(df_filmes[['Gross','Meta_score']].isna().sum())

# df_filmes_completo = df_filmes.dropna()

# print(f"\nNúmero de linhas no DataFrame original: {len(df_filmes)}") # 2.
# print(f"Número de linhas após remover todas com Nan: {len(df_filmes_completo)}")

# df_filmes_completo['Gross'] = df_filmes_completo['Gross'].str.replace(',','.')
# df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')
# df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')
# print(df_filmes_completo['Gross'])

# df_filmes_preenchido_media = df_filmes.copy()

# df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
# df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].median())

# print("\nValores ausentes após preenchimento:") # 3.
# print(df_filmes_preenchido_media[['Gross','Meta_score']].isna().sum())