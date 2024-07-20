import numpy as np
import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, lattice_length: int, num_agents: int):
        self.lattice_length = lattice_length
        self.num_agents = num_agents

    def plot_lattice(self, lattice: np.ndarray):
        """
        Plot the lattice showing the distribution of agents and their information.
        """
        plt.figure(figsize=(10, 1))
        plt.imshow(lattice.reshape(1, -1), cmap='coolwarm', vmin=-self.num_agents, vmax=self.num_agents)
        plt.colorbar(label='Net Information')
        plt.title('Lattice Visualization')
        plt.xlabel('Position')
        plt.yticks([])  # Hide y-axis ticks
        plt.show()

    def print_lattice(self, lattice: np.ndarray):
        """
        Print the lattice with a simple text-based representation.
        """
        visual_representation = ''.join(
            str(value) if value != 0 else '0'
            for value in lattice
        )
        print(visual_representation)
