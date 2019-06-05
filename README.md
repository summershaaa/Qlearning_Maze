# Qlearning_Maze
## 用Qlearning实现走迷宫问题
### 大致内容
如下图，左子图是迷宫环境，黑色点代表障碍物，棕色为目标点，黄色为查找初始点。<br>
**训练目标** : 找到一条最快的路径从黄色点走到棕色目标点(如右子图所示)。<br>
**回报值设置** : 遇到障碍物 -1，找到目标 +1，其他情况不变。
![图一](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E5%9B%BE%E4%B8%80%E7%BB%93%E5%90%88.PNG)
### 使用说明
```python 
maze.py :迷宫环境代码
model.py : 模型代码，包括动作选择，环境更新，学习知识等
test.py : 测试模型代码
```
### 结果展示
> **初始点在左上角**

![图一](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E5%9B%BE%E4%B8%80%E7%BB%93%E5%90%88.PNG)
<br>
<center>输出Q表和查找精度信息</center>

![输出Q表和查找精度信息](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E7%BB%93%E6%9E%9C%E4%BF%A1%E6%81%AF1.PNG)
<br>
可视化查找情况及步数

![可视化查找情况及步数](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E5%9B%BE%E4%B8%80%E7%BB%93%E6%9E%9C.png)
<br>
<br>
> **初始点在中心**

![图二](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E5%9B%BE%E4%BA%8C%E7%BB%93%E5%90%88.PNG)
<center>输出Q表和查找精度信息</center>
<br>

![输出Q表和查找精度信息](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E7%BB%93%E6%9E%9C%E4%BF%A1%E6%81%AF2.PNG)
<br>
可视化查找情况及步数

![可视化查找情况及步数](https://github.com/summershaaa/Qlearning_Maze/blob/master/Images/%E5%9B%BE%E4%BA%8C%E7%BB%93%E6%9E%9C.png)
