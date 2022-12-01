import gymnasium
import numpy as np

import PyFlyt

env = gymnasium.make("PyFlyt/AdvancedGatesEnv-v0", render_mode="human")

for i in range(3):
    obs, info = env.reset()

    while True:
        target = info["target"]
        action = np.array([target[0], target[1], 0.0, target[2] - 0.1])

        obs, rew, term, trunc, info = env.step(action)
