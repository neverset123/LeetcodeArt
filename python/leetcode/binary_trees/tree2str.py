# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traverse_string=""

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root==None:
            return
        self.traverse_string+="("+str(root.val)
        if root.left==None and root.right!=None:
            self.traverse_string+="()"
        self.tree2str(root.left)
        self.tree2str(root.right)
        self.traverse_string+=")"
        return self.traverse_string[1:-1]