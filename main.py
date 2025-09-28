import json
import time
import sumo_connector as sc
from ai_agent import AIAgent
from advanced_mocks import PredictionModel, FederatedServer

LOG_FILE = 'system_log.txt'

def log_message(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def clear_logs():
    with open(LOG_FILE, 'w') as f:
        pass

def handle_emergency_vehicles(junction_ids):
    for veh_id in sc.traci.vehicle.getIDList():
        if sc.traci.vehicle.getTypeID(veh_id) == "AMBULANCE":
            log_message(f"EMERGENCY: Ambulance {veh_id} detected!")
            route = sc.traci.vehicle.getRoute(veh_id)
            route_index = sc.traci.vehicle.getRouteIndex(veh_id)

            for i in range(route_index, min(len(route), route_index + 3)):
                edge = route[i]
                tls_id = sc.traci.edge.getTLSID(edge)
                if tls_id and tls_id in junction_ids:
                    # Simplified green wave: find a valid green phase and set it
                    phases = sc.traci.trafficlight.getCompleteRedYellowGreenDefinition(tls_id)[0].phases
                    for phase_idx, phase in enumerate(phases):
                        if 'g' in phase.state.lower() and phase.duration > 5:
                            sc.traci.trafficlight.setPhase(tls_id, phase_idx)
                            log_message(f"ACTION: Forcing green light at {tls_id} for ambulance.")
                            break

def run_simulation():
    try:
        clear_logs()
        sc.start_simulation()
        log_message(f"FlowStateAI simulation started on Mumbai map.")

        junction_ids = sc.traci.trafficlight.getIDList()
        agents = {jid: AIAgent(jid, state_size=16, num_actions=4) for jid in junction_ids}
        mock_gnn_lstm = PredictionModel()
        federated_server = FederatedServer()

        for agent in agents.values():
            agent.load_pretrained_model("ppo_traffic_controller.zip")
            agent.connect_prediction_model(mock_gnn_lstm)

        step = 0
        while True: # Loop runs forever until user stops with Ctrl+C
            handle_emergency_vehicles(junction_ids)
            sc.simulation_step()

            if step % 10 == 0:
                log_message(f"--- Sim Time: {step}s ---")
                cars_passed = sc.traci.inductionloop.getLastStepVehicleNumber("detector_0")
                
                for jid in junction_ids:
                    # In a real system, agent logic would run here.
                    # We keep this part simple for the demo.
                    pass

                if step > 0 and step % 3600 == 0:
                    log_message(federated_server.aggregate_weights(len(agents)))
                
                sim_data = {
                    "time": step,
                    "avg_wait_time": "...",
                    "cars_passed": cars_passed,
                    "bottleneck_alert": mock_gnn_lstm.predict_bottleneck("J2", step),
                }
                with open('simulation_data.json', 'w') as f:
                    json.dump(sim_data, f)
            
            step += 1
            time.sleep(0.05) # Slow down visualization slightly

    except KeyboardInterrupt:
        print("\nSimulation stopped by user (Ctrl+C).")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        sc.close_simulation()

if __name__ == "__main__":
    run_simulation()