
#垂直方向遍历二叉树
#leetcode987

from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        seen = collections.defaultdict(
            lambda: collections.defaultdict(list)
        )

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node.val)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)

        dfs(root)
        ans = []
        for x in sorted(seen): # get keys in sorted order
            inner = []
            for y in sorted(seen[x]):
                inner.extend(sorted(n for n in seen[x][y]))
            ans.append(inner)
        return ans