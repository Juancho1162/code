import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función f(x, y)
def f(x, y):
    return np.sin(x) + np.cos(y)

# Definir la curva en el plano xy
t = np.linspace(0, 2*np.pi, 100)  # Parámetro t
x = np.cos(t)
y = np.sin(t)

# Evaluar la función f(x, y) a lo largo de la curva
z = f(x, y)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la curva en el plano xy
ax.plot(x, y, zs=0, zdir='z', label='Curva en el plano xy')

# Graficar la función tridimensional f(x, y)
ax.plot(x, y, z, label='f(x, y) a lo largo de la curva')

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título del gráfico
plt.title('Visualización de la curva y la función en 3D')

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

