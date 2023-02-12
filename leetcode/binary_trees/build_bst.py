class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.memo={}
        self.trees=[]

    def num_bst(self, n):
        return self.count(1,n)

    def count(self, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left>=right:
            return 1
        sum_count = 0
        for i in range(left, right+1):
            left_count=self.count(left,i-1)
            right_count=self.count(i+1, right)
            sum_count+=left_count*right_count
        return sum_count
    
    def build_bst(self, n):
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


if __name__ == "__main__":
    n=5
    solution=Solution()
    print(solution.build_bst(n))