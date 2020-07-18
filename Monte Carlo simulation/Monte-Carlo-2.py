import numpy as np
import matplotlib.pyplot as plt
from math import *
list1 = []
list2 = []
plt.figure()
count = 0
n = 150000
left, right = -1, 1  # 约束边界条件
upper, lower = 1, -1
x = np.random.uniform(left, right, n)  # 调用均匀分布开始制作点列
y = np.random.uniform(upper, lower, n)
for i in range(0, n-1):
    if(0 <= np.cos(pi*x[i])+np.sin(pi*y[i]) <= 1):
        list1.append(x[i])
        list2.append(y[i])
        count += 1
print(count)
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(list1, list2, 'ro', label="Monte Carlo",
          color='deepskyblue', markersize=0.03)  # 又选了个喜欢的颜色
plt.axis('equal')  # 防止图形在Jupyter-lab中变形
plt.show()
