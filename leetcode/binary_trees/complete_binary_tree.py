#子问题复杂度是while循环logN，子问题个数为树的高度logN，所以总复杂度为logN*logN
#该题为计算完整二叉树地节点数
#完整二叉树的题与层序遍历关联

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

class Solution:
    def count_node(self,root):
        if root==None:
            return 0
        left=root.left
        right=root.right
        h_left=0
        h_right=0
        while(left!=None):
            left=left.left
            h_left+=1
        while(right!=None):
            right=right.right
            h_right+=1
        if h_left==h_right:
            return int(math.pow(2, h_left+1))-1
        else:
            return 1+self.count_node(root.left)+self.count_node(root.right)

if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    test_tree = from_list(test_data)
    solution=Solution()
    print(solution.count_node(test_tree))
