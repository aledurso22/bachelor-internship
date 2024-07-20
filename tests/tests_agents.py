import unittest
import numpy as np
from lattice import Lattice
from agents import Agents

class TestAgentsInitialization(unittest.TestCase):

    def test_agents_initialization(self):
        # Create a Lattice with known configuration
        lattice = np.array([0, -1, 0, 1, 0, -1, 0, 0, 1, 0])
        
        # Initialize Agents
        agents = Agents(N=3)
        agents.initialization(lattice)
        positions = agents.get_position()
        
        # Check if positions are correctly identified
        expected_positions = [-2, 4, 9]
        np.testing.assert_array_equal(positions, expected_positions, "Agents' positions are incorrect")
    
    def test_agents_with_empty_lattice(self):
        agents = Agents(N=3)
        with self.assertRaises(ValueError):
            agents.initialization(np.array([]))

    def test_agents_initialization_exceeds(self):
        # Create a Lattice with fewer non-zero elements than agents
        lattice = np.array([0, -1, 0, 1])
        
        # Initialize Agents
        agents = Agents(N=5)
        agents.initialization(lattice)
        positions = agents.get_position()
        
        # Check if positions are correctly identified
        expected_positions = [-2, 4, 0, 0, 0]  # Only two positions filled, rest should be zero
        np.testing.assert_array_equal(positions, expected_positions, "Agents' positions are incorrect")

if __name__ == '__main__':
    unittest.main()
