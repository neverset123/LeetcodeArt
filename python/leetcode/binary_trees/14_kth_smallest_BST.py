from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.current_rank = 0
        self.rank_val = None

    def kthSmallestEleBST(self, root, rank):
        if root==None:
            return
        self.kthSmallestEleBST(root.left, rank)
        self.current_rank+=1
        if self.current_rank==rank:
            self.rank_val = root.val
            return
        self.kthSmallestEleBST(root.right, rank)
    
if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    rank = 3
    test_tree = from_list(test_data)
    solution = Solution()
    solution.kthSmallestEleBST(test_tree, rank)
    print(solution.rank_val)