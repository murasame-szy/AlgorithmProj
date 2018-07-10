import random
import math


T0 = 1000
TF = 0.01
T = 0.99
N = 1000
M = 50

w = []
v = []
a = []
preseq = []
bestseq = []
for i in range(M):
    w.append(random.randint(1, 20))
    v.append(random.randint(1, 100))
    a.append(0)
    preseq.append(0)
    bestseq.append(0)

c = 100
premaxp = 0
bestmaxp = 0

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


#模拟退火算法
def calvalue(a):
    p = 0
    for i in range(M):
        p = p + (a[i] * v[i])
    return p

def calweight(a):
    p = 0
    for i in range(M):
        p = p + (w[i] * a[i])
    return p

def initialize():
    for i in range(M):
        a[i] = 0
        preseq[i] = 0
        bestseq[i] = 0
    premaxp = calvalue(a)
    bestmaxp = premaxp

def change():
    r1 = random.randint(0, 49)
    r2 = random.randint(0, 49)
    a[r1] = 1
    a[r2] = 1
    if calweight(a) > c:
        a[r2] = 0
    if calweight(a) > c:
        a[r1] = 0

def SA():
    global bestmaxp
    t = T0
    i = 0
    j = 0
    dif1 = 0
    dif2 = 0
    p = 0.0
    while t > TF:
        for i in range(M):
            change()
            dif1 = calvalue(a) - bestmaxp
            if dif1 > 0:
                for j in range(M):
                    preseq[j] = a[j]
                    bestseq[j] = a[j]
                premaxp = calvalue(a)
                bestmaxp = premaxp
            else:
                dif2 = calvalue(a) - premaxp
                if dif2 > 0:
                    for j in range(M):
                        preseq[j] = a[j]
                    premaxp = calvalue(a)
                else:
                    p = float(random.randint(0,20000)/20000.0)
                    if math.exp(dif2/t) > p:
                        for j in range(M):
                            preseq[j] = a[j]
                        premaxp = calvalue(a)
                    else:
                        for j in range(M):
                            a[j] = preseq[j]
        t = t * T

if __name__ == "__main__":
    print("动态规划结果：")
    m = knapsack(v, w, c, M)
    traceback(w, c, M, m)
    print('\n')
    print("模拟退火算法: ")
    SA()
    # for i in range(M):
    #     if i%5 == 0:
    #         print(" ")
    #     print(bestseq[i])
    print("最大价值为: ", bestmaxp)