import gymnasium as gym
import numpy as np
import cv2

env = gym.make("CarRacing-v3", render_mode="rgb_array")


def preprocess(img):

    img = cv2.resize(img, (96, 96))
    img = img / 255.0
    return img


def step_simulation():

    state, _ = env.reset()

    state = preprocess(state)

    action = [0, 1, 0]  # accelerate

    next_state, reward, terminated, truncated, _ = env.step(action)

    frame = cv2.resize(next_state, (400, 400))

    return frame.tolist(), float(reward)
