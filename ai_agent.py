import random
from stable_baselines3 import PPO
import numpy as np

class AIAgent:
    def __init__(self, junction_id, state_size, num_actions):
        self.junction_id = junction_id
        self.state_size = state_size
        self.num_actions = num_actions
        self.prediction_model = None
        self.model = None

    def load_pretrained_model(self, path):
        try:
            self.model = PPO.load(path)
            print(f"Agent {self.junction_id}: Successfully loaded model from {path}")
        except Exception as e:
            print(f"Agent {self.junction_id}: Could not load model. Falling back to random. Error: {e}")

    def connect_prediction_model(self, model):
        self.prediction_model = model

    def get_state(self, sumo_state_dict):
        state_vector = np.zeros(self.state_size, dtype=np.float32)
        for i, count in enumerate(sumo_state_dict.values()):
            if i < self.state_size:
                state_vector[i] = count
        return state_vector

    def predict_action(self, state):
        if self.model:
            action, _ = self.model.predict(state, deterministic=True)
            return int(action)
        return random.randint(0, self.num_actions - 1)