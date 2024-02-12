# 二分图结构在某些场景可以更高效地存储数据
from utils import build_graph

visited = set()
color = dict()
isBipartite = True

def is_bipartite(graph):
    global visited, color, isBipartite
    for index in list(graph.keys()):
        if index not in visited:
            color[index] = 1
            traverse(graph, index)
    return isBipartite

# 遍历法与之前的DFS有所不同
def traverse(graph, start):
    global isBipartite
    if not isBipartite:
        return
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            color[neighbor] = - color[start]
            traverse(graph, neighbor)
        else:
            if color[neighbor] == color[start]:
                isBipartite = False
            
if __name__ == '__main__':
    # edges = [[0,1],[0,2],[2,3],[1,3]]
    edges = [[1, 2], [1,3], [2,3]]
    graph = build_graph(edges)
    print(graph)
    print(is_bipartite(graph))
