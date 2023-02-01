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
    def __init__(self):
        self.maxdepth = 0
        self.depth = 0

    #遍历解法
    def maxDepth_v1(self, root: Optional[TreeNode]):
        self.traverse(root)
        return self.maxdepth

    def traverse(self, root):
        if root==None:
            return
        self.depth+=1
        if root.left==None and root.right==None:
            self.maxdepth=max(self.depth, self.maxdepth)
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth-=1
    
    #递归解法
    def maxDepth(self, root: Optional[TreeNode]):
        if root==None:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return max(left_max, right_max)+1


if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().maxDepth(test_tree))