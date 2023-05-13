#balanced tree: 一颗空树或它的左右两个子树的高度差的绝对值不超过1，
#并且左右两个子树都是一颗平衡二叉树

from typing import Optional
from utils import TreeNode, from_list

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

