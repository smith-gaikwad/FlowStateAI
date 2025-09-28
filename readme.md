FlowStateAI: A 5D Digital Twin for Traffic Management
FlowStateAI is a real-time AI traffic control system designed to reduce congestion, optimize signal timings, and improve commute efficiency in dense urban environments. This prototype, built for the Smart India Hackathon (SIH), demonstrates a multi-layered approach to intelligent traffic management using a SUMO (Simulation of Urban MObility) digital twin.

The system combines predictive analytics with real-time, multi-agent reinforcement learning to proactively manage traffic flow and respond to emergencies.

Key Features (Implemented in this Prototype)
Real-World Simulation: Simulates a traffic-dense area of Mumbai, moving beyond simple grid networks.

AI-Powered Signal Control: A pre-trained Reinforcement Learning (RL) agent at each intersection dynamically controls traffic light phases to minimize congestion.


Predictive Alerts: A mocked GNN-LSTM module provides proactive alerts for potential bottlenecks, showcasing the system's ability to forecast traffic issues.


Emergency Vehicle Preemption: The system automatically detects emergency vehicles and creates a "green wave" by forcing traffic lights ahead to green, clearing a path to save critical time.


Real-Time Dashboard: A web-based dashboard provides authorities with live KPIs, system logs, and predictive alerts for decision support.


Scalable Architecture: The prototype includes mocks for advanced concepts like Federated Learning, demonstrating a privacy-preserving way for the system to learn and improve over time.

System Requirements
Python 3.8+

SUMO (Simulation of Urban MObility)

How to Set Up and Run the Project
1. Clone the Repository
First, download the project files to your computer.

Bash

git clone https://github.com/your-username/FlowStateAI.git
cd FlowStateAI
2. Create and Activate the Virtual Environment (venv)
A virtual environment is a private sandbox for your project's libraries. This ensures that the project's dependencies don't interfere with other Python projects on your system.

On Windows:

PowerShell

# Create the virtual environment folder named 'venv'
python -m venv venv

# Activate it
.\venv\Scripts\activate
You will know it's active when you see (venv) at the beginning of your terminal prompt.

3. Install Required Libraries
Install all the necessary Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
4. Configure the Simulation
Before the first run, you need to configure the simulation files for your chosen map (e.g., Mumbai).

Generate Map & Traffic: If you don't have the mumbai_csmt.net.xml and mumbai_csmt.rou.xml files, follow the steps in the project documentation to generate them using netconvert and randomTrips.py.

Configure the Detector: The car counter needs a valid lane ID from your map.

First, launch the SUMO GUI directly to inspect the map. It will stay open as long as you need.

PowerShell

sumo-gui -c flowstate.sumocfg
In the SUMO window, use the Inspector tool (magnifying glass) to find and copy a lane ID from a busy road.

Close the SUMO window.

Open the file detectors.add.xml and paste the copied ID into the lane="..." attribute.

5. Run the FlowStateAI Prototype
You need to run two scripts in two separate terminals.

In your FIRST terminal, run the Dashboard:

Bash

python dashboard.py
Open your web browser and go to http://127.0.0.1:8050/.

In your SECOND terminal, run the main Simulation:

Bash

python main.py
The SUMO window will launch, and you will see the simulation running with traffic. The dashboard will update with live data.

To stop the simulation, go to the terminal running main.py and press Ctrl+C.FlowStateAI: A 5D Digital Twin for Traffic Management
FlowStateAI is a real-time AI traffic control system designed to reduce congestion, optimize signal timings, and improve commute efficiency in dense urban environments. This prototype, built for the Smart India Hackathon (SIH), demonstrates a multi-layered approach to intelligent traffic management using a SUMO (Simulation of Urban MObility) digital twin.

The system combines predictive analytics with real-time, multi-agent reinforcement learning to proactively manage traffic flow and respond to emergencies.

Key Features (Implemented in this Prototype)
Real-World Simulation: Simulates a traffic-dense area of Mumbai, moving beyond simple grid networks.

AI-Powered Signal Control: A pre-trained Reinforcement Learning (RL) agent at each intersection dynamically controls traffic light phases to minimize congestion.


Predictive Alerts: A mocked GNN-LSTM module provides proactive alerts for potential bottlenecks, showcasing the system's ability to forecast traffic issues.


Emergency Vehicle Preemption: The system automatically detects emergency vehicles and creates a "green wave" by forcing traffic lights ahead to green, clearing a path to save critical time.


Real-Time Dashboard: A web-based dashboard provides authorities with live KPIs, system logs, and predictive alerts for decision support.


Scalable Architecture: The prototype includes mocks for advanced concepts like Federated Learning, demonstrating a privacy-preserving way for the system to learn and improve over time.

System Requirements
Python 3.8+

SUMO (Simulation of Urban MObility)

How to Set Up and Run the Project
1. Clone the Repository
First, download the project files to your computer.

Bash

git clone https://github.com/your-username/FlowStateAI.git
cd FlowStateAI
2. Create and Activate the Virtual Environment (venv)
A virtual environment is a private sandbox for your project's libraries. This ensures that the project's dependencies don't interfere with other Python projects on your system.

On Windows:

PowerShell

# Create the virtual environment folder named 'venv'
python -m venv venv

# Activate it
.\venv\Scripts\activate
You will know it's active when you see (venv) at the beginning of your terminal prompt.

3. Install Required Libraries
Install all the necessary Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
4. Configure the Simulation
Before the first run, you need to configure the simulation files for your chosen map (e.g., Mumbai).

Generate Map & Traffic: If you don't have the mumbai_csmt.net.xml and mumbai_csmt.rou.xml files, follow the steps in the project documentation to generate them using netconvert and randomTrips.py.

Configure the Detector: The car counter needs a valid lane ID from your map.

First, launch the SUMO GUI directly to inspect the map. It will stay open as long as you need.

PowerShell

sumo-gui -c flowstate.sumocfg
In the SUMO window, use the Inspector tool (magnifying glass) to find and copy a lane ID from a busy road.

Close the SUMO window.

Open the file detectors.add.xml and paste the copied ID into the lane="..." attribute.

5. Run the FlowStateAI Prototype
You need to run two scripts in two separate terminals.

In your FIRST terminal, run the Dashboard:

Bash

python dashboard.py
Open your web browser and go to http://127.0.0.1:8050/.

In your SECOND terminal, run the main Simulation:

Bash

python main.py
The SUMO window will launch, and you will see the simulation running with traffic. The dashboard will update with live data.

To stop the simulation, go to the terminal running main.py and press Ctrl+C.
