# django_project/ml/dqn_model.py

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import deque
import random

# DQN 모델 정의
class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# 하이퍼파라미터 정의
INPUT_DIM = 6  # 상태 벡터의 길이 (예: 장르, 시청 비율 등)
OUTPUT_DIM = 5  # 가능한 액션 수 (추천 가능한 영화의 수)
BATCH_SIZE = 32
GAMMA = 0.99
LEARNING_RATE = 0.001

# DQN 및 기타 요소 초기화
model = DQN(INPUT_DIM, OUTPUT_DIM)
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
memory = deque(maxlen=10000)  # 경험 리플레이 메모리

# 보상 계산 함수 (이전 단계에서 정의한 것을 사용)
def reward_function(watched_percentage):
    if watched_percentage > 90:
        return 1.0
    elif watched_percentage > 50:
        return 0.5
    else:
        return 0.1

# 경험을 추가하는 함수
def add_experience(state, action, reward, next_state, done):
    memory.append((state, action, reward, next_state, done))

# DQN 학습 함수
def train():
    if len(memory) < BATCH_SIZE:
        return

    batch = random.sample(memory, BATCH_SIZE)
    states, actions, rewards, next_states, dones = zip(*batch)

    states = torch.tensor(states, dtype=torch.float)
    actions = torch.tensor(actions, dtype=torch.long)
    rewards = torch.tensor(rewards, dtype=torch.float)
    next_states = torch.tensor(next_states, dtype=torch.float)
    dones = torch.tensor(dones, dtype=torch.float)

    # Q값 업데이트
    q_values = model(states)
    next_q_values = model(next_states)
    target_q_values = rewards + (GAMMA * torch.max(next_q_values, dim=1)[0] * (1 - dones))

    q_values = q_values.gather(1, actions.unsqueeze(-1)).squeeze(-1)
    loss = nn.MSELoss()(q_values, target_q_values)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 행동 선택 함수 (탐험 또는 이용)
def act(state, epsilon=0.1):
    if random.random() < epsilon:
        return random.randrange(OUTPUT_DIM)
    state = torch.tensor(state, dtype=torch.float).unsqueeze(0)
    with torch.no_grad():
        q_values = model(state)
    return torch.argmax(q_values).item()
