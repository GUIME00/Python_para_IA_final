try:
    with open('Atividades/Arquivos/dados.csv','r') as arquivo:
        total_linhas = 0
        for linha in arquivo:
            total_linhas += 1
    print(f"O arquivo contém {total_linhas} linha(s).")
    with open('Atividades/Arquivos/dados_maiores.csv','x') as arquivoes:           
        
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")