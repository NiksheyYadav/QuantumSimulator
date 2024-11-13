# quantum_simulation/visualization.py

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_bloch_sphere(state):
    """Visualize the state of a single qubit on the Bloch sphere."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    # Draw the Bloch sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color="c", alpha=0.1)

    # Calculate theta and phi for the state vector
    alpha, beta = state[0][0], state[1][0]
    theta = 2 * np.arccos(np.abs(alpha))
    phi = np.angle(beta) - np.angle(alpha)
    
    # Compute coordinates
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    ax.quiver(0, 0, 0, x, y, z, color="r", arrow_length_ratio=0.2)
    
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()
