import heapq

class State:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance

def weight(fromNode, toNode):
    return 0

def dijkstra(graph, start):
    distTo = [float('inf') for _ in range(len(graph))]
    queue = [State(start, 0)]
    visited = set()
    distTo[start] = 0
    while queue:
        curState = heapq.heappop(queue)
        if curState.id in visited:
            continue
        visited.add(curState.id)
        if(curState.distance > distTo[curState.id]):
            continue
        for neighbor in graph[curState.id]:
            distTo[neighbor] = min(distTo[neighbor], curState.distance + weight(curState.id, neighbor))
            heapq.heappush(queue, State(neighbor, distTo[neighbor]))
    return distTo
