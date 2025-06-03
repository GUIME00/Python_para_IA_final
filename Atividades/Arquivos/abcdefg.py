with open('Atividades/Arquivos/pessoas.csv') as novoArquivo:
    for linha in novoArquivo:
        linha = linha.replace("\n","")
        partes = linha.split(";")
        nome = partes[0]
        notas = partes[1:]
        print("Nome:", nome)
        print("Nota:", notas)