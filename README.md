# 蒙特卡罗方法(Monte Carlo Method)

## 概述
蒙特卡罗方法也称统计模拟方法，是一种以概率统计理论为指导的数值计算方法。是指使用随机数或更常见的伪随机数来解决很多计算问题的方法。

20世纪40年代，在冯·诺伊曼，斯塔尼斯拉夫·乌拉姆和尼古拉斯·梅特罗波利斯在洛斯阿拉莫斯国家实验室为核武器计划工作时发明了蒙特卡罗方法。因为乌拉姆的叔叔经常在摩纳哥的蒙特卡洛赌场输钱得名。蒙特卡罗方法正是以概率为基础的方法，与它对应的是确定性算法（注：确定性算法是利用问题的解析性质，产生一确定的有限或无限点序列使其收敛于全局最优解。这类方法依据某一确定性策略搜索局部极小，并试图跳跃已获得的局部极小而达到某个全局最优点，能充分利用问题的解析性质，从而计算效率高）。

## 思想
蒙特卡罗方法通常可粗略地分成两类：
* 一类是所求解的问题本身具有内在的随机性，借助计算机的运算能力可以直接模拟这种随机的过程。例如在核物理研究中，分析中子在反应堆中的传输过程。中子与原子核作用受到量子力学规律的制约，人们只能知道它们相互作用发生的概率，却无法准确获得中子与原子核作用时的位置以及裂变产生的新中子的行进速率和方向。科学家依据其概率进行随机抽样得到裂变位置、速度和方向，这样模拟大量中子的行为后，经过统计就能获得中子传输的范围，作为反应堆设计的依据。 
* 另一种类型是所求解问题可以转化为某种随机分布的特征数，比如随机事件出现的概率，或者随机变量的期望值。通过随机抽样的方法，以随机事件出现的频率估计其概率，或者以抽样的数字特征估算随机变量的数字特征，并将其作为问题的解。这种方法多用于求解复杂的多维积分问题。

## 实例

* 定积分![first equation](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B100%7D%20%5Cint_%7B0%7D%5E%7B1%7Dx%5E%7B2%7Ddx)求解

思路：该红色区域在一个1×1的正方形里面。使用蒙特卡洛方法，随机在这个正方形里面产生大量随机点（数量为n），计算有多少点（数量为count）落在红色区域内（判断条件为y<x^2），count/n就是所要求的积分值，也即红色区域的面积。
``` python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 1000)
y = x ** 2
plt.plot(x, y)
plt.fill_between(x, y, where=(y > 0), color='red', alpha=0.5)
plt.show()
```
``` python
import random

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
```
```
蒙特卡罗方法结果：0.333613
实际定积分结果：0.333333
两个结果的误差还是较小的。
```

* π求解

思路：
正方形内部有一个相切的圆，它们的面积之比是π/4。现在，在这个正方形内部，随机产生n个点，计算它们与中心点的距离，并且判断是否落在圆的内部。若这些点均匀分布，则圆周率 pi=4 * count/n, 其中count表示落到圆内投点数 n:表示总的投点数。

``` python
import random

def calpai():
    n = 1000000
    r = 1.0
    a, b = (0.0, 0.0)
    x_neg, x_pos = a - r, a + r
    y_neg, y_pos = b - r, b + r

    count = 0
    for i in range(0, n):
        x = random.uniform(x_neg, x_pos)
        y = random.uniform(y_neg, y_pos)
        if x*x + y*y <= 1.0:
            count += 1

    print (count / float(n)* 4) 
    
calpai()
```

```
蒙特卡罗方法结果：3.14056
实际定积分结果：3.14159
两个结果的误差还是较小的。
```

## 参考
* https://blog.csdn.net/bitcarmanlee/article/details/82716641
* https://blog.csdn.net/u014281392/article/details/76202493
* https://blog.csdn.net/u014281392/article/details/76285280
