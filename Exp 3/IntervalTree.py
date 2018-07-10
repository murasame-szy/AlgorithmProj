class Interval(object):
    def __init__(self):
        self.low = None
        self.high = None

class Lesson(object):
    def __init__(self):
        self.num = None
        self.name = None
        self.time = Interval()

class TreeNode(object):
    def __init__(self):
        self.lesson = Lesson()
        self.key = self.lesson.time.low
        self.left = None
        self.right = None
        #self.parent = TreeNode()
        self.parent = None
        self.color = 'black'
        # self.size = None
        self.max = self.lesson.time.high
        self.inter = self.lesson.time

class RBTree(object):
    def __init__(self):
        self.nil = TreeNode()
        self.root = self.nil

# 重叠返回1，不重叠返回0
def Overlap(a, b):
    if a.high < b.low :
        return 0
    if a.low > b.high:
        return 0
    return 1

# 左旋
def LeftRotate(T, x):
    y = x.right
    if y.left == None:
        print("y左结点为空")
        return
    x.right = y.left
    y.left.parent = x
    y.parent = x.parent
    # 若x为根，则修改树指针为y
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    y.max = x.max
    if x.left:
        x.max = max(float(x.lesson.time.high), float(x.left.max), float(x.right.max))
    else:
        x.max = max(float(x.lessson.time.high), float(x.right.max))

#右旋
def RightRotate(T, x):
    y = x.left
    if y.right == None:
        print("y右节点为空")
        return
    x.left = y.right
    y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
    y.max = x.max
    if x.right:
        x.max = max(float(x.lesson.time.high), float(x.left.max), float(x.right.max))
    else:
        x.max = max(float(x.lesson.time.high), float(x.left.max))

#插入
def RBInsert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        x.max = max(float(x.max), float(z.max))
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    # 同上，若y为空，则T为空树，z为根节点
    if y == T.nil:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = T.nil
    z.right = T.nil
    #z.color = 'red'
    RBInsertFixup(T, z)

