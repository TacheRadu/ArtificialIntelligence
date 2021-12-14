import gym
import numpy as np
import pickle as pkl

# 1 - down
# 2 - right
# 3 - up
# 4 - left

env = gym.make('FrozenLake-v1', is_slippery=False)
q = np.zeros((env.observation_space.n, env.action_space.n))
eta = .628
gma = .9

observation = env.reset()
done = False
for i in range(10000):
    # env.render()
    action = np.argmax(q[observation, :] + np.random.randn(1, env.action_space.n) * (1.0 / (i + 1)))
    observation1, reward, done, info = env.step(action)
    
    q[observation, action] = reward + gma * np.max(q[observation1, :])
    observation = observation1
    
    if done:
        env.reset()
pkl.dump(q, open("q.pkl", "wb"))
    
    
env.close()
