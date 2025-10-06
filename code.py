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

fig = plt.figure(figsize=(14, 10))

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2))
ax3 = plt.subplot2grid((3, 3), (1, 0))
ax4 = plt.subplot2grid((3, 3), (1, 1))
ax5 = plt.subplot2grid((3, 3), (1, 2))
ax6 = plt.subplot2grid((3, 3), (2, 0), colspan=3)



