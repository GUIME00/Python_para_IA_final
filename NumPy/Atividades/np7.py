# import numpy as np

# Minha versão
# def somar_matrizes(i,j):
#     if len(array_) != len(_array_):
#         print("Erro: arrays de tamanhos diferentes.")
#     else:
#         soma = i + j
#         return np.array(soma)
# array_ = np.array([[1,2,5,10,20],[1,2,5,10,20]])
# _array_ = np.array([[20,10,5,2,1],[20,10,5,2,1]])
# print(somar_matrizes(array_,_array_))


# Versão do professor

# def somar_matrizes(i,j):
#     if np.shape(i) == np.shape(j):
#         return i + j
#     else:
#         return "Erro: arrays de tamanhos diferentes."

# m1 = np.array([[1, 2], [3, 4]])
# m2 = np.array([[5, 6], [7, 8]])
# print(somar_matrizes(m1,m2))