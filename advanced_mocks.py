class PredictionModel:
    """Mock for the GNN-LSTM model described in the flowchart."""
    def predict_bottleneck(self, junction_id, sim_time):
        if sim_time > 1800 and junction_id in ["J2", "J10"]: # Mock specific junctions
            return 'High Risk'
        return 'Low Risk'

class FederatedServer:
    """Mock for the Federated Learning server."""
    def aggregate_weights(self, num_agents):
        log_message = (
            f"\n[Federated Learning] Aggregating models from {num_agents} agents to create a new global model.\n"
        )
        return log_message