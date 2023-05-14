from utils import TreeNode, from_list

def lca_two_node(root, val1, val2):
    if root==None:
        return
    #root本身是某一子树的根结点
    if root.val==val1 or root.val==val2:
        return root
    left=lca_two_node(root.left, val1, val2)
    right=lca_two_node(root.right, val1, val2)
    #左右返回值都不为空，则当前节点为最近公共祖先
    if left!=None and right!=None:
        return root
    #两节点都不在以root为根的树中，直接返回None
    if left==None and right==None:
        return None
    #只有一个节点存在于root为根的树中，返回该节点
    return left if left!=None else right

def lca_multi_node(root, node_list):
    if root==None:
        return
    vals_list=[node.val for node in node_list]

    if root.val in vals_list:
        return root
    left=lca_multi_node(root.left, node_list)
    right=lca_multi_node(root.right, node_list)
    if left!=None and right!=None:
        return root
    return left if left!=None else right

class Solution:
    def __init__(self):
        self.existence=[0,0]
    
    def lca_v2(self, root, p, q):
        node = self.find(root, p, q)
        if sum(self.existence)!=2:
            return 
        else: 
            return node

    def find(self,root,p,q):
        if root==None:
            return
        left=self.find(root.left, p, q)
        right=self.find(root.right, p, q)
        if left!=None and right!=None:
            return root
        if root.val == p.val: 
            self.existence[0]=1
            return root
        if root.val==q.val: 
            self.existence[1]=1
            return root
        
        return left if left!=None else right

    def lca_bst(self, root, p, q):
        min_val=min(p.val,q.val)
        max_val=max(p.val, p.val)
        return self.find_in_bst(root, min_val, max_val)

    def find_in_bst(self,root,min_value,max_value):
        if root==None:
            return
        if root.val<min_value:
            return self.find_bst(root.right, min_value, max_value)
        elif root.val>max_value:
            return self.find_bst(root.left, min_value, max_value)
        return root


if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,7,1]
    test_tree = from_list(test_data)
    solution=Solution()
    node=lca_two_node(test_tree, 1, 8)
    #node=solution.lca_v2(test_tree, TreeNode(9), TreeNode(7))
    # node=solution.lca_bst(test_tree,TreeNode(3),TreeNode(1))
    print(node.val)