from typing import Optional
import sys

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
