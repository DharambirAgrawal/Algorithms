# !pip uninstall -y numpy tensorflow
# !pip install tensorflow



import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Dense
import gymnasium as gym
import random
from collections import deque

# Hyperparameters
learning_rate = 0.001
gamma = 0.95              # Discount factor
epsilon = 1.0             # Exploration rate
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
        Input(shape=(state_size,)),
        Dense(24, activation='relu'),
        Dense(24, activation='relu'),
        Dense(action_size, activation='linear')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss=tf.keras.losses.Huber())  # More stable than MSE
    return model

model = build_model()

# Epsilon-greedy action selection
def act(state):
    if np.random.rand() <= epsilon:
        return random.randrange(action_size)
    q_values = model.predict(state, verbose=0)
    return np.argmax(q_values[0])

# Experience replay training
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
    state, _ = env.reset()
    state = np.reshape(state, [1, state_size])
    total_reward = 0

    for time in range(200):
        action = act(state)
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        next_state = np.reshape(next_state, [1, state_size])
        memory.append((state, action, reward, next_state, done))
        state = next_state

        if done:
            print(f"Episode {e+1}/{episodes}, Score: {total_reward}, Epsilon: {epsilon:.2f}")
            break

        replay()

# Test the trained model
test_env = gym.make('CartPole-v1', render_mode='human')
test_episodes = 5

for _ in range(test_episodes):
    state, _ = test_env.reset()
    state = np.reshape(state, [1, state_size])
    for t in range(200):
        action = np.argmax(model.predict(state, verbose=0)[0])
        next_state, _, terminated, truncated, _ = test_env.step(action)
        done = terminated or truncated
        next_state = np.reshape(next_state, [1, state_size])
        state = next_state
        if done:
            break

test_env.close()
# end of the code
# Save the model
model.save('cartpole_dqn_model.h5')
# Load the model
# model = tf.keras.models.load_model('cartpole_dqn_model.h5')
# Note: The code above is a simple implementation of a Deep Q-Network (DQN) for the CartPole environment.
# It uses experience replay and an epsilon-greedy strategy for action selection.
# The model is trained over a number of episodes, and the performance is printed after each episode.
# The trained model can be saved and loaded for future use.
# Note: Make sure to have the required libraries installed in your Python environment.
# You can install them using pip:
# pip install numpy tensorflow gymnasium
# Note: The code is designed to run in a Python environment with TensorFlow and Gymnasium installed.
# Note: The CartPole environment is a classic control problem where the goal is to balance a pole on a cart.
# The agent learns to balance the pole by applying forces to the cart.
# Note: The code uses a simple neural network with two hidden layers to approximate the Q-values.