#对前中后序位置不敏感选择前序
#中序位置主要用于BST, 遍历有序数组
#需要用到子树返回值的，使用后序遍历

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

    #遍历解法
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
    
    #递归解法
    def pre_traverse_v2(self, root):
        res=[]
        if root==None:
            return []
        res.append(root.val)
        res.extend(self.pre_traverse_v2(root.left))
        res.extend(self.pre_traverse_v2(root.right))
        return res


if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().pre_traverse_v2(test_tree))
    print(min("abcde", "abc"))