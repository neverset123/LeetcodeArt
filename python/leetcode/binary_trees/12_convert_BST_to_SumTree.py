#Convert BST to Greater Tree
from utils import from_list

class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        if root==None:
            return
        self.in_traverse(root.right)
        self.sum+=root.val
        root.val=self.sum
        self.in_traverse(root.left)
    
if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    test_tree = from_list(test_data)
    solution = Solution()
    solution.convertBST(test_tree)