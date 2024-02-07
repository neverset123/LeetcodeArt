
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbour):  
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)


def build_graph(edges):
    graph = Graph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    return graph.graph
