import pickle as pkl
import gym
import numpy as np

q = pkl.load(open("q.pkl", "rb"))

env = gym.make('FrozenLake-v1', is_slippery=False)

hit_count = 0
total_counts = 0
observation = env.reset()
for i in range(100):
    action = np.argmax(q[observation, :] + np.random.randn(1, env.action_space.n) * (1.0 / (i + 1)))
    observation, reward, done, info = env.step(action)
    if done:
        total_counts += 1
        if reward == 1:
            hit_count += 1
        env.reset()
print("Accuracy:", hit_count/total_counts * 100, "%")