# 树就是「无环连通图」, 生成树是含有图中所有顶点的「无环连通子图」
# 所有可能的生成树中，权重和最小的那棵生成树就叫「最小生成树」
# 一般在无向加权图中计算最小生成树
# 主要有 Prim 算法（普里姆算法）和 Kruskal 算法（克鲁斯卡尔算法）两种算法;
# Kruskal 算法是在一开始的时候就把所有的边排序，然后从权重最小的边开始挑选属于最小生成树的边，组建最小生成树。
# Prim 算法是从一个起点的切分（一组横切边）开始执行类似 BFS 算法的逻辑，借助切分定理和优先级队列动态排序的特性，从这个起点「生长」出一棵最小生成树。
# 切分定理：在图的任意切分中，横切边中权重最小的边必然属于图的最小生成树
# 假设一幅图的节点个数为V，边的条数为E，首先需要O(E)的空间装所有边，而且 Union-Find 算法也需要O(V)的空间，所以 Kruskal 算法总的空间复杂度就是O(V + E)。
# 时间复杂度主要耗费在排序，需要O(ElogE)的时间，Union-Find 算法所有操作的复杂度都是O(1)，套一个 for 循环也不过是O(E)，所以总的时间复杂度为O(ElogE)。
# Prim 算法实现的总时间复杂度是O(ElogE)，空间复杂度是O(V + E)。

from union_find import UnionFind as UF
from heapq import heappush, heappop

#check if a graph is a valid tree
def valid_tree(n, edges):
    uf = UF(n)
    for u, v, _ in edges:
        if uf.connected(u, v):
            return False
        uf.union(u, v)
    return uf.count == 1

# Kruskal's algorithm
def min_cost_cities_kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UF(n+1) #+1 for no valid connection case
    res = 0
    for u, v, w in edges:
        if uf.connected(u, v):
            continue
        uf.union(u, v)
        res += w
    return uf.count == 2 and res or -1

# Kruskal's algorithm
def min_cost_connect_points_kruskal(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            edges.append((i, j, dist))
    
    return min_cost_cities_kruskal(n, edges)

# Prim's algorithm
class Prim:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.graph = [] #  adjacency list {from, to, weight}
        self.visited = [False] * n
        self.res = 0 # weight sum of minimum spanning tree
        self.pq = []

    def Prim(self, graph):
        self.graph = graph
        self.visited[0] = True
        self.cut(0)
        while self.pq:
            w, u = heappop(self.pq)
            if self.visited[u]:
                continue
            self.visited[u] = True
            self.res += w
            self.cut(u)
    
    def cut(self, u):
        for v, w in self.graph[u]:
            if not self.visited[v]:
                heappush(self.pq, (w, v))
    
    def all_connected(self):
        return all(self.visited)

def min_cost_cities_prim(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v-1, w)) # prim algorithm starts from 0
        graph[v].append((u-1, w))
    prim = Prim(n, edges)
    prim.Prim(graph)
    return prim.all_connected() and prim.res or -1

def min_cost_connect_points_prim(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            edges.append((i, j, dist))
    
    return min_cost_cities_prim(n, edges)

if __name__ == "__main__":
    n = 4
    edges = [[0,1,1],[0,2,2],[0,3,3],[1,2,4],[2,3,5]]
    print(valid_tree(n, edges))
    print(min_cost_cities_kruskal(n, edges))
    print(min_cost_cities_prim(n, edges))

    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(min_cost_connect_points_kruskal(points))
    print(min_cost_connect_points_prim(points))