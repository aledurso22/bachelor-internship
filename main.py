import json
from simulation import Simulation

def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def save_statistics(statistics_file, stats):
    with open(statistics_file, 'w') as file:
        json.dump(stats, file, indent=4)

if __name__ == "__main__":
    # Load configurations
    config = load_config('config.json')
    simulations_config = config['simulations']
    
    all_stats = []

    for sim_config in simulations_config:
        lattice_length = sim_config['lattice_length']
        num_agents = sim_config['num_agents']
        
        # Run simulation
        simulation = Simulation(lattice_length, num_agents)
        num_steps = simulation.run(visualize=True)
        
        # Collect statistics
        stats = {
            'lattice_length': lattice_length,
            'num_agents': num_agents,
            'num_steps': num_steps
        }
        all_stats.append(stats)

    # Save all statistics
    save_statistics('statistics.json', all_stats)
    
    print(f"Simulations finished. Results saved to statistics.json.")
