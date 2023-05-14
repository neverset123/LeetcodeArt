from utils import TreeNode, from_list
from typing import Optional

class Solution:
    def __init__(self):
        self.traverse_string=""

    # construct a string from tree with parenthesis for seperation
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