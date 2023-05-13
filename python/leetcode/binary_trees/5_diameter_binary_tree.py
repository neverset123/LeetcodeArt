from typing import Optional
from utils import TreeNode, from_list


class Solution:
    def __init__(self):
        self.diameter_max=0

    def diameter(self, root):
        self.maxDepth(root)
        return self.diameter_max
        
    def maxDepth(self, root):
        if root==None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        self.diameter_max=max(self.diameter_max, left_depth+right_depth)
        return max(left_depth, right_depth)+1

if __name__ == "__main__":
    test_data = [9,None, 1,2,3,4,5, 6, None]
    test_tree = from_list(test_data)
    print(Solution().diameter(test_tree))