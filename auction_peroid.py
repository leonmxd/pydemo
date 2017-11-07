
# 需要体现
# 1 报单，方向，价格
# 2 撤单
# 3 成交，数量。方向（index大小判断？）
# 4 最新价（和成交重合？）
# 5 对应的时间戳，一秒有多个成交和挂单，怎么处理？

import matplotlib.pyplot as plt
import random


'''

plt.plot(c, label='first')
plt.plot([1, 2, 3, 9], [5, 7, 4, 1], label='second')
plt.xlabel('x')
plt.ylabel('yyy')
plt.title('till')
plt.legend()
plt.show()
'''


upper_limit = 30


def get_random(count):
    i = 0
    l = []
    while i < count:
        n = random.uniform(1, upper_limit)
        l.append(n)
        i += 1

    return l


def get_random_relative(count, step=upper_limit / 30.0):
    i = 0
    l = []
    start = upper_limit / 2.0
    while i < count:
        n = random.uniform(start - step / 2.0, start + step / 2.0)
        l.append(n)
        start = n
        i += 1

    return l


def plot1():
    arr = get_random(500)
    plt.grid = True
    index = 0
    for x in arr:
        span = 0 # upper_limit
        if x > upper_limit / 2:
            c = 'r'
            y = span + x
        else:
            c = 'g'
            y = span - x
        # plt.plot([index, index], [span, y], color=c)
        plt.vlines(index, span, y, colors=c)
        index += 1


def plot2():
    arr = get_random_relative(500)
    plt.plot(arr)

plot1()
plot2()
plt.show()

