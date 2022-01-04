import pickle as pkl
import gym
import numpy as np

f = open("model.pkl", "rb")
model = pkl.load(f)

env = gym.make('FrozenLake-v1', is_slippery=False)
state = env.reset()
done = False
for i in range(1000):
    env.render()
    action = np.argmax(model.predict(np.identity(env.observation_space.n)[state:state+1]))
    state, reward, done, info = env.step(action)
    if done:
        if reward == 1:
            print("e bun")
        else:
            print("e rau")
        env.reset()
        break