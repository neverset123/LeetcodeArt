# 深度优先， 使用回溯算法框架


from typing import Optional
from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.path=""
        self.min_path=""
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if root==None:
            return
        self.path+=chr(97+root.val)
        print(self.path)
        if root.left==None and root.right==None:
            if self.min_path=="":
                self.min_path=self.path[::-1]
            else:
                self.min_path=min(self.min_path, self.path[::-1])
        self.smallestFromLeaf(root.left)
        self.smallestFromLeaf(root.right)
        self.path=self.path[:-1]
        return self.min_path
