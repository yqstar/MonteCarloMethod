# -*- coding: utf-8 -*-
# Author: AndrewYq
# Date: 2019-03-05
# Email: hfyqstar@163.com

import numpy as np
import matplotlib.pyplot as plt
import random

'''
问题：求解y=x^2在[0,1]上的定积分
求解：蒙特卡洛求解结果：0.333218
    实际结果：0.333333
'''

# 绘制 y = x^2 函数
x = np.linspace(0, 1, 1000)
y = x ** 2
plt.plot(x, y)
# 填充 y = x^2 曲线下和 y=0 之间填充
plt.fill_between(x, y, where=(y>0), color='red', alpha=0.5)
# 显示所绘制的图形
plt.show()


# 定义积分运算的主程序
def integral():
    n = 1000000
    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0

    count = 0
    for i in range(0, n):
        # random.uniform(x, y)方法将随机生成一个实数，它在[x,y]范围内。
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        # x*x > y，表示该点位于曲线的下面。所求的积分值即为曲线下方的面积与正方形面积的比。
        if x*x > y:
            count += 1

    integral_value = count / float(n)
    print (integral_value)
    
integral()