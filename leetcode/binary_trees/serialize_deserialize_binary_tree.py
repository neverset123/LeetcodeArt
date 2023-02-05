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
            return "None"
        self.elements.append(root.val)
        self.preorder_serialize(root.left)
        self.preorder_serialize(root.right)
        return ",".join([str(ele) for ele in self.elements])
    
    def preorder_deserialize(self, arr_str):
        self.element = arr_str.split(",")
        if len(self.element)==0:
            return
        ele=self.element.pop(0)
        if ele=="None":
            root=TreeNode(None)
            return None
        root=TreeNode(ele)
        root.left=self.preorder_deserialize(",".join([str(ele) for ele in self.element]))
        root.right=self.preorder_deserialize(",".join([str(ele) for ele in self.element]))
        return root

if __name__ == "__main__":
    test_data = [None]
    test_tree = from_list(test_data)
    solution = Solution()
    solution1=Solution()
    solution3 = Solution()
    print(solution3.preorder_serialize(solution1.preorder_deserialize(solution.preorder_serialize(test_tree))))
