from envs.drone_hover_env import DroneHoverEnv
import time
import pybullet as p

env = DroneHoverEnv()

obs, info = env.reset()
print(p.getDynamicsInfo(env.drone, -1)[0])

for i in range(500):
    action = env.action_space.sample()

    obs, reward, terminated, truncated, info = env.step(action)

    time.sleep(1/60)

    if terminated or truncated:
        print("Episode ended at step", i)
        obs, info = env.reset()