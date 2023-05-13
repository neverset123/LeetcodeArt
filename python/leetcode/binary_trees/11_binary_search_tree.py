# 左子树上所有结点的值均小于它的根结点的值以及右子树上所有结点的值均大于它的根结点的值
# 提供 logN 级别的增删查改效率
# 可以与二分查找结构结合，进行快速查找

from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.valid=True
        self.preNode=None

    # 通过中序遍历BST是否递增，判断BST有效性
    def isValidBST(self, root):
        self.traverse(root)
        return self.valid
    
    def traverse(self, root):
        if root==None:
            return
        self.traverse(root.left)
        if self.preNode!=None and self.preNode.val>=root.val:
            self.valid=False
        self.preNode=root
        print(root.val)
        self.traverse(root.right)

    # BST解题的通用遍历框架
    def search(self, root, target):
        if root==None:
            return
        if root.val==target:
            return root
        elif root.val>target:
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)

    def insert(self, root, val):
        if root==None:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insert(root.left, val)
        elif root.val<val:
            root.right=self.insert(root.right, val)
        return root

    def delete(self, root, val):
        if root==None:
            return
        if root.val==val:
            if root.left==None:
                return root.right
            if root.right==None:
                return root.left
            else:
                node_next=self.min(root.right)
                root.right=self.delete(root.right, node_next.val)
                #root.val=node_next.val
                node_next.left=root.left
                node_next.right=root.right
                root=node_next
        elif root.val>val:
            root.left=self.delete(root.left, val)
        else:
            root.right=self.delete(root.right, val)
        return root
    
    def min(self, root):
        if root==None:
            return
        return root if root.left == None else self.min(root.left)

if __name__ == "__main__":
    test_data = [5,3,7,2,4,None,None,1]
    test_tree = from_list(test_data)
    solution = Solution()
    solution.insert(test_tree, 6)
    solution.traverse(test_tree)
    # solution.delete(test_tree, 2)
    # solution.traverse(test_tree)