from envs.drone_hover_env import DroneHoverEnv
import time
import pybullet as p
import numpy as np
from stable_baselines3 import PPO
env = DroneHoverEnv()

model = PPO.load("models/trained_hovering_agent")

obs, info = env.reset()



while True:
    action, _ = model.predict(
        obs, 
        deterministic = True
    )

    obs, reward, terminated, truncated, _ = env.step(action)


    time.sleep(1/30)
    if(terminated or truncated):
        print("Resetting!")
        obs, _  = env.reset()