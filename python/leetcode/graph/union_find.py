# 动态连通性其实就是一种等价关系，具有「自反性」「传递性」和「对称性」
# 原问题转化成图的动态连通性问题

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) 
        self.size = [1] * n # Size of each component
        self.count = n # Number of components

    # Path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by weight
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            self.count -= 1

    # Check if two nodes are connected
    def connected(self, x, y):
        return self.find(x) == self.find(y)

def equationsPossible(equations):
    uf = UnionFind(26)
    for eq in equations:
        if eq[1] == '=':
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            uf.union(x, y)
    for eq in equations:
        if eq[1] == '!':
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            if uf.connected(x, y):
                return False
    return True

