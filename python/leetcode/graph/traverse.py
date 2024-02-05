import utils

visited = set() # 防止重复访问
onPath = set() # 记录当前路径上的节点

def traverse(graph, start):
    if start in visited:
        return
    visited.add(start)
    onPath.add(start)
    for neighbor in graph[start]:
        if neighbor in onPath:
            raise Exception('Cycle detected')
        traverse(graph, neighbor)
    onPath.remove(start)

if __name__ == '__main__':
    edges = [[0,1],[0,2],[2,3],[1,3]]
    graph = utils.build_graph(edges)
    print(graph)
    try:
        traverse(graph, 0)
    except Exception as e:
        print(e)
        print(visited)
        print(onPath)