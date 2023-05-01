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
        self.dummy = TreeNode(-1)
        self.p=self.dummy

    def flatten_v1(self, root):
        if root==None:
            return
        self.p.right=TreeNode(root.val)
        self.p=self.p.right
        self.flatten_v1(root.left)
        self.flatten_v1(root.right)
        return self.dummy.right

    def flatten(self, root):
        if root==None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        node1=root.left
        node2=root.right
        root.left=None
        root.right=node1
        p=root
        while(p.right!=None):
            p=p.right
        p.right=node2
        
if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().flatten(test_tree))