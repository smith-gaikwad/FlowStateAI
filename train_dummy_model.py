from stable_baselines3 import PPO
import gymnasium as gym

env = gym.make("CartPole-v1")
model = PPO("MlpPolicy", env, verbose=0)
model.learn(total_timesteps=100)
model.save("ppo_traffic_controller")
print("Dummy model 'ppo_traffic_controller.zip' saved successfully!")