#插入颜色修正
def RBInsertFixup(T, z):
    #若z为根，z.parent = nil,颜色为黑，不进入循环
    #若z.parent为黑色，无需调整，不进入循环
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:#case1,2,3
            y = z.parent.parent.right
            if y.color == 'red':#case1
                y.color = 'black'
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z.parent.right == z:#case2
                    z = z.parent
                    LeftRotate(T, z)
                #case3
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                RightRotate(T, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'red':
                y.color = 'black'
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z.parent.left == z:
                    z = z.parent
                    RightRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                LeftRotate(T, z.parent.parent)
    T.root.color = 'black'

def TreeMin(T, x):
    while x.left != T.nil:
        x = x.left
    return x

#中序后继
def TreeSuccessor(T, x):
    if x.right != T.nil:
        return TreeMin(T, x.right)
    y = x.parent
    while y != T.nil and x == y.right:
        x = y
        y = y.parent
    return y

#删除
def RBDelete(T, z):
    if z.left == T.nil or z.right == T.nil:#case1,2
        y = z
        # 附加信息维护
        # p = y.parent
        # if y.left != T.nil and p != T.nil:
        #     p.max = max(float(p.lesson.time.high), float(y.left.max))
        # elif y.right != T.nil and p != T.nil:
        #     p.max = max(float(p.lesson.time.high), float(y.right.max))
        # p = p.parent
        # if p:
        #     while p.max == y.max:
        #         p.max = max(float(p.lesson.time.high), float(p.left.max), float(p.right.max))
        #         p = p.parent
    else:
        y = TreeSuccessor(T, z)
    # 附加信息维护
    p = y.parent
    if y.left != T.nil and p != T.nil:
        p.max = max(float(p.lesson.time.high), float(y.left.max))
    elif y.right != T.nil and p != T.nil:
        p.max = max(float(p.lesson.time.high), float(y.right.max))
    p = p.parent
    if p:
        while p.max == y.max:
            p.max = max(float(p.lesson.time.high), float(p.left.max), float(p.right.max))
            p = p.parent
    if y.left != T.nil:
        x = y.left
    else:
        x = y.right
    x.parent = y.parent
    #若y为根节点，树指针指向x
    if y.parent == T.nil:
        T.root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != z:
        z.lesson = y.lesson
        z.key = y.key
        z.max = y.max
        z.inter = y.inter
        p = z.parent
        while p.max < z.max and p != T.nil:
            p.max = z.max
            p = p.parent
    if y.color == 'black':
        RBDeleteFixup(T, x)
    return y

#删除颜色修正
def RBDeleteFixup(T, x):
    while x != T.root and x.color == 'black':
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 'red':#case1
                w.color = 'black'
                x.parent.color = 'red'
                LeftRotate(T, x.parent)
                w = x.parent.right#to case2,3,4
            if w.left.color == 'black' and w.right.color == 'black':#case2
                w.color = 'red'
                x = x.parent
            else:
                if w.right.color == 'black':
                    w.left.color = 'black'
                    w.color = 'red'
                    RightRotate(T, w)
                    w = x.parent.right#to case4
                #case4
                w.color = x.parent.color
                x.parent.color = 'black'
                w.right.color = 'black'
                LeftRotate(T, x.parent)
                x = T.root
        else:
            w = x.parent.left
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                RightRotate(T, x.parent)
                w = x.parent.left
            if w.right.color == 'black' and w.left.color == 'black':
                w.color = 'red'
                x = x.parent
            else:
                if w.left.color == 'black':
                    w.right.color = 'black'
                    w.color = 'red'
                    LeftRotate(T, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = 'black'
                w.left.color = 'black'
                RightRotate(T, x.parent)
                x = T.root
    x.color = 'black'

#搜索区间
def SearchInterval(T, i):
    x = T.root
    while x != T.nil and Overlap(i, x.lesson.time) == 0:
        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        elif x.right != T.nil and x.right.key <= i.high:
            x = x.right
    return x

#插入一门课程
def LessonInsert(T, z):
    RBInsert(T, z)

#删除一门课程
def LessonDelete(T, z):
    x = SearchInterval(T, z.time)
    if x == T.nil:
        print("the lesson doesn't exist, please chech your input")
        return 0
    else:
        y = RBDelete(T, x)
        return 1

#打印某节点树
def PrintTree_Node(T, z):
    if z == T.nil:
        return
    PrintTree_Node(T, z.left)
    print("time: ", z.lesson.time.low, "-", z.lesson.time.high,"\n", "lesson no.", z.lesson.number, "\n", "lesson name", z.lesson.name, "\n", "key: ", z.key, "\n", "max: ", z.max)
    PrintTree_Node(T, z.right)

#打印树
def PrintTree(T):
    if T.root == T.nil:
        print("the tree is nil")
        return
    PrintTree_Node(T, T.root)

#查询特定区间的所有课程并打印
def SearchAll_Print(T, root, i):
    x = root
    if Overlap(x.lesson.time, i):
        print("time: ", x.lesson.time.low, "-", x.lesson.time.high,"\n", "lesson no.", x.lesson.number, "\n", "lesson name", x.lesson.name)
    if x.left != T.nil and x.left.max > i.low:
        SearchAll_Print(T, x.left, i)
    if x.right != T.nil and x.right.key < i.high:
        SearchAll_Print(T, x.right, i)

if __name__ == '__main__':
    T =RBTree()
    while(1):
        print("please choose what you want to do")
        print("1.Insert a lesson")
        print("2.Delete a lesson")
        print("3.Search the lessons in a specific interval")
        print("4.Print the tree by LDR")
        result = input()
        if result == '1':
            l = Lesson()
            n = TreeNode()
            l.number = input("input the lesson no.: ")
            l.name = input("input the lesson name: ")
            t1 = input("input the begin time: ")
            t2 = input("input the end time: ")
            l.time.low = float(t1)
            l.time.high = float(t2)
            n.lesson = l
            n.inter = l.time
            n.key = l.time.low
            n.max = l.time.high
            LessonInsert(T, n)
            print("successfully insert\n")
        elif result == '2':
            t1 = input("input the begin time: ")
            t2 = input("input the end time: ")
            l = Lesson()
            l.time.low = float(t1)
            l.time.high = float(t2)
            while LessonDelete(T, l) != 0:
                a = 1
            print("successfully delete\n")
        elif result == '3':
            t1 = input("input the begin time: ")
            t2 = input("input the end time: ")
            l = Lesson()
            l.time.low = float(t1)
            l.time.high = float(t2)
            SearchAll_Print(T, T.root, l.time)
        elif result == '4':
            PrintTree(T)
        else:
            print("error, please check your input")