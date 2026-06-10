import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pybullet as p



ENV_NAME  = "gym-pybullet-drones"

# action space:
# [
#     motor0,
#     motor1,
#     motor2,
#     motor3
# ] 

# Observation space:
# [
#     x, y, z,
#     vx, vy, vz,
#     roll, pitch, yaw,
#     wx, wy, wz
# ]


class DroneHoverEnv(gym.Env):
    
    
    
    
    
    def __init__(self):
        super().__init__()
        self.env = gym.make(ENV_NAME)
        self.observation_space = spaces.Box(
            low = -np.inf, 
            high = np.inf,
            shape = (12, ),
            dtype= np.float32

        )

        self.action_space = spaces.Box(
            low = 0.0,
            high= 1.0,
            shape = (4, ),
            dtype= np.float32
        )

        self.drone = None
        self.plane = None
        self.client = None
        self.target_pos = np.array([0.0, 0.0, 1])
        self.current_step = 0
        self.max_steps = 1000
        self.drone_path = "/home/anant-anil-lahamge/gym-pybullet-drones/gym_pybullet_drones/assets/cf2x.urdf"

    def reset (self):
        pass

    def step(self, action):
        pass