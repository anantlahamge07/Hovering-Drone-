from stable_baselines3 import PPO
from envs.drone_hover_env import DroneHoverEnv
import numpy as np

env = DroneHoverEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose = 1
)



model.learn(total_timesteps = 300_000)

model.save("models/trained_hovering_agent")

print("Model saved :)")