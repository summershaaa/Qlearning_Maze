# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:26:41 2019

@author: WinJX
"""

import numpy as np
import pandas as pd


class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # 行为空间列表
        self.lr = learning_rate #学习率
        self.gamma = reward_decay #γ
        self.epsilon = e_greedy   #ε
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64) #Q表

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # 选择动作
        if np.random.uniform() < self.epsilon:
            # 最优策略
            state_action = self.q_table.ix[observation, :]
            state_action = state_action.reindex(np.random.permutation(state_action.index)) 
            action = state_action.idxmax()
        else:
            # 随机选择
            action = np.random.choice(self.actions)
        return action

    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.ix[s, a] #估计值
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.ix[s_, :].max()  
        else:
            q_target = r  
        self.q_table.ix[s, a] += self.lr * (q_target - q_predict)  # 更新Q值

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # 添加新状态到Q表
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )