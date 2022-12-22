import numpy as np

def f(x):
    return np.sin(x) + 0.5 * x

a = 0.5
b = 9.5

# 在积分区间内取 I 个随机的 x 值，并计算每个随机 x 值处 的积分函数值。
# 加总所有函数值并求其平均值，就可以得到积分区间的平均函数值。
# 将该值乘以积分区间长度，可以得出估算的积分值。
#
# 下面的代码说明蒙特卡洛估算积分值如何随着提取随机数个数的增加而收敛（但并非 单调收敛）。
# 即使提取的随机数个数较少，估算值也已经相当接近

for i in range(1, 200):
    np.random.seed(1000)
    rd = np.random.random(i * 10) # length of the vector is 10, 20, 30, ...
    x = rd * (b - a) + a
    # print(i, rd, x, np.mean(f(x)) * (b - a))
    print(np.mean(f(x)) * (b - a))