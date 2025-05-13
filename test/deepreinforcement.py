import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import gym
import random
from collections import deque

# Hyperparameters
learning_rate = 0.001
gamma = 0.95  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_decay = 0.995
epsilon_min = 0.01
batch_size = 64
memory_size = 100000

# Environment
env = gym.make('CartPole-v1')
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# Replay memory
memory = deque(maxlen=memory_size)

# Build Q-Network
def build_model():
    model = Sequential([
        Dense(24, activation='relu', input_shape=(state_size,)),
        Dense(24, activation='relu'),
        Dense(action_size, activation='linear')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='mse')
    return model

model = build_model()

# Epsilon-greedy action selection
def act(state):
    if np.random.rand() <= epsilon:
        return random.randrange(action_size)
    q_values = model.predict(state, verbose=0)
    return np.argmax(q_values[0])

# Training the agent using experience replay
def replay():
    global epsilon
    if len(memory) < batch_size:
        return

    minibatch = random.sample(memory, batch_size)
    for state, action, reward, next_state, done in minibatch:
        target = reward
        if not done:
            target += gamma * np.amax(model.predict(next_state, verbose=0)[0])
        target_f = model.predict(state, verbose=0)
        target_f[0][action] = target
        model.fit(state, target_f, epochs=1, verbose=0)

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Training loop
episodes = 500

for e in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    total_reward = 0

    for time in range(200):
        action = act(state)
        next_state, reward, done, _, _ = env.step(action)
        total_reward += reward
        next_state = np.reshape(next_state, [1, state_size])
        memory.append((state, action, reward, next_state, done))
        state = next_state

        if done:
            print(f"Episode {e+1}/{episodes}, Score: {total_reward}, Epsilon: {epsilon:.2f}")
            break

        replay()

# Test the trained model
test_episodes = 5
for _ in range(test_episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    for t in range(200):
        env.render()
        action = np.argmax(model.predict(state, verbose=0)[0])
        state, _, done, _, _ = env.step(action)
        state = np.reshape(state, [1, state_size])
        if done:
            break
env.close()
