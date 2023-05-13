from typing import Optional
import sys
from utils import TreeNode, from_list

class Solution:
    def buildBinaryTreePreIn(self, pre_order_arr, in_order_arr):
        if len(pre_order_arr)==0 or len(in_order_arr)==0:
            return
        root=TreeNode(pre_order_arr[0])
        index=sys.maxsize
        for i, item in enumerate(in_order_arr):
            if item==pre_order_arr[0]:
                index=i
                break
        root.left=self.buildBinaryTreePreIn(pre_order_arr[1:index+1],in_order_arr[:index])
        root.right=self.buildBinaryTreePreIn(pre_order_arr[index+1:], in_order_arr[index+1:])
        return root

    def buildBinaryTreePostIn(self, in_order_arr, post_order_arr) -> Optional[TreeNode]:
        if len(post_order_arr)==0 or len(in_order_arr)==0:
            return
        root=TreeNode(post_order_arr[-1])
        index=sys.maxsize
        for i, item in enumerate(in_order_arr):
            if item==post_order_arr[-1]:
                index=i
                break
        root.left=self.buildBinaryTreePostIn(in_order_arr[:index], post_order_arr[:index])
        root.right=self.buildBinaryTreePostIn(in_order_arr[index+1:], post_order_arr[index:-1])
        return root
    
    def buildBinaryTreePrePost(self, pre, post) -> TreeNode:
        if not post:
            return None
        root = TreeNode(post.pop())
        if len(pre) > 1:
            cut = post.index(pre[1])
            
            root.left = self.constructFromPrePost(pre[1:cut+2], post[:cut+1])
            root.right = self.constructFromPrePost(pre[cut+2:], post[cut+1:])
        return root

if __name__ == "__main__":
    pre_order_arr = [3,9,20,15,7]
    in_order_arr = [9,3,15,20,7]
    print(Solution().buildBinaryTreePreIn(pre_order_arr, in_order_arr))