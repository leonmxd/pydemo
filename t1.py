import matplotlib.pyplot as plt
import random
c = [1, 2, 3, 4, 5]


'''

plt.plot(c, label='first')
plt.plot([1, 2, 3, 9], [5, 7, 4, 1], label='second')
plt.xlabel('x')
plt.ylabel('yyy')
plt.title('till')
plt.legend()
plt.show()
'''


print(len(c))

print('abc %s%s' % ('test', 'hello'))

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

# 我的注解
def plot1():
    arr = get_random(500)
    plt.grid = True
    index = 0
    for x in arr:
        span = 0 #upper_limit
        if x > upper_limit / 2:
            c = 'r'
            y = span + x
            #linestyle = ":" #线条类型。:虚线，-实线，--破折线
            linestyle = '-.'
        else:
            c = 'g'
            y = span - x
            linestyle = "-"
        plt.plot([index, index], [span, y], color=c, ls=linestyle)
        index += 1


def plot2():
    arr = get_random_relative(500)
    plt.plot(arr)

plot1()
plot2()
plt.show()

