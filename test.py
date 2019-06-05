# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:25:09 2019

@author: WinJX
"""
import numpy as np
import pandas as pd
from collections import Counter
from maze import Maze
from model import QLearningTable
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
pd.set_option('precision', 6)
pd.set_option('display.float_format',lambda x : '%.2f' % x)


def update():
    count = 0 #迭代次数记录
    find_target = 0 #找到目标次数
    iters = 100  #迭代次数
    length = []  #存放每次查找步数
    labels=[]    #标签，成功或踩雷
    paths = []   #路径
    for episode in range(iters):
        #初始化环境
        observation = env.reset()
        #映射表
        action_table = {0:'上',1:'下',2:'左',3:'右',4:'踩雷',5:'成功'}
        path = []
        while True:
            #更新环境
            env.render()
            # 基于当前状态选择一个动作
            action = RL.choose_action(str(observation))
            path.append(action_table[action])  #保存动作路径
            # 执行动作获得新的状态和汇报，标记等
            observation_, reward, done,flag = env.step(action)

            #学习新的知识
            RL.learn(str(observation), action, reward, str(observation_))

            # 更新值函数
            observation = observation_

            # 如果踩雷或者成功找到中点则跳出循环
            if done:
                path.append(action_table[flag])
                
                break
        #输出当前寻找路径
        labels.append(flag)
        if flag==5:
            find_target += 1
            length.append(len(path)-1)
        else:
            length.append(len(path))
            
        print('----------------第 %d 次查找路径----------------'%count)
        print(path)
        paths.append(path)
        print()
        count += 1
    
    #可视化部分
    labels = np.where(np.array(labels)==4,'踩雷','找到目标') #标记分类
    plt.title('迷宫',fontproperties = 'SimHei',fontsize = 26)
    avg_step = sum(length)/len(length)  #平均查找步数
    y= [avg_step]*iters
    #构造DataFrame
    df = pd.DataFrame({'labels':labels,'value':length},columns=['labels','value'])
    #可视化步数，并按标记分类输出
    sns.scatterplot(np.arange(len(length)),df['value'],hue=df['labels'],data=df,style=df['labels'],s=100)
    plt.ylabel('寻找步数',fontproperties = 'SimHei',fontsize = 22)
    plt.xlabel('循环数',fontproperties = 'SimHei',fontsize = 22)
    plt.plot(y,'--r',label='平均查找步数')
    plt.legend(loc='best',fontsize = 22)

    #输出相关信息
    print('步数\n',length)
    print('标签\n',labels)
    qtable = RL.q_table
    qtable.rename({0:'up',1:'down',2:'left',3:'right'},axis='columns',inplace=True)
    print('Q表\n',qtable)
    print('----------------------循环结束----------------------')
    
    #输出查找成功率
    print('在{}次查找中有{}次成功找到目标'.format(iters,find_target))
    
    #行走最多次的路径
    path_count = Counter([tuple(path) for path in paths])
    most_one = path_count.most_common(1)
    print('该路径行走次数最多，共{}次:\n{}'.format(most_one[0][1],most_one[0][0]))
    
    env.destroy()
    

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()