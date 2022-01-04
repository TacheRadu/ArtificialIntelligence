import gym
import numpy as np
from keras.models import Sequential
from keras.layers import InputLayer
from keras.layers import Dense
import pickle as pkl

env = gym.make('FrozenLake-v1', is_slippery=False)
discount_factor = 0.95
eps = 0.5
eps_decay_factor = 0.999
num_episodes=500

model = Sequential()
model.add(InputLayer(input_shape=(env.observation_space.n, )))
model.add(Dense(30, activation='relu'))
model.add(Dense(env.action_space.n, activation='linear'))
model.compile(loss='mse', optimizer='adam', metrics=['acc'])
for i in range(num_episodes):
    print("Episode:", i)
    state = env.reset()
    eps *= eps_decay_factor
    done = False
    while not done:
        if np.random.random() < eps:
            # holes: 5, 7, 11, 12
            action = np.random.randint(0, env.action_space.n)
            while state + action in [5, 7, 11, 12]:
                action = np.random.randint(0, env.action_space.n)
        else:
            action = np.argmax(
              model.predict(np.identity(env.observation_space.n)[state:state + 1]))
        new_state, reward, done, _ = env.step(action)
        target = reward + \
          discount_factor * \
            np.max(
              model.predict(
                np.identity(env.observation_space.n)[new_state:new_state + 1]))
        target_vector = model.predict(
          np.identity(env.observation_space.n)[state:state + 1])[0]
        target_vector[action] = target
        model.fit(
          np.identity(env.observation_space.n)[state:state + 1], 
          target_vector.reshape(-1, env.action_space.n), 
          epochs=1)
        state = new_state

f = open("model.pkl", "wb")
pkl.dump(model, f)