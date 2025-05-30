# Esse código define uma variável de string a com o valor "Hello World!". 
# A sintaxe [::-1] é usada para cortar a cadeia de caracteres em ordem inversa, invertendo efetivamente a ordem dos caracteres na cadeia. 
# A função print() é então usada para enviar a string invertida para o console. O resultado desse código será "!dlroW olleH".

a = "Hello World!"
print(a[::-1])

# Esse trecho de código foi escrito em Python. As duas primeiras linhas de código atribuem os valores 10 e 5 às variáveis a e b, respectivamente. 
# A instrução print na terceira linha usa uma string f para imprimir os valores de a e b dentro de uma tupla. O resultado dessa instrução print é "First: (10, 5)".
# A quarta linha de código usa o desempacotamento de tuplas para atribuir o valor de b a a e o valor de a + 2 a b. 
# Isso significa que a agora tem o valor de 5 e b tem o valor de 12. 
# A segunda instrução print usa outra string f para imprimir os novos valores de a e b dentro de uma tupla. 
# O resultado dessa instrução print é "Second: (5, 12)".

a = 10
b = 5
print(f"First: {a, b}")


a, b = b, a + 2
print(f"Second: {a, b}")

# Esse código usa o Python para atribuir os valores de 1, 2 e 3 às variáveis a, b e c, respectivamente, usando o desempacotamento de tuplas. 
# Em seguida, ele imprime os valores de a, b e c em linhas separadas usando a função print(). 
# A saída desse código será: 1 2 3 Isso significa que os valores de a, b e c foram atribuídos e impressos com sucesso.

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

# Esse código importa o módulo sys e define uma lista a e uma tupla b, ambas contendo os mesmos elementos.
# Em seguida, ele usa a função sys.getsizeof() para determinar o tamanho de cada objeto em bytes e imprime os resultados usando f-strings.
# Por fim, ele gera o tamanho da lista e da tupla em bytes. A função sys.getsizeof() retorna o tamanho de um objeto em bytes, incluindo qualquer sobrecarga.
# Nesse caso, ele é usado para comparar o tamanho de uma lista e de uma tupla, que são usadas para armazenar coleções de elementos no Python.
# O resultado mostra que a tupla é menor em tamanho do que a lista, porque as tuplas são imutáveis e exigem menos sobrecarga do que as listas, que podem ser redimensionadas e modificadas.

import sys

a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(a)} bytes")
print(f"Tuple size: {sys.getsizeof(b)} bytes")

# Esse código cria uma lista a com os valores [1,2,3,4,5].
# Em seguida, ele modifica o valor no índice 2 (que é o terceiro elemento da lista) para ser 8 usando o operador de atribuição =.
# Por fim, ele imprime a lista modificada usando a função print().
# A saída mostra que o valor no índice 2 foi alterado para 8, resultando na lista [1,2,8,4,5].

a = [1,2,3,4,5]
a[2] = 8
print(a)

# Esse código cria dois objetos, a e b, usando a compreensão de lista e a expressão geradora, respectivamente.
# Na primeira linha, a é criado usando a compreensão de lista.
# Ele cria uma lista de números multiplicando cada número no intervalo de 0 a 9 por 2.
# Isso resulta em uma lista de números pares de 0 a 18. Na segunda linha, b é criado usando a expressão geradora.
# Ele cria um objeto gerador que produz a mesma sequência de números pares de 0 a 18.
# A diferença entre uma lista e um gerador é que uma lista armazena todos os valores na memória,
# enquanto um gerador produz um valor de cada vez e não armazena todos os valores na memória de uma só vez.
# Isso pode ser útil para grandes conjuntos de dados em que o uso da memória é uma preocupação.
# Por fim, os comandos print imprimem os valores de a e b. 
# A saída mostra a lista de números pares para a e o local da memória do objeto gerador para b.

a = [x * 2 for x in range(10)]
b = (x * 2 for x in range(10))

print(a)
print(b)

# Testando o comando .join()

palavras = ['eu', 'estou', 'aprendendo','Python']
frase = ' '.join(palavras)
print(frase)

frutas = ['maçã', 'banana', 'laranja']
resultado = ', '.join(frutas)
print(resultado)

letras = ['P', 'y', 't', 'h', 'o', 'n']
palavra = ''.join(letras)
print(palavra)