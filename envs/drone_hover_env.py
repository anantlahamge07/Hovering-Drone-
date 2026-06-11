import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pybullet as p
import pybullet_data




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
        self.client = p.connect(p.GUI)
        self.target_pos = np.array([0.0, 0.0, 1])
        self.current_step = 0
        self.max_steps = 100
        self.max_thrust = 0.4
        self.drone_path = "/home/anant-anil-lahamge/gym-pybullet-drones/gym_pybullet_drones/assets/cf2x.urdf"




    def reset (self, seed = None, options = None):
        super().reset(seed = seed)
        p.resetSimulation()
        p.setGravity(0, 0, -9.81)
        p.setAdditionalSearchPath(
            pybullet_data.getDataPath()
        )
        self.current_step = 0
        self.plane = p.loadURDF("plane.urdf")
        self.drone = p.loadURDF(
            self.drone_path,
            [0, 0, 1],
            globalScaling = 8.0
        )
        obs = self.get_observation()
        return obs, {}
    


    
    def get_observation(self):
        pos, orientation = p.getBasePositionAndOrientation(self.drone)
        linear_velocity, angular_velocity = p.getBaseVelocity(self.drone)
        roll, pitch, yaw = p.getEulerFromQuaternion(orientation)

        return np.array([
            pos[0], pos[1], pos[2],
            linear_velocity[0],linear_velocity[1], linear_velocity[2], 
            roll, pitch, yaw,
            angular_velocity[0], angular_velocity[1], angular_velocity[2],
        ], dtype= np.float32)




    def step(self, action):


        reward = float(0.0)
        self.current_step += 1
        for t in range(4):
            thrust = action[t]*self.max_thrust
            p.applyExternalForce(
                self.drone, 
                t,
                [0, 0, thrust],
                [0, 0, 0],
                p.LINK_FRAME
            )
        for _ in range(5):
            p.stepSimulation()
        obs = self.get_observation()
        truncated = bool(self.current_step >= self.max_steps)
        terminated = bool(obs[2] <= 0.5)

        if(terminated): reward = -100.0
        else:
            distance =  np.sqrt(obs[0]*obs[0] + obs[1]*obs[1] + (obs[2] - 1.0)**2)
            vertical_speed = obs[5]
            reward = float(
                2.0
                - 3.0 * distance
                - 0.2 * abs(vertical_speed)
            )

        return obs, reward, terminated, truncated, {}
    


