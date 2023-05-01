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
        self.elements = []

    def pre_traverse_v1(self, root):
        if root==None:
            return
        self.elements.append(root.val)
        self.pre_traverse_v1(root.left)
        self.pre_traverse_v1(root.right)

    def pre_traverse(self, root):
        if root==None:
            return []
        return [root.val] + self.pre_traverse(root.left) + self.pre_traverse(root.right)
    
if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().pre_traverse(test_tree))
    print(min("abcde", "abc"))