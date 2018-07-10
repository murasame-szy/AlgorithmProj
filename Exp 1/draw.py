import random
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from Sort import *

X = []
Y = []
n = 1
# length = 500000
length = 0
with open('radix_sort.txt', 'w') as file:
    while n <= 4:
        # length += 500000
        length += 5000
        file.write('length:' + str(length) + '\n')
        j = 1
        time = 0
        while j <= 5:
            list = []
            for i in range(0, length):
                num = random.randint(0, length)
                list.append(num)
            begin = datetime.datetime.now()
            list = bubble_sort(list)
            # list = quick_sort(list, 0, length - 1)
            # list = merge_sort(list)
            # list = heap_sort(list)
            # list = count_sort(list)
            # list = radix_sort(list)
            end = datetime.datetime.now()
            time_now = end - begin
            time_second = time_now.total_seconds()
            print(time_second)
            file.write(str(time_second) + '\n')
            time += time_second
            for i in range(0, length - 1):
                if list[i] > list[i + 1]:
                    print('error')
                    break
            j += 1
        time = time / 5
        print('avg time is' + str(time))
        file.write('avg time is' + str(time) + '\n')
        X.append(length/1000)
        Y.append(time)
        n += 1

#绘制图
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
fig = plt.figure()
plt.plot(X, Y, linewidth=1,color='r',marker='o', markerfacecolor='blue',markersize=5)
plt.xlabel(u"长度/千", fontproperties=font)
plt.ylabel(u"排序时间/秒", fontproperties=font)
plt.title(u"排序时间随长度变化图", fontproperties=font)
plt.grid(X)
plt.show()