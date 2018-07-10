import random
from Sort import *

length = 20
list = []
for i in range(0, length):
    num = random.randint(0, 1000)
    list.append(num)
print('original list')
print(list)
list0 = heap_sort(list)
print('heap sort')
print(list0)
list1 = bubble(list)
print('bubble sort')
print(list1)
list2 = quick_sort(list, 0, len(list) - 1)
print('quick sort')
print(list2)
list3 = merge_sort(list)
print('merge sort')
print(list3)
list4 = count_sort(list)
print('count sort')
print(list4)
list5 = radix_sort(list)
print('radix sort')
print(list5)