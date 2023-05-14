from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.subtree=dict()
        self.duplicate_subtree_list = []

    def post_serialize(self, root):
        if root==None:
            return "None"
        left=self.post_serialize(root.left)
        right=self.post_serialize(root.right)
        elements_str = left+","+right+","+str(root.val)
        if elements_str in self.subtree:
            self.subtree[elements_str]+=1
            if self.subtree[elements_str]==2:
                self.duplicate_subtree_list.append(root)
        else: self.subtree[elements_str]=1
        return elements_str

    def find_duplicates(self, root):
        self.post_serialize(root)
        return self.duplicate_subtree_list


if __name__ == "__main__":
    test_data = [1,2,3,4,None,2,4,None,None,4]
    test_tree = from_list(test_data)
    solution = Solution()
    print([item.val for item in solution.find_duplicates(test_tree)])
