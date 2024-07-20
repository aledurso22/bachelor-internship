import numpy as np
from agents import Agents

class Simulation:
    def __init__(self, lattice_length: int, num_agents: int):
        self.lattice_length = lattice_length
        self.num_agents = num_agents
        self.lattice_data = self.initialization()
        self.agents = Agents(num_agents, lattice_length)
        self.agents.initialization(self.lattice_data)
    
    def initialization(self):
        # Create an array with N-1 minus ones
        ones = np.ones(self.num_agents - 1) * -1
        # Create an array with L - (N-1) zeros
        zeros = np.zeros(self.lattice_length - (self.num_agents - 1))
        combined = np.concatenate((ones, zeros))
        np.random.shuffle(combined)

        # Ensure that there's exactly one +1 in the middle if N >= 1
        if self.num_agents >= 1:
            middle_index = self.lattice_length // 2
            combined[middle_index] = 1  # Place +1 in the middle
            np.random.shuffle(combined)

        return combined

    def step(self):
        self.agents.move_agents()
        self.agents.exchange_information()

    def run(self, visualize=False):
        steps = 0
        while not self.agents.all_informed():
            self.step()
            steps += 1
            if visualize:
                self.agents.plot_lattice()  # Show the lattice visualization
        return steps
