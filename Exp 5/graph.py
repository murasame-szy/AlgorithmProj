class Graph(object):
    def __init__(self, map):
        self.map = map
        self.nodecount = self.get_node()
        self.edgecount = self.get_edge()

    def get_node(self):
        return len(self.map)

    def get_edge(self):
        count = 0
        for i in range(self.nodecount):
            for j in range(i):
                if self.map[i][j] > 0 and self.map[i][j] < MAX:
                    count += 1
        return count

    def prim(self):
        result = []
        if self.nodecount <= 0 or self.edgecount < self.nodecount - 1:
            return result
        node_select = [0]    #已选择的点
        node_left = [i for i in range(1, self.nodecount)]   #剩下的点
        while len(node_left) > 0:
            begin = 0
            end = 0
            minweight = MAX
            for i in node_select:
                for j in node_left:
                    if self.map[i][j] < minweight:
                        minweight = self.map[i][j]
                        begin = i
                        end = j
            result.append([begin, end, minweight])
            node_select.append(end)
            node_left.remove(end)
        return result

    def kruskal(self):
        result = []
        if self.nodecount <= 0 or self.edgecount < self.nodecount - 1:
            return result
        edge_list = []
        for i in range(self.nodecount):
            for j in range(i, self.nodecount):
                if self.map[i][j] < MAX:
                    edge_list.append([i, j ,self.map[i][j]])
        edge_list.sort(key=lambda a:a[2])
        group = [[i] for i in range(self.nodecount)] #在同一树里的放入一个集合
        for edge in edge_list:
            for i in range(len(group)):
                # print(group)
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                result.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return result




if __name__ == '__main__':
    MAX = 99999
    map = [[0,6,1,5,MAX,MAX], [6,0,5,MAX,3,MAX], [1,5,0,5,6,4], [5,MAX,5,0,MAX,2], [MAX,3,6,MAX,0,6], [MAX,MAX,4,2,6,0]]
    graph = Graph(map)
    print("邻接矩阵为:")
    for i in range(len(graph.map)-1):
        print(graph.map[i])
    print("节点数为 ", graph.nodecount)
    print("边数为 ", graph.edgecount)
    print("Prim 算法")
    print(graph.prim())
    print("Kruskal 算法")
    print(graph.kruskal())