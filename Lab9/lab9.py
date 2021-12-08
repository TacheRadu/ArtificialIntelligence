import gym

env = gym.make('FrozenLake-v1', is_slippery=False, map_name='4x4')

observation = env.reset()
for _ in range(10):
    env.render()
    
    action = env.action_space.sample() # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)
    if done:
        observation = env.reset()
env.close()
