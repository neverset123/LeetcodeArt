from utils import TreeNode, from_list
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return
        left=self.invertTree(root.right)
        right=self.invertTree(root.left)
        root.left=left
        root.right=right
        return root