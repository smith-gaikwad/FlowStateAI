import os
import sys
import traci

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

def start_simulation():
    """Starts the SUMO simulation and connects with TraCI."""
    sumo_binary = "sumo-gui"
    sumo_config_file = "flowstate.sumocfg"
    sumo_cmd = [sumo_binary, "-c", sumo_config_file, "--start", "--quit-on-end"]
    traci.start(sumo_cmd)
    print("SUMO simulation started.")

def simulation_step():
    """Advances the simulation by one step."""
    traci.simulationStep()

def close_simulation():
    """Closes the TraCI connection."""
    print("\nClosing TraCI connection...")
    traci.close()
    print("SUMO simulation closed.")