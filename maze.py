# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:25:49 2019

@author: WinJX
"""

import numpy as np
import time
import tkinter as tk


UNIT = 40   # 单元大小
MAZE_H = 5  # 网格高度
MAZE_W = 5  # 网格宽度


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']  #行为空间，上下左右
        self.n_actions = len(self.action_space)   #行为个数
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # 画线
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # 块大小
        origin = np.array([20, 20])

        # 障碍物hell14
        hell14_center = origin + np.array([UNIT*3, 0])
        self.hell14 = self.canvas.create_oval(
            hell14_center[0] - 15, hell14_center[1] - 15,
            hell14_center[0] + 15, hell14_center[1] + 15,
            fill='black')
        # 障碍物hell24
        hell24_center = origin + np.array([UNIT*3, UNIT])
        self.hell24 = self.canvas.create_oval(
            hell24_center[0] - 15, hell24_center[1] - 15,
            hell24_center[0] + 15, hell24_center[1] + 15,
            fill='black')
        
        # 障碍物hell31
        hell31_center = origin + np.array([0, UNIT * 2])
        self.hell31 = self.canvas.create_oval(
            hell31_center[0] - 15, hell31_center[1] - 15,
            hell31_center[0] + 15, hell31_center[1] + 15,
            fill='black')
        
        # 障碍物hell32
        hell32_center = origin + np.array([UNIT, UNIT * 2])
        self.hell32 = self.canvas.create_oval(
            hell32_center[0] - 15, hell32_center[1] - 15,
            hell32_center[0] + 15, hell32_center[1] + 15,
            fill='black')
        
        # 障碍物hell53
        hell53_center = origin + np.array([UNIT*2, UNIT*4])
        self.hell53 = self.canvas.create_oval(
            hell53_center[0] - 15, hell53_center[1] - 15,
            hell53_center[0] + 15, hell53_center[1] + 15,
            fill='black')
        
        # 障碍物hell54
        hell54_center = origin + np.array([UNIT*3, UNIT*4])
        self.hell54 = self.canvas.create_oval(
            hell54_center[0] - 15, hell54_center[1] - 15,
            hell54_center[0] + 15, hell54_center[1] + 15,
            fill='black')
        
        # 障碍物hell55
        hell55_center = origin + np.array([UNIT*4, UNIT*4])
        self.hell55 = self.canvas.create_oval(
            hell55_center[0] - 15, hell55_center[1] - 15,
            hell55_center[0] + 15, hell55_center[1] + 15,
            fill='black')

        # 目标点
        oval_center = origin + np.array([UNIT * 4,UNIT*3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='brown')

        # 查找点
        initial = origin# + np.array([UNIT*2,UNIT*2])
        self.rect = self.canvas.create_oval(
            initial[0] - 15, initial[1] - 15,
            initial[0] + 15, initial[1] + 15,
            fill='yellow')

        # 布局环境
        self.canvas.pack()
        
    #重置起始位置
    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        initial = origin# + np.array([UNIT*2,UNIT*2])
        self.rect = self.canvas.create_oval(
            initial[0] - 15, initial[1] - 15,
            initial[0] + 15, initial[1] + 15,
            fill='yellow')
        # 返回状态
        return self.canvas.coords(self.rect)
    
    #下一步执行
    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # 上
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # 下
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        
        elif action == 2:   # 左
            if s[0] > UNIT:
                base_action[0] -= UNIT
        elif action == 3:   # 右
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1]) 

        s_ = self.canvas.coords(self.rect)  # 下一个状态

        # 回报值
        flag = 0
        #成功找到，回报值+1
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            flag = 5
            s_ = 'terminal'
        #踩雷，回报值-1
        elif s_ in [self.canvas.coords(self.hell14), self.canvas.coords(self.hell24),
                    self.canvas.coords(self.hell31), self.canvas.coords(self.hell32),
                    self.canvas.coords(self.hell53), self.canvas.coords(self.hell54),
                    self.canvas.coords(self.hell55)]:
            reward = -1
            done = True
            flag = 4
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done,flag
    #更新环境
    def render(self):
        time.sleep(0.2)
        self.update()































#def update():
#    for t in range(10):
#        s = env.reset()
#        while True:
#            env.render()
#            a = 1
#            s, r, done = env.step(a)
#            if done:
#                break
#
#if __name__ == '__main__':
#    env = Maze()
#    env.after(100, update)
#    env.mainloop()