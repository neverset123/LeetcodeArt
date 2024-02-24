import utils
from copy import deepcopy

allPaths = []
visited = set() # 防止重复访问
onPath = set() # 记录当前路径上的节点
postorder = []
hasCycle = False

# DFS遍历无环图
def traverse(graph, start):
    onPath.add(start) #关注整个路径，而不是单个节点
    if(len(onPath) == len(graph)):
        allPaths.append(deepcopy(onPath))
        onPath.remove(start)
        return
    for neighbor in graph.get(start, []):
        traverse(graph, neighbor)
    onPath.remove(start)

# DFS遍历有环图
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

# BFS遍历有环图
def traverse_visit_bfs(graph, start):
    global hasCycle
    queue = []
    depth = 0
    queue.append(start)
    while(len(queue) != 0):
        size = len(queue)
        depth += 1
        for _ in range(size):
            node = queue.pop(0)
            if(node in visited):
                continue
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append(neighbor)
        

def check_cycle(graph):
    for node in graph:
        if(node not in visited):
            traverse_visit(graph, node)
    return hasCycle

# 拓扑排序
def find_order(graph, start):
    global hasCycle
    if(check_cycle(graph)):
        return []
    for node in graph:
        traverse_post(graph, node)
    return postorder[::-1]

def traverse_post(graph, start):
    if(start in visited):
        return
    visited.add(start)
    for neighbor in graph.get(start, []):
        traverse_post(graph, neighbor)
    postorder.append(start)

if __name__ == '__main__':
    edges = [[0,1],[0,2],[2,3],[1,3]]
    graph = utils.build_graph(edges)
    print(graph)
    # traverse(graph, 0)
    # print(allPaths)
    # traverse_visit(graph, 0)
    # print(hasCycle)
    print(find_order(graph, 0))