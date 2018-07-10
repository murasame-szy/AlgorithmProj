import random

def random_point(count):
    global point
    point = [(500*random.random(), 500*random.random()) for i in range(count)]
    for i in point:
        print(i)
    return point

def get_distance(lst):
    dis = ((lst[0][0] - lst[1][0])**2 + (lst[0][1] - lst[1][1])**2) ** 0.5
    return dis


def force_search_min_distance(point):
    p1 = 0
    p2 = 0
    min = float('inf')
    for i in range(count - 1):
        for j in range(i+1, count):
            distance = ((point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2) ** 0.5
            if min > distance:
                min = distance
                p1 = i
                p2 = j
    print('暴力算法,O(n^2)')
    print('最短距离点对为 ' + str(point[p1]) + ' , ' + str(point[p2]))
    print('距离为' + str(min))

def search_min_distance(point):
    if len(point) == 1:
        print('分治法,O(nlgn)')
        print('只有一个点，距离为inf')
        return 0
    if len(point) == 2:
        min = get_distance(point)
        print('分治法,O(nlgn)')
        print('最短距离点对为 ' + str(point[0]) + ' , ' + str(point[1]))
        print('距离为' + str(get_distance(point)))
        return 0
    px = sorted(point, key=lambda x: (float(x[0])), reverse=False)
    point = search(px)
    print('分治法,O(nlgn)')
    print('最短距离点对为 ' + str(point[0]) + ' , ' + str(point[1]))
    print('距离为' + str(get_distance(point)))

def search(px):
    length = len(px)
    left = px[ : int(length/2)]
    right = px [int(length/2) : ]
    x_mid = (left[-1][0] + right[0][0]) / 2.0
    if len(left) > 2:
        lmin = search(left)
    else:
        lmin = left
    if len(right) > 2:
        rmin = search(right)
    else:
        rmin = right
    if len(lmin) >1:
        min1 = get_distance(lmin)
    else:
        min1 = float('inf')
    if len(rmin) >1:
        min2 = get_distance(rmin)
    else:
        min2 = float('inf')
    #min_0 = min(min1, min2)
    if min1 < min2:
        min_0 = min1
        p1 = lmin[0]
        p2 = lmin[1]
    else:
        min_0 = min2
        p1 = rmin[0]
        p2 = rmin[1]
    #以下确定是否存在跨区域点对小于最小距离
    compare = []
    for i in left:
        if x_mid - i[0] <= min_0:
            for j in right:
                if abs(i[0] - j[0]) <= min_0 and abs(i[1] - j[1]) <= min_0:
                    compare.append([i,j])
    if compare:
        dic = []
        for i in compare:
            if get_distance(i) <= min_0:
                min_0 = get_distance(i)
                p1 = i[0]
                p2 = i[1]
        return [p1, p2]
    elif min1 > min2:
        return rmin
    else:
        return lmin


count = 100
point = random_point(count)
force_search_min_distance(point)
search_min_distance(point)