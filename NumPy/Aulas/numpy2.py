import numpy as np

# aqui é uma variável que representa o método .default_rng()
rng = np.random.default_rng()

# Criar Array apartir de listas e tuplas
lista_py = [1,2,3,4,5,6]
print(lista_py) # Lista
array_1d = np.array(lista_py)
print(array_1d) 
# Array 50X mais rápido que lista

# np.array converte tuplas e listas em array
lista2_py = [[1,2,3,4],[4,3,2,1]]
array_2d = np.array(lista2_py)
print(array_2d)

tupla = (1, "Python", 3.14) # Definida com (p(a(r(ê(n()t)e)s)e)s)
tupla_ = (1,2,3,4,5,6,7,8,9,10)
array_tupla = np.array(tupla_)
print(array_tupla)

# np.zeros
# cria um array preenchido por zeros

# x-linhas e y-colunas x,y
zero_array = np.zeros((2,3))
print(f"Array de zeros: {zero_array}")

zero_array_ = np.zeros((2,3),int)
print(f"Array de zeros: {zero_array_}")

# np.ones
one_array = np.ones((2,3),int)
print(f"Array de uns: {one_array}")

# np.full
# cria um array preenchido com números específicos
full_array = np.full((2,4),7.5)
print(full_array)

# np.arange
#                        x,y,z  x-nº inicial  y-nº final  z-nº contagem
array_arange = np.arange(0,10,2)
print(array_arange)

array_arange_float = np.arange(0.0,1.0,0.25)
print(array_arange_float)

# array de nºs aleatórios
array_aleatorios = rng.random((2,5))
print(array_aleatorios)

array_aleatorios2 = rng.integers(0,1000,size=10)
print(array_aleatorios2)

# índice NumPy
array_indice = np.array([1,2,5,9,8])
print(f"elemento 0: {array_indice[0]}")
print(f"elemento 3: {array_indice[3]}")

# índice matriz
array_indice2 = np.array([[1,2,5,8,9],
                          [5,9,8,7,6]])
print(f"Elemento na linha 0, coluna 2: {array_indice2[0,2]}") # saída - 5

# Slicing
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 12, 13],
                  [14, 7, 15, 16]])
# x-lin e y-col   x   y
fati2d_a = arr2d[:2, 1:3] # [:] é pra "fatiar"
print(fati2d_a)

# operações matemáticas
array_a = np.array([1,3,5,7])
array_b = np.array([2,4,6,8])
# saídas --------- [3 7 11 15]
# saídas --------- [-1 -1 -1 -1]
# saídas --------- [2 12 30 56]
# saídas --------- [0.5 0.75 0.83333333 0.875]
# Adição
soma = array_a + array_b
print(soma)
# Subtração
sub = array_a - array_b
print(sub)
# Multiplicação
mult = array_a * array_b
print(mult)
# Divisão
div = array_a / array_b
print(div)

# .copy() e .view()
precos = np.array([150.00,10.99,20.50])
print(f"Preços: {precos}")

precoAjustado = precos
print(precos[0] * 2)

# .copy() faz uma cópia de outra qualquer alteração na cópia sem alterar a original
precoAjustado2 = precos.copy()

# iteração
array = np.array([1,2,3,4,5,6,7,8,9,1,25,50])
for n in array:
    print(f"Valor: {n}")