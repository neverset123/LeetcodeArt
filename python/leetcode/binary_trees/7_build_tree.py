from typing import Optional
import sys
from utils import TreeNode, from_list

class Solution:
    def buildBinaryTreePreIn(self, pre_arr, in_arr):
        if not pre_arr:
            return
        root=TreeNode(pre_arr[0])
        index=in_arr.index(pre_arr[0])
        if len(pre_arr)>1:
            root.left=self.buildBinaryTreePreIn(pre_arr[1:index+1],in_arr[:index])
            root.right=self.buildBinaryTreePreIn(pre_arr[index+1:], in_arr[index+1:])
        return root

    def buildBinaryTreePostIn(self, in_arr, post_arr) -> Optional[TreeNode]:
        if not post_arr:
            return
        root=TreeNode(post_arr[-1])
        index=in_arr.index(post_arr[-1])
        if len(post_arr)>1:
            root.left=self.buildBinaryTreePostIn(in_arr[:index], post_arr[:index])
            root.right=self.buildBinaryTreePostIn(in_arr[index+1:], post_arr[index:-1])
        return root
    
    def buildBinaryTreePrePost(self, pre, post) -> TreeNode:
        if not post:
            return
        root = TreeNode(post.pop())
        if len(pre)>1:
            cut = post.index(pre[1])
            root.left = self.constructFromPrePost(pre[1:cut+2], post[:cut+1])
            root.right = self.constructFromPrePost(pre[cut+2:], post[cut+1:])
        return root

    # build binary tree with max value in array as root
    def constructMaximumBinaryTree(self, arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return
        max_val = max(arr)
        index = arr.index(max_val)
        root = TreeNode(max_val)
        root.left=self.constructMaximumBinaryTree(arr[:index])
        root.right=self.constructMaximumBinaryTree(arr[index+1:])
        return root 

if __name__ == "__main__":
    pre_order_arr = [3,9,20,15,7]
    in_order_arr = [9,3,15,20,7]
    root = Solution().buildBinaryTreePreIn(pre_order_arr, in_order_arr)
    print(root.val)