import queue
import random
import math

#动态规划
def knapsack(v, w, c, n):
    m = [[0 for i in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            m[i][j] = m[i-1][j]
            if j >= w[i - 1] and m[i][j] < m[i-1][j-w[i-1]] + v[i-1]:
                m[i][j] = m[i-1][j-w[i-1]] + v[i-1]
    # for i in range(n + 1):
    #     print(m[i])
    return m

def traceback(w, c, n, m):
    print("最大价值为", m[n][c])
    x = [-1 for i in range(n)]
    j = c
    for i in range(1, n + 1):
        if m[i][j] > m[i-1][j]:
            x[i-1] = 1
            j -= w[i-1]
    # print("选择物品为:")
    # for i in range(n):
    #     if x[i] == 1:
    #         print("第", i+1, "个", end='')

#回溯法
bestv = 0
curw = 0
curv = 0
bestx = None

def knapbacktrack(i):
    global bestv, curw, curv, bestx
    if i >= n:
        if bestv < curv:
            bestv = curv
            bestx = x[:]

    else:
        if curw + w[i] <= c:
            x[i] = 1
            curw += w[i]
            curv += v[i]
            knapbacktrack(i + 1)
            curw -= w[i]
            curv -= v[i]
        x[i] = -1
        knapbacktrack(i + 1)

#分支限界法
# def maxknapsack(v, w, c, n):
#     vec_len = 2**(n + 1) - 1
#     vec_v = [0 for i in range(vec_len)]
#     vec_w = [0 for i in range(vec_len)]
#     vec_w[0] = c
#     que = queue.Queue()
#     que.put(0)
#     best = 0
#     while(not que.empty()):
#         cur = que.get()
#         level = int(math.log(cur+1, 2))
#         if(vec_v[cur] > vec_v[best]):
#             best = cur
#         left = 2 * cur + 1
#         right = 2 * cur + 2
#         if(left < vec_len and vec_w[cur] - w[level] > 0 and vec_v[cur] + v[level] > vec_v[best]):
#             vec_v[left] = vec_v[cur] + v[level]
#             vec_w[left] = vec_w[cur] - w[level]
#             que.put(left)
#         if(right < vec_len and sum(v[level+1:-1]) + vec_v[cur] > vec_v[best]):
#             vec_v[right] = vec_v[cur]
#             vec_w[right] = vec_w[cur]
#             que.put(right)
#     print("最大价值为", vec_v[best])

class treenode(object):
    def __init__(self):
        self.weight = None
        self.value = None
        self.level = None
        self.flag = None

bestvalue = 0
que = queue.Queue()
def enQueue(w, v, level, flag, n):
    global bestvalue
    node = treenode()
    node.weight = w
    node.value = v
    node.flag = flag
    node.level = level
    if level == n:
        if node.value > bestvalue:
            bestvalue = node.value
        return 0
    else:
        que.put(node)

def bbfifoknap(w, v, n, c):
    i = 1
    tag = treenode()
    livenode = treenode()
    livenode.weight = 0
    livenode.value = 0
    livenode.level = 1
    livenode.flag = 0
    tag.weight = -1
    tag.value = 0
    tag.level = 0
    tag.flag = 0
    que.put(tag)
    while 1:
        if livenode.weight + w[i - 1] <= c:
            enQueue(livenode.weight + w[i - 1], livenode.value + v[i - 1], i, 1, n)
        enQueue(livenode.weight, livenode.value, i, 0, n)
        livenode = que.get()
        if livenode.weight == -1:
            if que.empty() == 1:
                break;
            livenode = que.get()
            que.put(tag)
            i += 1

def tanxin(v, w, c, n):
    a = []
    for i in range(n):
        a.append(float(v[i]/w[i]))
    max = a[0]
    index = 0
    for i in range(n):
        if a[i] > max:
            max = a[i]
            index = i

    left = c
    res = 0
    while left > 0:
        if w[index] <= left:
            res += v[index]
            left -= w[index]
            a[index] = 0
            max = a[0]
            index = 0
            for i in range(n):
                if a[i] > max:
                    max = a[i]
                    index = i
        else:
            a[index] = 0
            max = a[0]
            index = 0
            for i in range(n):
                if a[i] > max:
                    max = a[i]
                    index = i
            if a[index] == 0:
                break;
    print("最大价值为: ", res)


if __name__ == "__main__":
    n = 20
    c = 100
    w = []
    v = []
    for i in range(n):
        w.append(random.randint(1, 20))
    for i in range(n):
        v.append(random.randint(1, 100))
    print("动态规划结果：")
    m = knapsack(v, w, c, n)
    traceback(w, c, n, m)
    print('\n')
    print("回溯法结果：")
    x = [0 for i in range(n)]
    knapbacktrack(0)
    print("最大价值为", bestv)
    # print("选择物品为：")
    # for i in range(n):
    #     if bestx[i] == 1:
    #         print("第", i + 1, "个", end='')
    print('\n')
    print("分支限界法：")
    #maxknapsack(v, w, c, n)
    bbfifoknap(w, v, n, c)
    print("最大价值为: ",bestvalue)
    print('\n')
    print("贪心算法: ")
    tanxin(v, w, c, n)
