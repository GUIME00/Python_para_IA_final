# with open('Atividades/Arquivos/pessoas.csv') as novoArquivo:
#     for linha in novoArquivo:
#         linha = linha.replace("\n","") # Replace substitui
#         partes = linha.split(";") # Split pega uma string inteira e substitui
#         nome = partes[0]
#         notas = partes[1:]
#         print("Nome:", nome)
#         print("Nota:", notas)

# with open("dados.txt") as arquivo:
#     f = arquivo.readlines()
#     print(f[2])
#     print(f[0])
#     print(f[3])
#     print(f[1])

# with open ("dados2.txt","a") as arquivo:
#      # "a" : adiciona uma nova linha de texto ao arquivo
#      # "w" : exclui as linhas anteriores e adiciona uma nova linha de texto
#      # "x" cria um novo arquivo e adiciona uma nova linha de texto
#     f = arquivo
#     f.write("Eu adoro ler")