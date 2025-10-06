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


x = np.arange(matriz.shape[1])

# Panel 1: plot
ax1.plot(x, matriz[0], label='Fila 1')
ax1.set_title('Gráfico de líneas')

# Panel 2: scatter
ax2.scatter(x, matriz[1], color='orange', label='Fila 2')
ax2.set_title('Gráfico de dispersión')

# Panel 3: bar
ax3.bar(x, matriz[2], color='green', label='Fila 3')
ax3.set_title('Gráfico de barras')

# Panel 4: histograma
ax4.hist(matriz[3], bins=5, color='purple')
ax4.set_title('Histograma')

# Panel 5: pie chart
ax5.pie(matriz[4] / np.sum(matriz[4]), labels=[f'Col {i}' for i in range(6)])
ax5.set_title('Gráfico de pastel')

# Panel 6: múltiples líneas
for i in range(6):
    ax6.plot(matriz[:, i], label=f'Columna {i+1}')
ax6.set_title('Varias líneas (todas las columnas)')
ax6.legend()

for ax in [ax1, ax2, ax3, ax4, ax6]:
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()

