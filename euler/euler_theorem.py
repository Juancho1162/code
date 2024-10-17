"""
Shows the convergence of (1 + i*theta/n)^n to e^{i*theta} as n increases,
looping over different values of theta and n, showing that 
iterating theta over [0, 2pi] we get the unit circle in the complex plane
and the equivalence with sum of imaginary sines and real cosines of the angle.
"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

##

# Función para calcular (1 + i*theta/n)^n
def calculate_exponential(theta, n):
    return (1 + 1j * theta / n) ** n


def main():
    # Valores de theta y n
    theta = np.linspace(0, 2 * np.pi, 100)

    theta_test = 1
    n_values = [1, 2, 4, 6, 10, 20, 60, 100, 500, 1000, 10000]

    # Crear figura
    plt.figure(figsize=(10, 8))

    # Plot para cada valor de n


    for n in n_values:
        exponential_values = [calculate_exponential(t, n) for t in theta]
        plt.plot(np.real(exponential_values), np.imag(exponential_values), label=f"n={n}")


    # Dibujar el círculo unidad (representa e^{i*theta})
    circle = patches.Circle((0, 0), 1, color="black", fill=False)
    plt.gca().add_artist(circle)

    # Configuración del gráfico
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title("Convergence of (1 + iθ/n)^n a e^{iθ}")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    # Mostrar el gráfico
    plt.show()

if __name__ == '__main__':
    main()
