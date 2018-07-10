#冒泡排序
def bubble_sort(lst):
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length - 1 - i):
            if(lst[j] > lst[j + 1]):
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


#快排
def quick_sort(lst, left, right):
    if left >= right:
        return lst
    key = lst[left]
    low = left
    high = right
    while left < right:
        while left < right and lst[right] >= key:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= key:
            left += 1
        lst[right] = lst[left]
    lst[right] = key
    quick_sort(lst, low, left - 1)
    quick_sort(lst, left + 1, high)
    return lst

#归并
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    num = int(len(lst) / 2)
    left = merge_sort(lst[:num])
    right = merge_sort(lst[num:])
    return merge(left, right)

#堆排序
def heap_sort(lst):
    length = len(lst)
    build_heap(lst, length)
    for i in range(0, length)[:: -1]:
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)
    return lst

def build_heap(lst, length):
    for i in range(0, int(length/2))[:: -1]:
        adjust_heap(lst, i, length)
    return lst

def adjust_heap(lst, i, length):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < (length/2):
        if lchild < length and lst[lchild] > lst[max]:
            max = lchild
        if rchild < length and lst[rchild] > lst[max]:
            max = rchild
        if max != i:
            lst[max], lst[i] = lst[i], lst[max]
            adjust_heap(lst, max, length)
    return lst

#计数排序
def count_sort(lst):
    m = max(lst)
    count = [0] * (m + 1)
    for i in lst:
        count[i] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    lst_new = [0] * len(lst)
    for i in range(0, len(lst))[:: -1]:
        lst_new[count[lst[i]] - 1] = lst[i]
        count[lst[i]] -= 1
    return lst_new

#基数排序
def radix_sort(lst):
    round = len(str(max(lst)))
    for k in range(0, round):
        s = [[] for i in range(10)]
        for i in lst:
            s[int(i / (10 ** k) % 10) ].append(i)
        lst = [a for b in s for a in b]
    return lst