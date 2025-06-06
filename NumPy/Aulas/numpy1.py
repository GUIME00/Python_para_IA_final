# import numpy as np # mudar o nome numpy para np

# # Saída o array e as dimensões pelo método(ndim)
# arr1d = np.array([1,2,3])
# print(f"Array 1D: {arr1d}, Dimensões: {arr1d.ndim}") # (ndim - number dimension/ nº de dimensões = 1)

# arr2d = np.array([[1,2,3,4,5],[5,6,7,8,9]])
# print(f"Array 2D: {arr2d}, Dimensões: {arr2d.ndim}") # (ndim - number dimension/ nº de dimensões = 2)


# arr3d = np.array([[[3,4,5],[1,2,3]],[[5,6,7],[8,9,6]]])
# print(f"Array 3D: {arr3d}, Dimensões: {arr3d.ndim}") # (ndim - number dimension/ nº de dimensões = 3)

# # Shape
# # Indica o tamanho da array
# print(f"Shape do arr1d: {arr1d.shape}")
# print(f"Shape do arr2d: {arr2d.shape}")
# print(f"Shape do arr3d: {arr3d.shape}")

# # Dtype
# array_float = np.array([1.5,1.8,9.5])
# print(f"O dtype dessa array é: {array_float.dtype}")
# print(f"O dtype dessa array é: {arr1d.dtype}")

# # Itemsize
# # Retorna o comprimento de cada elemento da matriz em bytes
# print(f"O itemsize do arr1d é: {arr1d.itemsize}.")
# print(f"O itemsize do arr3d é: {arr3d.itemsize}.")
# print(f"O itemsize do array_float é: {array_float.itemsize}.")

# Prática
# array_1 = np.array([1,2,3,4,5]) # Cinco elementos
# print("nº de dimensões" , array_1.ndim)
# print("formato" , array_1.shape)
# print("nº total de elementos" , array_1.size)
# print("tipo de dados" , array_1.dtype)
# print("tamanho de cada elemento em bytes" , array_1.itemsize)

# array_2 = np.array  ([
#                     [1.1,2.2,3.3],
#                     [7.7,8.8,9.9] # Duas linha por três colunas
#                     ])
# print("nº de dimensões" , array_2.ndim)
# print("formato" , array_2.shape)
# print("nº total de elementos" , array_2.size)
# print("tipo de dados" , array_2.dtype)
# print("tamanho de cada elemento em bytes" , array_2.itemsize)

# array_3 = np.array([[[1,2,3],[3,2,1]],[[4,5,6],[6,5,4]],[[7,8,9],[9,8,7]]])
# print("nº de dimensões" , array_3.ndim)
# print("formato" , array_3.shape)
# print("nº total de elementos" , array_3.size)
# print("tipo de dados" , array_3.dtype)
# print("tamanho de cada elemento em bytes" , array_3.itemsize)