#对前中后序位置不敏感选择前序
#中序位置主要用于BST, 遍历有序数组
#需要用到子树返回值的，使用后序遍历
from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.elements = []

    #遍历解法
    def pre_traverse_v1(self, root):
        if root==None:
            return
        self.elements.append(root.val)
        self.pre_traverse_v1(root.left)
        self.pre_traverse_v1(root.right)

    def pre_traverse(self, root):
        if root==None:
            return []
        return [root.val] + self.pre_traverse(root.left) + self.pre_traverse(root.right)
    
    #递归解法
    def pre_traverse_v2(self, root):
        res=[]
        if root==None:
            return []
        res.append(root.val)
        res.extend(self.pre_traverse_v2(root.left))
        res.extend(self.pre_traverse_v2(root.right))
        return res

    # 多叉树遍历
    def pre_traverse_multitree(self, root):
        res = []
        if root == None:
            return []
        res.append(root.val)
        for child in root.children:
            res.extend(self.pre_traverse_multitree(child))
        return res

if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().pre_traverse_v2(test_tree))
    print(min("abcde", "abc"))