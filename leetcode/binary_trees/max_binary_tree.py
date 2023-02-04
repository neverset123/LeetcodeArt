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
    def buildMaxBinaryTree(self, arr):
        return self.build(arr, 0, len(arr)-1)

    def build(self, arr, left, right):
        if left>right:
            return
        max_val=-sys.maxsize
        index = sys.maxsize
        for i, item in enumerate(arr[left:right+1]):
            if item>max_val:
                max_val=item
                index=i+left
        root = TreeNode(max_val)
        root.left=self.build(arr, left, index-1)
        root.right=self.build(arr, index+1, right)
        return root  

if __name__ == "__main__":
    test_data = [3,9,20,10,5,15,7]
    print(Solution().buildMaxBinaryTree(test_data))