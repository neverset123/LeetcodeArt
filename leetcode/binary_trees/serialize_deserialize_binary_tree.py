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
        self.elements = []

    def preorder_serialize(self, root):
        if root==None:
            self.elements.append(None)
            return
        self.elements.append(root.val)
        self.preorder_serialize(root.left)
        self.preorder_serialize(root.right)
        return self.elements
    
    def preorder_deserialize(self, arr):
        if len(arr)==0:
            return
        ele=arr.pop(0)
        if ele==None:
            root=TreeNode(ele)
            return
        root=TreeNode(ele)
        root.left=self.preorder_deserialize(arr)
        root.right=self.preorder_deserialize(arr)
        return root

if __name__ == "__main__":
    test_data = [1,2,3,None,None,4,5]
    test_tree = from_list(test_data)
    solution = Solution()
    solution.preorder_serialize(test_tree)
    print(solution.elements)
    solution1=Solution()
    root = solution1.preorder_deserialize(solution.elements)
    solution1.preorder_serialize(root)
    print(solution1.elements)
