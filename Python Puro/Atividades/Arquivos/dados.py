# try:
#     with open('Atividades/Arquivos/dados.csv','r') as arquivo:
#         with open('dados_maiores.csv','w') as arquivoes:           
#             for linha in arquivo: 
#                 linha = linha.replace("\n","")                
#                 if linha:
#                     partes = linha.split(",")
#                     nome = partes[0]
#                     idade = partes[1]
#                     if int(idade) >= 18:
#                         arquivoes.write(linha + "\n")
#     print("Arquivo 'dados_maiores' foi criado.")

# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# except ValueError:
#     print("Erro: Verifique se o arquivo está no formato 'nome','idade'.")