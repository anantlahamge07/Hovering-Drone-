from stable_baselines3 import PPO
from envs.drone_hover_env import DroneHoverEnv


env = DroneHoverEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose = 1
)

model.learn(total_timesteps=10000)



obs, _ = env.reset()

for i in range(200):
    action, _ = model.predict(obs, deterministic=True)

    obs, reward, terminated, truncated, _ = env.step(action)

    print(
        f"z={obs[2]:.3f}",
        f"reward={reward:.3f}",
        f"action={action}"
    )

    if terminated or truncated:
        break