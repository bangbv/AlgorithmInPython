import gymnasium as gym

env = gym.make("CartPole-v1")

observation, info = env.reset(seed=42)
for _ in range(1000):
    action = env.action_space.sample()
    print(f"Action: {action}")
    observation, reward, terminated, truncated, info = env.step(action)
    print(f"Observation: {observation}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}, Info: {info}")
    if terminated or truncated:
        observation, info = env.reset()
env.close()