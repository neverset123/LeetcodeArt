from typing import Optional

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        if abs(self.max_depth(root.left)-self.max_depth(root.right))>1:
            return False
        left=self.isBalanced(root.left)
        right=self.isBalanced(root.right)
        return left & right 

    def max_depth(self, root):
        if root==None:
            return 0
        left_max=self.max_depth(root.left)
        right_max=self.max_depth(root.right)
        return max(left_max, right_max)+1

