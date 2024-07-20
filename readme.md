# Agent-Based Simulation of Information Spreading

## Overview

This project simulates the spreading of information on a lattice using an agent-based model (ABM). It was originally developed as part of a bachelor internship in C and later transcribed into Python. The simulation aims to replicate the findings from the paper:

- **"2007 - Agliari, Burioni, Cassi, Neri - Universal Features of Information Spreading Efficiency on d-Dimensional Lattices"**

The current Python version focuses on visualizing and analyzing how information spreads among agents on a one-dimensional lattice.

## Scope

The primary objective of this project is to simulate the dynamics of information spreading on a lattice where agents can be informed or uninformed. The simulation tracks how long it takes for all agents to become informed when they interact according to specified rules. 

### Key Features

- **Agent-Based Modeling**: Agents move randomly and exchange information based on their neighbors' states.
- **Visualization**: The lattice and agent states are visualized using graphical plots.
- **Configurable Simulation**: The simulation parameters, such as lattice length and number of agents, can be defined through a configuration file.

### Limitations

- **Incomplete Features**: Several features from the original C implementation are still pending, including:
  - Results analysis
  - Extension to higher-dimensional lattices
- **Simplified Visualization**: Currently, visualization is limited to one-dimensional lattices.

## Implementation

### Classes

- **`Agent`**: Represents a single agent with a position and state (informed or uninformed).
- **`Agents`**: Manages a collection of `Agent` objects, including initialization, movement, and information exchange.
- **`Simulation`**: Orchestrates the simulation process, including setting up the lattice, running the simulation, and collecting statistics.
- **`Visualization`**: Provides methods for visualizing the lattice and agent states.

### Files

- **`agent.py`**: Contains the `Agent` class definition.
- **`agents.py`**: Contains the `Agents` class definition and interactions with the `Agent` class.
- **`visualization.py`**: Contains the `Visualization` class for plotting and printing lattice states.
- **`simulation.py`**: Manages the overall simulation logic, including initializing the lattice and running the simulation.
- **`main.py`**: Entry point for running simulations. Reads configuration from a JSON file, executes simulations, and saves results.

### Tests

#### `test_agent.py`

Contains tests for the `Agent` class, including initialization and movement functionalities.

#### `test_agents.py`

Contains tests for the `Agents` class, including:
- Initialization with a lattice.
- Information exchange logic.
- Movement and positioning of agents.

Note: The tests in this file are currently incomplete and may require additional coverage and validation.

#### `test_simulation.py`

Contains tests for the `Simulation` class, including:
- Initialization with different lattice sizes and agent counts.
- Running simulations and validating the number of steps required for all agents to be informed.

#### `test_visualization.py`

Contains tests for the `Visualization` class, ensuring that the visualization methods work correctly. 

## Usage

1. **Configuration**: Define simulation parameters in `config.json`.

   ```json
   {
       "simulations": [
           {
               "lattice_length": 20,
               "num_agents": 10
           },
           {
               "lattice_length": 30,
               "num_agents": 15
           },
           {
               "lattice_length": 40,
               "num_agents": 20
           }
       ]
   }
