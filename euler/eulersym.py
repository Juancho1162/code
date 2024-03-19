# I want to do a simulation of the approximation
# of the number e, using the compound interest formula

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def compound_interest(n):
    return (1 + 1 / n) ** n


def main():
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    # Set the x and y axis labels
    ax.set_xlabel('Number of times compounded')
    ax.set_ylabel('Approximation of e')
    # Set the title of the plot
    ax.set_title('Approximation of e using compound interest formula')
    # Set the x and y axis limits
    ax.set_xlim(1, 20)
    ax.set_ylim(1.8, 3)
    # Create the x and y data
    x = np.arange(1, 100)
    y = compound_interest(x)
    # Create the plot
    ax.plot(x, y, 'r')
    # Show the plot
    plt.show()

if __name__ == '__main__':
    main()

