#flatten tree to linked list in pre-traverse order using right child pointer

from typing import Optional
from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.dummy = TreeNode(-1) #创建链表头
        self.p=self.dummy   #创建移动指针

    #this does not modify in place but create new node
    def flatten(self, root):
        if root==None:
            return
        # 移动指针
        self.p.right=TreeNode(root.val)
        self.p=self.p.right
        self.flatten(root.left)
        self.flatten(root.right)
        return self.dummy.right

    # this modify in-place
    def flattenInPlace(self, root):
        if root==None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        node1=root.left #创建临时node
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