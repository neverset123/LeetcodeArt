# 构造二叉搜索树

from utils import TreeNode

class Solution:
    def __init__(self):
        self.memo={}
        self.trees=[]

    # num of BST can be built with [1...n]
    def numBSTTrees(self, n):
        return self.numBSTCount(1,n)

    def numBSTCount(self, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left>=right:
            return 1
        sum_count = 0
        for i in range(left, right+1):
            left_count=self.numBSTCount(left,i-1)
            right_count=self.numBSTCount(i+1, right)
            sum_count+=left_count*right_count
        self.memo[(left, right)]=sum_count
        return sum_count
    
    # return all the BST can be built with [1...n]
    def generateBSTTrees(self, n):
        return self.build(1, n)
    
    def build(self, left, right):
        #后序遍历需要局部arr，前序遍历需要全局arr
        res=[]
        if left>right:
            res.append(None)
            return res
        for i in range(left, right+1):
            tree_left = self.build(left, i-1)
            tree_right = self.build(i+1, right)
            for j in tree_left:
                for k in tree_right:
                    root=TreeNode(i)
                    root.left=j
                    root.right=k
                    res.append(root)
        return res
    
    # build one balanced bst with sorted array
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root        

if __name__ == "__main__":
    n=0
    solution=Solution()
    print(solution.generateBSTTrees(5))