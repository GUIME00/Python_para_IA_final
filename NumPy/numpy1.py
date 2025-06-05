import numpy as np

# Saída o array e as dimensões pelo método(ndim - number dimension)
arr1d = np.array([1,2,3])
print(f"Array 1D: {arr1d}, Dimensões: {arr1d.ndim}")

arr2d = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(f"Array 2D: {arr2d}, Dimensões: {arr2d.ndim}")


arr3d = np.array([[[3,4,5],[1,2,3]],[[5,6,7],[8,9,6]]])
print(f"Array 3D: {arr3d}, Dimensões: {arr3d.ndim}")

# Shape
# Indica o tamanho da array
print(f"Shape do arr1d: {arr1d.shape}")
print(f"Shape do arr2d: {arr2d.shape}")
print(f"Shape do arr3d: {arr3d.shape}")