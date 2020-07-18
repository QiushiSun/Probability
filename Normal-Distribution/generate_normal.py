import numpy as np
import scipy
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
def normal_generator():
    mu=float(input())
    sigma=float(input())
    num_bins=int(input())
#     mu, sigma , num_bins = 0, 1, 50
    x = mu + sigma * np.random.randn(1000000)
    # 正态分布的数据
    n, bins, patches = plt.hist(x, num_bins, density=True, facecolor = 'dodgerblue', alpha = 0.7)
    # 拟合曲线
    y = scipy.stats.norm.pdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('X')
    plt.ylabel('Probability')
    plt.title("display histogram of normal distribution")
    plt.subplots_adjust(left = 0.15)
    plt.show()
    
normal_generator()