import numpy as np
from bisect import bisect_left, bisect_right
from agent import Agent
from visualization import Visualization

class Agents:
    def __init__(self, N: int, lattice_length: int):
        self.N = N
        self.lattice_length = lattice_length
        self.agents = []
        self.visualization = Visualization(lattice_length, N)

    def initialization(self, lattice: np.ndarray):
        for i, value in enumerate(lattice):
            if abs(value) == 1:
                informed = value > 0
                self.agents.append(Agent(i, informed))
        self.agents.sort(key=lambda agent: agent.position)

    def move_agents(self):
        for agent in self.agents:
            agent.move(self.lattice_length)
        self.agents.sort(key=lambda agent: agent.position)

    def exchange_information(self):
        agent_positions = [agent.position for agent in self.agents]

        for pos in set(agent_positions):
            left_index = bisect_left(agent_positions, pos)
            right_index = bisect_right(agent_positions, pos)
            agents_at_position = self.agents[left_index:right_index]

            if any(agent.informed for agent in agents_at_position):
                for agent in agents_at_position:
                    agent.inform()

    def all_informed(self):
        return all(agent.informed for agent in self.agents)

    def get_lattice(self):
        lattice = np.zeros(self.lattice_length, dtype=int)
        for agent in self.agents:
            lattice[agent.position] += 1 if agent.informed else -1
        return lattice

    def print_lattice(self):
        lattice = self.get_lattice()
        self.visualization.print_lattice(lattice)

    def plot_lattice(self):
        lattice = self.get_lattice()
        self.visualization.plot_lattice(lattice)
