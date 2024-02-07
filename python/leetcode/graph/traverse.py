import utils
from copy import deepcopy

allPaths = []
visited = set() # 防止重复访问
onPath = set() # 记录当前路径上的节点
hasCycle = False

# DFS遍历图
def traverse(graph, start):
    onPath.add(start) #关注整个路径，而不是单个节点
    if(len(onPath) == len(graph)):
        allPaths.append(deepcopy(onPath))
        onPath.remove(start)
        return
    for neighbor in graph.get(start, []):
        traverse(graph, neighbor)
    onPath.remove(start)

def traverse_visit(graph, start):
    global hasCycle
    if(start in onPath):
        hasCycle = True
    if((start in visited) or hasCycle):
        return
    visited.add(start)
    onPath.add(start)
    for neighbor in graph.get(start, []):
        traverse_visit(graph, neighbor)
    onPath.remove(start)

def find_order(graph, start):
    global hasCycle
    if(start in onPath):
        hasCycle = True
    if((start in visited) or hasCycle):
        return
    visited.add(start)
    for neighbor in graph.get(start, []):
        traverse_visit(graph, neighbor)
    onPath.add(start)

if __name__ == '__main__':
    edges = [[0,1],[0,2],[2,3],[1,3]]
    graph = utils.build_graph(edges)
    print(graph)
    # traverse(graph, 0)
    # print(allPaths)
    traverse_visit(graph, 0)
    print(hasCycle)