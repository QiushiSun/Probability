from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt
plt.figure()
n = 15000  # 试验次数，理论上次数越多越精确
r = 1.0
a, b = (0., 0.)  # 取圆心和半径
left, right = a-r, a+r  # 约束边界条件
upper, lower = b-r, b+r
x = np.random.uniform(left, right, n)  # 调用均匀分布开始制作点列
y = np.random.uniform(upper, lower, n)
# 计算随机点到圆心的距离
d = np.sqrt((x-a)**2+(y-b)**2)
# 统计落在单位圆的随机点数目
count = sum(np.where(d < r, 1, 0))
pi = 4*count/n  # 计算近似圆周率
print('pi is approximate to')
print(pi)
# 往画布上添加两个图形，即点列和圆
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(x, y, 'ro', label="Monte Carlo",
          color='paleturquoise', markersize=0.2)  # 选了个喜欢的颜色
plt.axis('equal')  # 防止图形在Jupyter-lab中变形
C1 = Circle(xy=(a, b), radius=r, alpha=0.5)
axes.add_patch(C1)
plt.show()
# 注意要把点的大小调的小一点，不然会挡住圆看不清效果
