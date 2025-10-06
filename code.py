import numpy as np
import matplotlib.pyplot as plt
vector = np.random.rand(720)
print(vector)

matriz = vector.reshape((120, 6))
print(matriz)


matriz_T = matriz.T
matriz_F = np.copy(np.reshape(matriz_T, matriz_T.shape, order='F'))
matriz_C = np.copy(np.reshape(matriz_T, matriz_T.shape, order='C'))
print(matriz_T)
print(matriz_F)
print(matriz_C)

