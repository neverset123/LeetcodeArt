from typing import Optional
import sys
from utils import TreeNode, from_list

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