import numpy as np
def matriz_identidade(n):
    multi = n * n
    return np.array(multi)
array_ = np.array([1,2,5,10,20])
print(matriz_identidade(array_))