import sys
from utils import TreeNode, from_list
from typing import List, Optional

class Solution:
    def __init__(self):
        self.max_sum=0
    
    def maxSum(self, root):
        self.traverse(root)
        return self.max_sum if self.max_sum>=0 else 0

    # return struct [is_valid_bst, min_val, max_val, max_val, max_sum]
    def traverse(self, root):
        if root==None:
            return [1, sys.maxsize, -sys.maxsize, 0]
        
        res_left = self.traverse(root.left)
        res_right = self.traverse(root.right)
        res=[]
        if (res_left[0]==1 and res_right[0]==1 and 
            res_left[2]<root.val and res_right[1]>root.val):
            res.append(1)
            res.append(min(res_left[1], root.val))
            res.append(max(res_right[2], root.val))
            res.append(res_left[3]+res_right[3]+root.val)
            self.max_sum=max(self.max_sum, res[3])
        else:
            res.append(0)
        return res

if __name__ == "__main__":
    test_data = [5,4,8,3,None,6,3]
    root = from_list(test_data)
    print(Solution().maxSum(root))