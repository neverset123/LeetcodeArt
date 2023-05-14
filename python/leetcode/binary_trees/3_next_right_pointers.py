# next pointer points to next node in breadth first search of perfect binary tree

from typing import Optional
from utils import TreeNode, from_list

class Solution:

    def connectNextToRightNode(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root==None:
            return 
        temp_list = [root]
        while(len(temp_list)!=0):
            size=len(temp_list)
            for i in range(size):
                ele = temp_list.pop(0)
                if i!=size-1:
                    ele.next=temp_list[0]
                if ele.left!=None:
                    temp_list.append(ele.left)
                if ele.right !=None:
                    temp_list.append(ele.right)
        return root
    
    #模拟三叉树遍历
    def connectNextToRightNode_v1(self, root):
        if root==None:
            return 
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if node1==None or node2==None:
            return
        node1.next=node2
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)

if __name__ == "__main__":
    test_data = [1,3,2,5,3,None,9]
    test_tree = from_list(test_data)
    print(Solution().connect(test_tree))