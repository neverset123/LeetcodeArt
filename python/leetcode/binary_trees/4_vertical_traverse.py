
#垂直方向遍历二叉树
#leetcode987

from typing import List
import collections
from utils import TreeNode, from_list


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